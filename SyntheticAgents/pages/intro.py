import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction ", order=0)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Sweden Socioeconomic Characteristics Dataset Overview"),
        "The Synthetic Sweden Mobility (SySMo) model provides a simplified yet statistically realistic microscopic representation of the real population of Sweden. The agents in this synthetic population contain socioeconomic attributes, household characteristics, and corresponding activity plans for an average weekday. This agent-based modelling approach derives the transportation demand from the agents’ planned activities using various transport modes (e.g., car, public transport, bike, and walking).Synthetic Agents:This dataset contains all agents in Sweden and their socioeconomic characteristics.",
        html.Br(),html.Br(),
        "This is the URL of the dataset. (https://zenodo.org/records/10648078)",
        ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        "Original File name: 1_syn_pop_all.parquet",html.Br(),
        "Smapled File name: sampled_dataset.csv",html.Br(),
        "Number of Attributes: 16 columns",
        html.Br(),html.Br(),
        html.B("- Agent ID"),
        html.Br(),
        html.B("- Zone code of Demographic statistical areas (DeSO)"),
        html.Br(),
        html.B("- Municipality code"),
        html.Br(),
        html.B("- Marital Status (single/ couple/ child)"),
        html.Br(),
        html.B("- Gender (0 = Male, 1 = Female)"),
        html.Br(),
        html.B("- Age"),
        html.Br(),
        html.B("- A unique identifier for households"),
        html.Br(),
        html.B("- Type of households (single/ couple/ other)"),
        html.Br(),
        html.B("- Number of people living in the households"),
        html.Br(),
        html.B("- Number of children less than six years old in the household"),
        html.Br(),
        html.B("- Employment Status (0 = Not Employed, 1 = Employed)"),
        html.Br(),
        html.B("- Studenthood Status (0 = Not Student, 1 = Student)"),
        html.Br(),
        html.B("- Number of cars owned by an individual "),
        html.Br(),
        html.B("- Number of cars in the household "),
        html.Br(),
        html.B("- Status of the individual (1=feasible, 0=infeasible) "),
        html.Br(),html.Br(),
        html.B("Income Class"),
        html.Br(),html.Br(),
        html.B("- 0 = No Income"), html.Br(),
        html.B("- 1 = Low Income"), html.Br(),
        html.B("- 2 = Lower-middle Income"), html.Br(),
        html.B("- 3 = Upper-middle Income"), html.Br(),
        html.B("- 4 = High Income"),
    ])
], className="p-4 m-2", style={"background-color": "#e3f2fd"})
