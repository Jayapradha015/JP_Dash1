from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
df.columns

df2 = df.groupby(["State", "Make"], as_index=False)["Model Year"].value_counts()

app.layout = html.Div([
    html.H1("Electric Vehicle Population", style={"text-align": "center"}),
    dcc.Dropdown(id="input1", options=[
        {"label": "MERCEDES-BENZ", "value": "MERCEDES-BENZ"},
        {"label": 'TESLA', "value": 'TESLA'},
        {"label": 'FORD', "value": 'FORD'},
        {"label": 'NISSAN', "value": 'NISSAN'},
        {"label": 'AUDI', "value": 'AUDI'},
        {"label": 'KIA', "value": 'KIA'},
        {"label": 'CHEVROLET', "value": 'CHEVROLET'},
        {"label": 'VOLKSWAGEN', "value": 'VOLKSWAGEN'},
        {"label": 'HONDA', "value": 'HONDA'},
        {"label": 'TOYOTA', "value": 'TOYOTA'},
        {"label": 'BMW', "value": 'BMW'},
        {"label": 'JEEP', "value": 'JEEP'},
        {"label": 'VOLVO', "value": 'VOLVO'},
        {"label": 'POLESTAR', "value": 'POLESTAR'},
        {"label": 'PORSCHE', "value": 'PORSCHE'},
        {"label": 'LAND ROVER', "value": 'LAND ROVER'},
        {"label": 'JAGUAR', "value": 'JAGUAR'}],
                 multi=False,
                 value='TOYOTA',
                 style={"width": "40%"}),

    html.Div(id="output1"),
    html.Br(),

    dcc.Graph(id='output2')

])


@app.callback(
    [Output(component_id='output1', component_property='children'),
     Output(component_id='output2', component_property='figure')],
    [Input(component_id='input1', component_property='value')]
)
def update_graph(option_slctd):
    container = f"The Make selected is {option_slctd}"
    dff = df2.copy()
    dff = dff[dff["Make"] == option_slctd]

    fig = px.choropleth(
        data_frame=dff,
        locationmode="USA-states",
        locations="State",
        scope="usa",
        color='Model Year',
        hover_data=["State", "Make", 'count'],
        color_continuous_scale="Viridis",
        labels={"Population of electric Vehicle Tesla"},
        template="plotly_dark"
    )
    return container, fig


if __name__ == '__main__':
    app.run_server()