# Electric Vehicle Market Performance & Insights

## Abstract
This project explores electric-vehicle market records to compare price, driving range, battery capacity, efficiency, customer rating, annual sales, vehicle category, manufacturer and market region. A Flask web application presents interactive charts and a narrative page, while a Tableau workbook can be authored from the same data and embedded after publishing.

## Objectives
1. Summarize important EV market indicators in one dashboard.
2. Compare pricing and range across vehicle categories.
3. Explore the relationship between battery capacity and driving range.
4. Compare recorded annual sales across manufacturers and market regions.
5. present a concise, evidence-led story and disclose data-quality limitations.

## Data and methodology
The supplied training CSV contains 200,000 rows and 37 columns; the supplied test CSV contains 100,000 rows. The dashboard currently uses the training CSV for descriptive analysis. The data include vehicle and manufacturer identifiers, model year, category, market region, battery specifications, range, efficiency, price, rating and annual sales. Numeric summaries are computed with pandas and visualized with Plotly in the Flask application. Tableau summary CSVs are provided as optional worksheet-ready aggregates.

## Findings from the training dataset
- Mean range: approximately 324.5 km; median range: 337.9 km.
- Mean listed price: approximately US$64,920.53; median price: US$42,814.93. The gap between mean and median suggests the price distribution is right-skewed.
- Mean customer rating: approximately 4.09 out of 5.
- Battery capacity and range have a Pearson correlation of approximately 0.267, a modest positive association rather than proof that battery size alone determines range.
- Luxury Sedan has the highest mean range among the categories in this dataset, approximately 550.6 km.
- South Asia has the largest sum of recorded annual sales in the training data. This should be treated cautiously because the sales field contains an extreme value.

## Dashboard components
- Manufacturer sales: compare average annual sales by manufacturer; use medians and tooltips to avoid hiding outliers.
- Average price by category: compare average listed price across vehicle categories.
- Battery capacity vs. range: scatterplot colored by battery type, with model and price in the tooltip.
- Regional sales mix: compare summed recorded annual sales across market regions.
- Filters: market region and vehicle category.

## Storyline
1. **Battery size and driving range:** battery capacity and range move together moderately, but other design factors affect the range.
2. **Category-level trade-offs:** the categories with the longest average range may also have much higher prices; compare both metrics instead of ranking on range alone.
3. **Regional and sales interpretation:** compare regional patterns while checking outliers and sample coverage; totals in a synthetic or sampled dataset should not be treated as verified real-world market share.

## Data quality and limitations
The training data has 18,996 missing cells, one duplicated row and one duplicate vehicle ID. `annual_sales_units` has a maximum of 1,066,612 while its median is 3,949.5, so sales aggregates can be distorted by outliers. The dataset provenance and whether values represent real observations or synthetic records have not been independently verified. Results are descriptive, not causal, and should not be presented as definitive real-world market estimates.

## Conclusion
The dashboard consolidates core EV market metrics and makes category, manufacturer and region comparisons easier. Battery capacity has a positive but modest relationship with range in the supplied data, while category-level range and price differences make segmentation important. Before using results for decisions, validate source provenance, inspect missing values and outliers, and confirm results against a trusted market dataset.

## Future work
- Document and resolve missing values and duplicates, retaining a reproducible cleaning log.
- Add robust sales visualizations using median and percentile bands.
- Include model-year trends and region/category drill-downs.
- Validate findings against trusted published market data.
- Publish the Tableau workbook/story and set their URLs in the Flask environment variables.
