from dash import Input, Output

# from data_processing import *
from dash_apps.ngp.tabs import internal_data
from dash_apps.ngp.tabs import companies_house


def get_callbacks(app):
    #
    # @app.callback(
    #     Output('main_table', 'data')
    #     [Input('', ''),
    #      Input('', '')]
    # )
    # def update_table(input1,
    #                  input2):
    #     if input1:
    #         df = df[df['column'].isin(input1)]
    #     if input2:
    #         pass
    #
    #     return df.to_dict('records')

    @app.callback(Output('tabs-content-example', 'children'),
                  [Input('tabs-example', 'value')])
    def render_content(tab):
        if tab == 'tab-1-example':
            return internal_data.tab_1_layout
        elif tab == 'tab-2-example':
            return companies_house.tab_2_layout

    # Tab 1 callback
    @app.callback(Output('page-1-content', 'children'),
                  [Input('page-1-dropdown', 'value')])
    def page_1_dropdown(value):
        return 'You have selected "{}"'.format(value)

    # Tab 2 callback
    @app.callback(Output('page-2-content', 'children'),
                  [Input('page-2-radios', 'value')])
    def page_2_radios(value):
        return 'You have selected "{}"'.format(value)
