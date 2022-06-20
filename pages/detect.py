from re import template
from dash import html, dcc, Input,Output, State
import dash_bootstrap_components as dbc
from matplotlib.pyplot import figure
import plotly.express as plot

def detect_page(dash_app, fnd):
    main_div = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H5(["Detect Fake News"], className="text-center")
            ])
        ]),
        html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Select(id="models_options",
                    options=[
                        {"label":"Logistic Regression", "value":"lr"},
                        {"label":"Random Forest", "value":"rf"},
                        {"label":"Support Vector Machine", "value":"svm"},
                        {"label":"Voting Classifier", "value":"vc"},
                        {"label":"Stacking Classifier", "value":"sc", "selected":True},
                    ]
                    )
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Progress(label="Model Accuracy: 93.6%", color="success", value=93.6)
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Textarea(placeholder="Write news here...", rows=14,id="news_text", style={"resize":"none","background-color":"#1e1e1e","color":"#ebebeb"})
                ], className="mt-3")
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Button(["Check News"], id="check_news")
                ],className="mt-3 d-flex justify-content-center")
            ]),
        ], style={"background":"#111111","border-radius":"10px","padding": "25px 30px"}),
        html.Div([
            dbc.Row([
                dbc.Col([
                ],id="alert_container")
            ]),
            dbc.Row([
                dbc.Col([
                    
                ], className="mt-3")
            ])
        ], style={"background":"#111111","border-radius":"10px","padding": "25px 30px"}, className="mt-3")
     ])
    
    @dash_app.callback(
        Output("alert_container","children"),
        Input("check_news","n_clicks"),
        State("news_text","value"),
        State("models_options","value"),
        prevent_initial_call=True
        )
    def predict_news(n_clicks,value,select_value):
        if n_clicks > 0 and value != None and value != "":
            pred = fnd.predict(value, select_value)
            class_label_probs = pred["prob"][0]
            #class_label_probs = [(class_label*100),((1-class_label)*100)]
            fig = plot.pie(names=["Real","Fake"], values=class_label_probs, hole=.5, 
            template="plotly_dark",color=["Real","Fake"],color_discrete_map={"Fake":"#de3737","Real":"#37de4b"})
            if pred["class"] == 1:
                return dbc.Row([
                    dbc.Col([
                        dbc.Alert("The news is real.", color="success"),
                        html.H5(["Prediction Confidence "]),
                        dcc.Graph(figure=fig)
                    ])
                ])
            else:
                return dbc.Row([
                    dbc.Col([
                        dbc.Alert("The news is fake.", color="danger"),
                        html.H5(["Prediction Confidence "]),
                        dcc.Graph(figure=fig)
                    ])
                ])
    return main_div