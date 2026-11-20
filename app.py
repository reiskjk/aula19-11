
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


def calcular_dias_restantes(data_atual):
    dias_faltantes = (date(data_atual.year, 12, 31) - data_atual).days
    return dias_faltantes

@app.route("/")
def pagina_inicial():
    data_corrente = date.today()

    dias_restantes = calcular_dias_restantes(data_corrente)

    return render_template(
        "index.html",
        dias_restantes=dias_restantes,
        ano_novo=data_corrente.year + 1,
        data_atual=data_corrente.strftime("%d/%m/%Y")
    )

if __name__ == "__main__":
    app.run(debug=True)

