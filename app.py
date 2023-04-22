# https://hvacrschool.com/how-to-compare-heat-sources-for-cost-effectiveness/

import pandas as pd
from dash import Dash, dcc, html, Output, Input
from layouts.oil import layout as oil_layout
from layouts.propane import layout as propane_layout
from layouts.pellets import layout as pellets_layout
from layouts.wood import layout as wood_layout
from layouts.electric import layout as wood_layout
from layouts.comparisons import layout as comparison_layout

file_name = "fuel_comparison_sheets.xlsx"

data = pd.read_excel("fuel_comparison_sheets.xlsx")

# Creates a ExcelFile object
xl = pd.ExcelFile(file_name)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?" "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

# print(data)
# Gets and reads sheet names
# print(xl.sheet_names)

dfs = [
    pd.read_excel(xl, sheet_name=sheet_name, skiprows=[1])
    for sheet_name in xl.sheet_names
]
# print(dfs[0])

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Comparison cost of different heat sources"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🔥🔥🔥", className="header-emoji"),
                html.H1(
                    "Comparing costs of different heating sources",
                    className="header-title",
                ),
                html.P(
                    "Based of the analytics of Ross Trethewey of TE2 Engineering",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.H2("Introduction"),
                html.P(
                    "Because we are comparing different sources of energy, they will have different"
                    " measures of units (i.e. wood vs electricity...). "
                    "In this article, we will show the costs of different heating source and try to compare them with each other. "
                    "To be able to compare those sources, we need to compare them for equivalent energetic heat output as well."
                    "Thus, depending on their unit, their volume and their cost per unit, we will be able to compare those different sources graphically"
                ),
            ],
            className="introduction",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H3("Natural Gas"),
                        html.P(
                            "The unit used for natural gas is the therm, equivalent to 100 cubic volume. Natural gas produces 100,000 BTU / therm (British Thermal Unit.)"
                        ),
                    ]
                ),
                html.Div(
                    children=dcc.Graph(
                        id="gas",
                        figure={
                            "data": [
                                {
                                    "x": dfs[0]["NATURAL GAS"],
                                    "y": dfs[0]["80% Eff."],
                                    "type": "lines",
                                    "name": "80% Eff",
                                },
                                {
                                    "x": dfs[0]["NATURAL GAS"],
                                    "y": dfs[0]["95% Eff."],
                                    "type": "lines",
                                    "name": "95% Eff",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Cost of Natural Gas per Therm",
                                    "x": 0.01,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True, "title": "$/therm"},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "title": "$/kWh",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897", "red"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            # className="first-graph",
        ),
        oil_layout,
        propane_layout,
        pellets_layout,
        wood_layout,
        # comparison_layout,
        html.Div(
            children=[
                html.P("References:"),
                html.P("References:"),
                html.P("References:"),
                html.P("References:"),
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
