from pathlib import Path
import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import plotly.express as px
import plotly.io as pio

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = Path(os.getenv("EV_DATA_PATH", BASE_DIR / "data" / "ev_market_train.csv"))
app = Flask(__name__)

def load_data():
    df = pd.read_csv(DATA_PATH)
    numeric = df.select_dtypes(include="number").columns
    df[numeric] = df[numeric].replace([np.inf, -np.inf], np.nan)
    return df

def make_chart(fig):
    fig.update_layout(
        template="plotly_white", margin=dict(l=20, r=20, t=55, b=20),
        font=dict(family="Arial, sans-serif", size=12),
        title_font=dict(size=17), height=360
    )
    return pio.to_html(fig, full_html=False, include_plotlyjs=False, config={"responsive": True})

def filtered_data(df, region, category):
    if region and region != "All":
        df = df[df["market_region"] == region]
    if category and category != "All":
        df = df[df["category"] == category]
    return df

@app.route("/")
def index():
    df = load_data()
    regions = ["All"] + sorted(df["market_region"].dropna().unique().tolist())
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
    region = request.args.get("region", "All")
    category = request.args.get("category", "All")
    view = filtered_data(df, region, category)
    if view.empty:
        view = df
    avg_range = float(view["range_km"].mean())
    avg_price = float(view["price_usd"].mean())
    avg_rating = float(view["customer_rating"].mean())
    avg_sales = float(view["annual_sales_units"].mean())
    total = len(view)

    sales = view.groupby("manufacturer", as_index=False)["annual_sales_units"].mean().nlargest(12, "annual_sales_units")
    fig_sales = px.bar(sales.sort_values("annual_sales_units"), x="annual_sales_units", y="manufacturer",
                       orientation="h", title="Top manufacturers by average annual sales",
                       labels={"annual_sales_units":"Average annual sales (units)", "manufacturer":"Manufacturer"})
    cat = view.groupby("category", as_index=False).agg(avg_price=("price_usd","mean"), avg_range=("range_km","mean"))
    fig_price = px.bar(cat.sort_values("avg_price", ascending=False), x="category", y="avg_price",
                       title="Average price by vehicle category", labels={"category":"Category","avg_price":"Average price (USD)"})
    fig_scatter = px.scatter(view.sample(min(2500, len(view)), random_state=42),
                             x="battery_capacity_kwh", y="range_km", color="battery_type",
                             hover_data=["manufacturer","model_name","price_usd"],
                             title="Battery capacity vs driving range",
                             labels={"battery_capacity_kwh":"Battery capacity (kWh)","range_km":"Range (km)"},
                             opacity=0.65)
    region_sales = view.groupby("market_region", as_index=False)["annual_sales_units"].sum()
    fig_region = px.pie(region_sales, names="market_region", values="annual_sales_units",
                        title="Share of recorded annual sales by market region", hole=0.35)

    return render_template("index.html", regions=regions, categories=categories,
        region=region, category=category, total=total,
        avg_range=avg_range, avg_price=avg_price, avg_rating=avg_rating, avg_sales=avg_sales,
        chart_sales=make_chart(fig_sales), chart_price=make_chart(fig_price),
        chart_scatter=make_chart(fig_scatter), chart_region=make_chart(fig_region))

@app.route("/story")
def story():
    df = load_data()
    n = len(df)
    avg_range = df["range_km"].mean()
    median_price = df["price_usd"].median()
    best_category = df.groupby("category")["range_km"].mean().idxmax()
    best_range = df.groupby("category")["range_km"].mean().max()
    best_sales_mfr = df.groupby("manufacturer")["annual_sales_units"].mean().idxmax()
    best_sales = df.groupby("manufacturer")["annual_sales_units"].mean().max()
    corr = df[["battery_capacity_kwh", "range_km"]].corr().iloc[0,1]
    efficient = df.groupby("category")["efficiency_wh_per_km"].mean().idxmin()
    return render_template("story.html", n=n, avg_range=avg_range, median_price=median_price,
        best_category=best_category, best_range=best_range, best_sales_mfr=best_sales_mfr,
        best_sales=best_sales, corr=corr, efficient=efficient)

@app.route("/tableau")
def tableau():
    # Defaults are the user's published Tableau Public views. Environment variables
    # can override these URLs when deploying to another Tableau workbook.
    dashboard_url = os.getenv(
        "TABLEAU_DASHBOARD_URL",
        "https://public.tableau.com/views/EVSALESBOOK/EVMARKETOVERVIEW"
    )
    story_urls = [
        os.getenv("TABLEAU_STORY1_URL", "https://public.tableau.com/views/EVSALESBOOK/Story1"),
        os.getenv("TABLEAU_STORY2_URL", "https://public.tableau.com/views/EVSALESBOOK/Story2"),
        os.getenv("TABLEAU_STORY3_URL", "https://public.tableau.com/views/EVSALESBOOK/Story3"),
    ]
    return render_template("tableau.html", dashboard_url=dashboard_url, story_urls=story_urls)

@app.route("/health")
def health():
    return {"status": "ok", "data_file_exists": DATA_PATH.exists()}

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
            host="127.0.0.1", port=int(os.getenv("PORT", "5000")))
