import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/avg-feature', name=" Average Feature 📊", order=4)

####################### DATASET #############################
file_path = r'C:\Users\Mahsa\EDA_dashplotly\sampled_dataset.csv'
data_df = pd.read_csv(file_path)

####################### BAR CHART #############################
def create_bar_chart(col_name):
    fig =  px.histogram(data_frame=data_df, y=col_name, x="income_class", color="income_class",
                        histfunc="avg", height=600)
    fig.update_traces(marker={"line":{"width": 2, "color": "black"}})
    fig = fig.update_layout(bargap=0.7, paper_bgcolor="#e5ecf6", margin={"t":0})
    return fig

####################### WIDGETS ################################
dd = dcc.Dropdown(id="sel_col", options=[{"label": col, "value": col} for col in data_df.columns],
     value=data_df.columns[0],  # Default value set to the first column
     clearable=False
)
####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Explore Avr Feature Values per Income-class Type", className="fw-bold text-center"),
    dd, 
    html.Br(),
    dcc.Graph(id="bar_chart")
])

####################### CALLBACKS ################################
@callback(Output("bar_chart", "figure"), [Input("sel_col", "value"), ])
def update_bar_chart(sel_col):
    return create_bar_chart(sel_col)