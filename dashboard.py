from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("Cachorros.xlsx")

fig = px.bar(df, x="Raca Cachorro",y="Quantidade", color="ID Petshop",barmode="group")

opcoes = list(df['ID Petshop'].unique())
opcoes.append("Todos petshops")


app.layout = html.Div(children=[
    html.H1(children='Quantidade por Petshop'),
    html.H2(children="Grafico com a quantidade de cachorros de determinada raça em cada petshop"),
    dcc.Dropdown(opcoes, value="Todos petshops", id="lista_petshops"),

    dcc.Graph(
        id="grafico_quantidade_cachorro",
        figure=fig
    )
])

@app.callback(
    Output("grafico_quantidade_cachorro", "figure"),
    Input("lista_petshops", "value")
)

def update_output(value):
    if value == "Todos petshops":
        fig = px.bar(df, x="Raca Cachorro",y="Quantidade", color="Id Petshop",barmode="group")
    else:
        tabela_filtrada = dc.loc[df["ID Petshop"] == value , :]
        fig = px.bar(tabela_filtrada, x="Raca Cachorro",y="Quantidade", color="Id Petshop",barmode="group")
        
    return fig
        
if __name__ == "__main__":
    app.run(debug=True)
        