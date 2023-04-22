import pandas as pd
from dash import Dash, dcc, html

data = pd.read_excel("fuel_comparison_sheets.xlsx", sheet_name="Elec", skiprows=[0, 2])

# print(data)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Electric"),
                html.P(
                    "The usual unit used for electricity heating is the kWh (KiloWatts per hour), with 1 Watt corresponding to to the transfer of 1 joule per second. The data used takes efficiency and energy content into account"
                    "When talking about electric heating, we also have different Coefficient of Performance (COP), corresponding to different sources."
                ),
                html.Ul(
                    children=[
                        html.Li("Electric resistance (ER) heaters have a COP of 1"),
                        html.Li(
                            "Air source pumps (ASP) generally have COPs ranging from 2-4."
                        ),
                        html.Li(
                            "Geothermal ground source pumps (GGSP) have COPs ranging from 4-5."
                        ),
                    ]
                ),
            ]
        ),
        html.Div(
            children=dcc.Graph(
                id="elec",
                figure={
                    "data": [
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 1"],
                            "type": "lines",
                            "name": "ER COP = 1",
                        },
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 2"],
                            "type": "lines",
                            "name": "ASP COP = 2",
                        },
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 2.5"],
                            "type": "lines",
                            "name": "ASP COP = 2.5",
                        },
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 3"],
                            "type": "lines",
                            "name": "ASP COP = 3",
                        },
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 3.5"],
                            "type": "lines",
                            "name": "ASP COP = 3.5",
                        },
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 4"],
                            "type": "lines",
                            "name": "GGSP COP = 4",
                        },
                        {
                            "x": data["Utility Rate"],
                            "y": data["COP = 5"],
                            "type": "lines",
                            "name": "GGSP COP = 5",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Cost of electricity per Kilowatt per hour",
                            "x": 0.01,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True, "title": "$/kWh"},
                        "yaxis": {
                            "tickprefix": "$",
                            "title": "$/kWh",
                            "fixedrange": True,
                        },
                        "colorway": [
                            "orange",
                            "green",
                            "grey",
                            "pink",
                            "cyan",
                            "teal",
                            "red",
                        ],
                    },
                },
            ),
            className="card",
        ),
    ],
    className="pellets-graph",
)
