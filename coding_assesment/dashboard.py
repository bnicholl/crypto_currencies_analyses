#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:05:18 2019

@author: bennicholl
"""
#plotly.tools.set_credentials_file(username='hockeyblades66', api_key='Ggxhe9Y4TSxmEOVKuiaR')
import dash
import dash_core_components as dcc
import dash_html_components as html
"""this function just wraps markdown text and makes it look prettier """
from textwrap import dedent as d
from dash.dependencies import Input, Output
import json

def build_dash_microservice(data):    
    app = dash.Dash()
    
    app.layout = html.Div([
            html.H1('CURRENCY PLOT'),
            dcc.Graph(id="basic-interactions", figure=data, config={"editable": True}, style={"height": "100vh", "width" : "100%"}),
            # this HTML Div creates the data div that gets lasso'd or rectangled
            html.Div(className='row', children=[
                html.Div([
                dcc.Markdown(d("""
                    **Selection Data**
    
                    Choose the lasso or rectangle tool in the graph's menu
                    bar and then select points in the graph.
    
                    Note that if `layout.clickmode = 'event+select'`, selection data also 
                    accumulates (or un-accumulates) selected data if you hold down the shift
                    button while clicking.
                """)),
                html.Pre(id='selected-data'),# style=styles['pre']),
            ], className='three columns')
        ])
    ])
                
            
            
    # basic-interactions is a component and selectedData is a property 
    # The input is the basic-interactions plot, and the selectedData is the pre made prop that holds the
    # selected data that was highlighted with the lasso. You can see selectedData prop in the redux store
    # the ouptut is where we put the input
    

    @app.callback(
        Output('selected-data', 'children'),
        [Input('basic-interactions', 'selectedData')])
    def display_selected_data(selectedData): 
        with open('calculations/data/selectedData', 'w') as f:  # writing JSON object
            json.dump(selectedData, f)
        
        #return json.dumps(selectedData, indent=2)
    



    app.run_server() 
    
