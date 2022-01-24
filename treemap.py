import pandas as pd
import plotly.express as px

data = pd.read_excel("./Puzzle_data.xlsx")

data_filtro = data[data["Status"] == "Montado"]

fig = px.treemap(data_filtro, path=["País", "Fabricante"], values="Peças", color="País")
fig.update_layout(
    title="Report Puzzle Montados x Qtde Peças",
    title_x=0.5,
    title_y=0.95,
    width=1200,
    height=800,
    title_font_size=24,
)
fig.data[0].textinfo = "label, text, value"
fig.update_layout(uniformtext=dict(minsize=12, mode="hide"))
fig.show()
