import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Distribution 📊", order=2)

####################### LOAD DATASET #############################
file_path = r'C:\Users\Mahsa\EDA_dashplotly\sampled_dataset.csv'
data_df = pd.read_csv(file_path)

####################### HISTOGRAM ###############################
def create_distribution(col_name):
    fig = px.histogram(data_frame=data_df, x=col_name, height=600, nbins=50)
    fig.update_traces(marker={"line":{"width": 2, "color": "black"}})
    fig.update_layout(paper_bgcolor="#e5ecf6", margin={"t":0},)
    return fig

####################### WIDGETS ################################
dd = dcc.Dropdown(id="dist_column", options=[{"label": col, "value": col} for col in data_df.columns],
     value=data_df.columns[0],  # Default value set to the first column
     clearable=False
)
####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Explore Distribution of Feature Values", className="fw-bold text-center"),
    dd,
    html.Br(),
    dcc.Graph(id="histogram")
])

####################### CALLBACKS ################################
@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)