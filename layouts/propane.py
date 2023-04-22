import pandas as pd
from dash import Dash, dcc, html

data = pd.read_excel(
    "fuel_comparison_sheets.xlsx", sheet_name="Liquid Propane", skiprows=[1]
)

# print(data)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Propane"),
                html.P(
                    "The unit used for propane is the gallon, equivalent to 3.8L. Propane produces 92,000 BTU / gallon (British Thermal Unit.)"
                ),
            ]
        ),
        html.Div(
            children=dcc.Graph(
                id="propane",
                figure={
                    "data": [
                        {
                            "x": data["LP"],
                            "y": data["80% Eff."],
                            "type": "lines",
                            "name": "80% Eff",
                        },
                        {
                            "x": data["LP"],
                            "y": data["95% Eff."],
                            "type": "lines",
                            "name": "95% Eff",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Cost of Propane per Gallon",
                            "x": 0.01,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True, "title": "$/gal"},
                        "yaxis": {
                            "tickprefix": "$",
                            "title": "$/kWh",
                            "fixedrange": True,
                        },
                        "colorway": ["magenta", "light-green"],
                    },
                },
            ),
            className="card",
        ),
    ],
    className="wrapper",
)
