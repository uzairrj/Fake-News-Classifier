from dash import Dash, html, dcc,Output,Input, State
import dash_bootstrap_components as dbc
from NLP import pipeline, models
from data import load_data
from pages import dashboard, detect

app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
app.config.suppress_callback_exceptions = True
#fake news class
fake_news_data = load_data.fake_news_data("./data/fake_train.csv")
fake_news_models = models.fake_news_models("./models/models.bin")
fake_news_pipeline = pipeline.fake_news_pipeline(models=fake_news_models)

dashboard_page = dashboard.dashboard_page(fake_news_data)

detect_page = detect.detect_page(app, fake_news_pipeline)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#370665",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Fake News Detector", className="display-6"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Detect", href="/detect", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)



app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dashboard_page
    elif pathname == "/detect":
        return detect_page
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
    dbc.Container(
        [
            html.H1("404 Not Found", className="display-3"),
            html.P(
                "You are trying to visit the page that is not found in the server.",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Please check you address, or contact admin for the issue."
            )
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


if __name__ == '__main__':
    app.run_server(debug=True)