import pandas as pd
from dash import Dash, dcc, html

data = pd.read_excel("fuel_comparison_sheets.xlsx", sheet_name="Wood", skiprows=[1])

# print(data)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Wood"),
                html.P(
                    "The usual unit used for wood is the cord, equivalent to 5000 pounds or 957.5 liquid gallons. Wood (Dry pine) produces 14.3 MBTU / lb (British Thermal Unit.)"
                ),
            ]
        ),
        html.Div(
            children=dcc.Graph(
                id="wood",
                figure={
                    "data": [
                        {
                            "x": data["WOOD"],
                            "y": data["70% Eff."],
                            "type": "lines",
                            "name": "70% Eff",
                        },
                        {
                            "x": data["WOOD"],
                            "y": data["80% Eff."],
                            "type": "lines",
                            "name": "80% Eff",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Cost of Wood per Cord",
                            "x": 0.01,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True, "title": "$/cord"},
                        "yaxis": {
                            "tickprefix": "$",
                            "title": "$/kWh",
                            "fixedrange": True,
                        },
                        "colorway": ["purple", "pink"],
                    },
                },
            ),
            className="card",
        ),
    ],
    className="wrapper",
)
