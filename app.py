import base64
import io
import uuid
import os
from textwrap import wrap

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_samples

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', "https://codepen.io/chriddyp/pen/brPBPO.css"]  # dash and loading spinner css

# mck_palette = ['#034B6F', '#027AB1', '#39BDF3', '#71D2F1', '#AFC3FF', '#3C96B4', '#AAE6F0',
#                '#8C5AC8', '#E6A0C8', '#E5546C', '#FAA082']
mck_palette = ['#034B6F', '#8C5AC8', '#E6A0C8', '#E5546C', '#FAA082', '#AFC3FF', '#027AB1', '#39BDF3', '#71D2F1', '#3C96B4', '#AAE6F0']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, url_base_pathname=os.getenv('BASE_URL', '')+'/')
server = app.server

def serve_layout():
    session_id = str(uuid.uuid4())
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Input(id='my-id', value='initial value', type='text'),
        html.Div(id='my-div')
    ])


app.layout = serve_layout

@app.callback(
    Output('my-div', 'children'),
    [Input('my-id', 'value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"!!!'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True, port=8080, host='0.0.0.0')

