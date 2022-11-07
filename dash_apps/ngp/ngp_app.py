from dash.dependencies import Input, Output
import dash
import dash_html_components as html
import dash_core_components as dcc
from flask_login.utils import login_required

from dash_apps.ngp.layout import layout
from dash_apps.ngp.callbacks import get_callbacks


def create_ngp_app(flask_app):

    ngp_app = dash.Dash(server=flask_app,
                        name="NGP",
                        url_base_pathname="/NGP/")
    ngp_app.layout = layout
    get_callbacks(ngp_app)

    for view_function in ngp_app.server.view_functions:
        if view_function.startswith(ngp_app.config.url_base_pathname):
            ngp_app.server.view_functions[view_function] = login_required(
                ngp_app.server.view_functions[view_function]
            )

    return ngp_app
