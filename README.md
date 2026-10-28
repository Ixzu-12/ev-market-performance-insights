# Electric Vehicle Market Performance & Insights — Flask App

## Included
- Interactive Flask dashboard with market-region and vehicle-category filters
- Four Plotly visualizations: manufacturer sales, category pricing, battery capacity vs range, regional sales share
- Data-story page with descriptive findings calculated from the training dataset
- Tableau embed page that accepts published dashboard/story URLs through environment variables
- Health endpoint at `/health`

## Requirements
- Python 3.10–3.12 recommended
- Internet access for the Plotly JavaScript CDN in the browser

## Run on Windows PowerShell
From the project folder:

```powershell
py -3.11 -m venv myenv
.\myenv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

If your existing virtual environment is already named `myenv`, activate it instead of recreating it:

```powershell
.\myenv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`. Test `http://127.0.0.1:5000/health`.

## Configure Tableau embedding
Publish the dashboard and story to Tableau Public/Server, then use the corresponding embed/view URLs:

```powershell
$env:TABLEAU_DASHBOARD_URL = "PASTE_PUBLISHED_DASHBOARD_EMBED_URL_HERE"
$env:TABLEAU_STORY_URL = "PASTE_PUBLISHED_STORY_EMBED_URL_HERE"
python app.py
```

Open `http://127.0.0.1:5000/tableau`.

The Tableau embed page deliberately shows a setup message if URLs are missing; the rest of the Flask app works without Tableau credentials or published views. Do not paste private Tableau credentials into source code.

## Data
`data/ev_market_train.csv` and `data/ev_market_test.csv` are the supplied datasets. The current dashboard uses the training dataset for descriptive analysis. The test file is included for future validation or additional analysis.

## Suggested 1-hour completion checklist
1. Install dependencies and run the app.
2. Verify dashboard filters, all four charts, story page and `/health`.
3. If a Tableau workbook is already published, add its URLs and test `/tableau`.
4. If not published, submit the working Flask dashboard and clearly mark Tableau URLs as pending rather than claiming a published embed is complete.
5. Add the GitHub repository URL to your tracker after pushing the project. Add a demo URL only after deploying it to a public host.

## Notes
- Findings are descriptive summaries of the supplied synthetic/recorded data and are not causal claims.
- Keep debug mode off unless actively developing locally.


## Tableau-ready materials
See `TABLEAU_QUICK_BUILD.md` for a fast worksheet/dashboard/story recipe and publish/embedding steps. Pre-aggregated Tableau worksheet data lives in `data/tableau_*_summary.csv`; the full training and test datasets remain included. `data_quality_profile.json` records quick quality checks and headline statistics.

**Data quality note:** the training dataset has missing cells, one duplicate row, one duplicate vehicle ID, and a very large outlier in annual sales. Interpret sales sums with caution and disclose these issues in your presentation.


### Published Tableau Public integration

The `/tableau` page is preconfigured with the published EV Sales Book views provided for this project:
- Dashboard: `https://public.tableau.com/views/EVSALESBOOK/EVMARKETOVERVIEW`
- Story 1: `https://public.tableau.com/views/EVSALESBOOK/Story1`
- Story 2: `https://public.tableau.com/views/EVSALESBOOK/Story2`
- Story 3: `https://public.tableau.com/views/EVSALESBOOK/Story3`

Run Flask and open `http://127.0.0.1:5000/tableau` to view the embedded dashboard and all three story views. The links can be overridden with `TABLEAU_DASHBOARD_URL`, `TABLEAU_STORY1_URL`, `TABLEAU_STORY2_URL`, and `TABLEAU_STORY3_URL` environment variables.
