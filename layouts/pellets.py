import pandas as pd
from dash import Dash, dcc, html

data = pd.read_excel("fuel_comparison_sheets.xlsx", sheet_name="Pellets", skiprows=[1])

# print(data)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Pellets"),
                html.P(
                    "The usual unit used for wood pellets is the ton, equivalent to 2000 pounds. Pellets produces 8,000 BTU / lb (British Thermal Unit.)"
                ),
            ]
        ),
        html.Div(
            children=dcc.Graph(
                id="pellets",
                figure={
                    "data": [
                        {
                            "x": data["PELLETS"],
                            "y": data["80% Eff."],
                            "type": "lines",
                            "name": "80% Eff",
                        },
                        {
                            "x": data["PELLETS"],
                            "y": data["85% Eff."],
                            "type": "lines",
                            "name": "85% Eff",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Cost of Pellets per Tons",
                            "x": 0.01,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True, "title": "$/ton"},
                        "yaxis": {
                            "tickprefix": "$",
                            "title": "$/kWh",
                            "fixedrange": True,
                        },
                        "colorway": ["dark-green", "grey"],
                    },
                },
            ),
            className="card",
        ),
    ],
    className="pellets-graph",
)
