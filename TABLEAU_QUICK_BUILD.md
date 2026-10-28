# Tableau dashboard & story quick-build guide (target: 20–30 minutes)

The Flask dashboard and story are already implemented in this project. This guide is for authoring and publishing the required *native Tableau* views. They cannot be marked published until you create and publish them in your Tableau account.

## 1. Open the data (2–4 min)
1. Open Tableau Public / Tableau Desktop Public Edition and sign in.
2. Connect to Text File and select `data/ev_market_train.csv` from this extracted project folder.
3. Keep the full training file as the primary data source for all the worksheets so filters can be shared easily. The `tableau_*_summary.csv` files are optional shortcut datasets, not required for the first version.

## 2. Create four worksheets (10–12 min)
Create and name each worksheet exactly as follows.

- **Sales by Manufacturer**: drag `manufacturer` to Rows and `annual_sales_units` to Columns; set the measure to Average; sort descending. Show only Top 12 manufacturers by AVG(annual_sales_units). Put median annual sales in the tooltip if time allows.
- **Average Price by Category**: drag `category` to Columns and `price_usd` to Rows; use AVG(price_usd), sort descending and format as USD.
- **Battery vs Range**: drag `battery_capacity_kwh` to Columns and `range_km` to Rows; select Circle marks; drag `battery_type` to Color and `model_name`, `manufacturer`, `price_usd` to Tooltip.
- **Sales by Region**: drag `market_region` to Columns and `annual_sales_units` to Rows; use SUM(annual_sales_units), sort descending and label the bars. A bar chart is preferable to a map for these broad market-region labels.

Optional KPI tiles for the dashboard: COUNTD(vehicle_id), MEDIAN(price_usd), AVG(range_km), AVG(customer_rating). If `COUNTD` or median settings are unfamiliar, use a simple text sheet with the measure and keep moving.

## 3. Assemble the dashboard (4–6 min)
1. Create a new Dashboard named **EV Market Overview** and set a fixed size around 1200 × 800.
2. Put a title at the top: **Electric Vehicle Market Performance & Insights**.
3. Arrange Sales by Manufacturer and Average Price by Category in the top row; Battery vs Range and Sales by Region in the bottom row.
4. Show `market_region` and `category` filters. For each filter use **Apply to Worksheets → All Using This Data Source**.
5. Add this small footer: `Source: supplied EV training dataset. Descriptive analysis only; see data-quality note.`

## 4. Create the Tableau Story (3–5 min)
Create a Story named **EV Market Insights Story**, and add three story points using the relevant worksheets/dashboard:

1. **Battery capacity and range** — Explain that the Pearson correlation is about 0.267 (moderate/weak positive association; no causal claim).
2. **Range and affordability differ by category** — Luxury Sedan has the highest average range in this dataset at about 550.6 km; compare category pricing before making recommendations.
3. **Market segments need context** — South Asia has the highest sum of recorded annual sales in the training data, but the sales field contains an extreme outlier. Interpret the chart cautiously.

## 5. Publish and embed (5 min, if account works)
1. Publish/save the workbook to Tableau Public and make sure the dashboard/story views are visible on your profile.
2. Copy the actual published dashboard view URL and story view URL.
3. In PowerShell from the project directory, set the URLs and start Flask:

```powershell
$env:TABLEAU_DASHBOARD_URL = "PASTE_REAL_PUBLISHED_DASHBOARD_VIEW_URL"
$env:TABLEAU_STORY_URL = "PASTE_REAL_PUBLISHED_STORY_VIEW_URL"
python app.py
```

4. Open `http://127.0.0.1:5000/tableau`. The Tableau Embedding API v3 component is already wired into this page.

**Do not paste example URLs or claim it is embedded until both real views load.** Tableau Public is intended for publicly shared visualizations; do not upload confidential data.

## Accurate data-quality note
The training dataset has 200,000 rows, 37 columns, 18,996 missing cells, one duplicated row, and one duplicate vehicle ID. `annual_sales_units` has a maximum of 1,066,612 versus a median of 3,949.5, so sales sums can be distorted. Mention this in your methodology/footer and avoid treating the result as verified real-world market share.

Official references:
- Tableau Embedding API basics: https://help.tableau.com/current/api/embedding_api/en-us/docs/embedding_api_basic.html
- Tableau Public FAQ: https://help.tableau.com/current/pro/desktop/en-us/public_faq.htm
