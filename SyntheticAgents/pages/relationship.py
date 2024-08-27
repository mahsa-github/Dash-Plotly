import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/relationship', name="Relationship 📈", order=3)

####################### DATASET #############################
file_path = r'C:\Users\Mahsa\EDA_dashplotly\sampled_dataset.csv'
data_df = pd.read_csv(file_path)

# Convert the income_class column to categorical
data_df['income_class'] = data_df['income_class'].astype('category')

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis, y_axis):
    fig = px.scatter(data_frame= data_df, x=x_axis, y=y_axis, color="income_class", height=600)
    fig.update_traces(marker={"size":15, "opacity": 0.85, "line":{"width": 2, "color": "black"}})
    fig.update_layout(paper_bgcolor="#e5ecf6", margin={"t":0})
    return fig

####################### WIDGETS #############################

x_axis = dcc.Dropdown(
    id="x_axis",
    options=[{"label": col, "value": col} for col in data_df.columns],
    value=data_df.columns[0],  # Default value set to the first column
    clearable=False
)

y_axis = dcc.Dropdown(
    id="y_axis",
    options=[{"label": col, "value": col} for col in data_df.columns],
    value=data_df.columns[1],  # Default value set to the second column
    clearable=False
)


####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Explore Relationship between Features", className="fw-bold text-center"),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    html.Br(),
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)