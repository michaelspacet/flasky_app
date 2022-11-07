from dash import html
from dash_apps.ngp.tabs.internal_data import *
from dash_apps.ngp.tabs.companies_house import *

layout = html.Div([
    html.H1('NGP'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Internal Data', value='tab-1-example'),
        dcc.Tab(label='Companies House', value='tab-2-example'),
    ]),
    html.Div(id='tabs-content-example')
])
