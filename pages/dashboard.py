from dash import html, dcc
import dash_bootstrap_components as dbc

def dashboard_page(fnd):
    main_div = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5(["Total News"]),
                    html.H5([fnd.getDataShape()[0]],style={"font-size": "20px"})
                ], style={"width":"100%","height":"140px","background-color":"rgb(192 59 59)","border-radius":"10px","padding": "25px 30px"})
            ]),
            dbc.Col([
                html.Div([
                    html.H5(["Total Authors"]),
                    html.H5([fnd.getUniqueAuthors()],style={"font-size": "20px"})
                ], style={"width":"100%","height":"140px","background-color":"rgb(80 180 60)","border-radius":"10px","padding": "25px 30px"})
            ]),
            dbc.Col([
                html.Div([
                    html.H5(["Total Fake News"]),
                    html.H5([10200],style={"font-size": "20px"})
                ], style={"width":"100%","height":"140px","background-color":"rgb(54 161 176)","border-radius":"10px","padding": "25px 30px"})
            ]),
            dbc.Col([
                html.Div([
                    html.H5(["Total Real News"]),
                    html.H5([10500],style={"font-size": "20px"})
                ], style={"width":"100%","height":"140px","background-color":"rgb(136 99 212)","border-radius":"10px","padding": "25px 30px"})
            ]),
        ]),
        dbc.Row([
            dbc.Col(md=4,children=[
                html.Div([
                    dbc.Row([
                        dbc.Col([html.H5(["Fake Vs Real News"])])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(figure=fnd.getFakeVsRealCount())
                        ])
                    ])
                ],className="mt-5", style={"background":"#111111","border-radius":"10px","padding": "25px 30px"})
            ]),
            dbc.Col(md=8,children=[
                html.Div([
                    dbc.Row([
                        dbc.Col([html.H5(["Top Authors"])])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(figure=fnd.getTopTenAuthors())
                        ])
                    ])
                ],className="mt-5", style={"background":"#111111","border-radius":"10px","padding": "25px 30px"})
            ])
        ]),
        dbc.Row([
            dbc.Col(md=6,children=[
                html.Div([
                    dbc.Row([
                        dbc.Col([html.H5(["Top Real News Authors"])])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(figure=fnd.getTopTenRealAuthors())
                        ])
                    ])
                ],className="mt-5", style={"background":"#111111","border-radius":"10px","padding": "25px 30px"})
            ]),
            dbc.Col(md=6,children=[
                html.Div([
                    dbc.Row([
                        dbc.Col([html.H5(["Top Fake News Authors"])])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(figure=fnd.getTopTenFakeAuthors())
                        ])
                    ])
                ],className="mt-5", style={"background":"#111111","border-radius":"10px","padding": "25px 30px"})
            ])
        ])
    ])

    return main_div