import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['Account 1',
                                                    'Account 2',
                                                    'Account 3']],
        value='Account 1'
    ),
    html.Div(id='page-1-content')
])
