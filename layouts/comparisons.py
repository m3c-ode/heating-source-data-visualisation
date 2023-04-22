import pandas as pd
from dash import Dash, dcc, html

# TODO: add interactivity for comparison
layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H2("Conclusion: Comparing the different heat sources"),
                html.P(
                    "Unit prices can vary greatly between heat source (i.e 1 therm of natural gas VS 1 cord of dry pine). So, how can we compare heat source prices in terms of a single common unit? "
                    "Trethewey’s worksheet converts the costs of all heat sources to the standard pricing unit for electricity, cost per kilowatt-hour. "
                    "For example, let’s take a closer look at wood pellets and oil. Unsurprisingly, a gallon of oil is cheaper than a ton of wood pellets. However, in terms of cost per kilowatt-hour, the two aren’t too different from each other. "
                ),
                html.H4("But what do those costs mean for you?"),
                html.P(
                    "The answer depends on different factors, such as availability of resources in the location and its related costs."
                ),
                html.P(
                    "To determine the best value heat source, you will want to look up the local costs per unit and find its approximate value on Trethewey’s chart. You can generally find these on utility bills and some government or company websites."
                ),
                html.P(
                    "Let’s use the pellets and oil example again to see which one is better from a price standpoint. For example, one ton of wood pellets could cost $234.00 per pound, and oil could cost $2.16 per gallon. Find the closest number to those prices on the table and see how much each heat source will cost you per kilowatt-hour."
                ),
                html.P(
                    "According to Trethewey’s tables, you would save slightly more money by using pellets as a heat source instead of oil."
                ),
            ]
        ),
        # html.Div(
        #     children=dcc.Graph(
        #         id="elec",
        #         figure={
        #             "data": [
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 1"],
        #                     "type": "lines",
        #                     "name": "ER COP = 1",
        #                 },
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 2"],
        #                     "type": "lines",
        #                     "name": "ASP COP = 2",
        #                 },
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 2.5"],
        #                     "type": "lines",
        #                     "name": "ASP COP = 2.5",
        #                 },
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 3"],
        #                     "type": "lines",
        #                     "name": "ASP COP = 3",
        #                 },
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 3.5"],
        #                     "type": "lines",
        #                     "name": "ASP COP = 3.5",
        #                 },
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 4"],
        #                     "type": "lines",
        #                     "name": "GGSP COP = 4",
        #                 },
        #                 {
        #                     "x": data["Utility Rate"],
        #                     "y": data["COP = 5"],
        #                     "type": "lines",
        #                     "name": "GGSP COP = 5",
        #                 },
        #             ],
        #             "layout": {
        #                 "title": {
        #                     "text": "Cost of electricity per Kilowatt per hour",
        #                     "x": 0.01,
        #                     "xanchor": "left",
        #                 },
        #                 "xaxis": {"fixedrange": True, "title": "$/kWh"},
        #                 "yaxis": {
        #                     "tickprefix": "$",
        #                     "title": "$/kWh",
        #                     "fixedrange": True,
        #                 },
        #                 "colorway": [
        #                     "orange",
        #                     "green",
        #                     "grey",
        #                     "pink",
        #                     "cyan",
        #                     "teal",
        #                     "red",
        #                 ],
        #             },
        #         },
        #     ),
        #     className="card",
        # ),
    ],
    # className="wrapper",
)
