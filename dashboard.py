import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import joblib

app = dash.Dash(__name__)
model = joblib.load('desert_model.pkl')

app.layout = html.Div()

@app.callback(
    [Output('output-div', 'children'), Output('importance-chart', 'figure')],
    [Input('btn', 'n_clicks')],
   
)
def update_view(n_clicks, value):
    if n_clicks is None: return "", {}
    # Visualizing the causal ranking from the model
    fig = px.bar(x=, 
                 y=model.feature_importances_)
    return f"Vulnerability Analysis for {value} is active.", fig

if __name__ == '__main__':
    app.run_server(debug=True)