import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px


dash.register_page(__name__, path='/heatmap', name="Correlation 📊", order=5)

####################### DATASET #############################
file_path = r'C:\Users\Mahsa\EDA_dashplotly\sampled_dataset.csv'
data_df = pd.read_csv(file_path)

####################### BAR CHART #############################
def create_heatmap():
    char_corr = data_df.corr(numeric_only=True)
    fig =  px.imshow(char_corr, height=600, color_continuous_scale="RdBu")
    fig = fig.update_layout(paper_bgcolor="#e5ecf6", margin={"t":0})
    return fig

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Features Correlation Heatmap", className="fw-bold text-center"),
    dcc.Graph(id="heatmap", figure=create_heatmap())
])