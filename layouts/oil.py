import pandas as pd
from dash import Dash, dcc, html

data = pd.read_excel("fuel_comparison_sheets.xlsx", sheet_name="Oil", skiprows=[1])

# print(data)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Oil"),
                html.P(
                    "The unit used for oil is the gallon, equivalent to 3.8L. Oil produces 138,700 BTU / gallon (British Thermal Unit.)"
                ),
            ]
        ),
        html.Div(
            children=dcc.Graph(
                id="oil",
                figure={
                    "data": [
                        {
                            "x": data["OIL"],
                            "y": data["80% Eff."],
                            "type": "lines",
                            "name": "80% Eff",
                        },
                        {
                            "x": data["OIL"],
                            "y": data["85% Eff."],
                            "type": "lines",
                            "name": "85% Eff",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Cost of Oil per Gallon",
                            "x": 0.01,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True, "title": "$/gal"},
                        "yaxis": {
                            "tickprefix": "$",
                            "title": "$/kWh",
                            "fixedrange": True,
                        },
                        "colorway": ["pink", "orange"],
                    },
                },
            ),
            className="card",
        ),
    ],
    className="wrapper",
)
