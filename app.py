from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Base de regras simples em Python para classificar os sintomas
base_sintomas = {
    "graves": ["falta de ar", "peito", "desmaio", "sangramento", "sangue"],
    "moderados": ["febre", "corpo", "diarreia", "tontura", "vômito", "vomito"],
    "leves": ["cabeça", "enjoo", "enjoada", "tosse", "coriza", "cansaço"],
}


@app.route("/")
def index():
  return render_template("chatbot.html")  # Sua tela do chat


@app.route("/api/chat", methods=["POST"])
def processar_chat():
  # Recebe a mensagem enviada pelo JavaScript do navegador
  dados = request.get_json()
  mensagem_usuario = dados.get("mensagem", "").lower()

  classificacao_encontrada = ""

  # Verifica em qual categoria o sintoma se encaixa
  for categoria, sintomas in base_sintomas.items():
    if any(sintoma in mensagem_usuario for sintoma in sintomas):
      classificacao_encontrada = categoria
      break

  # Define a resposta com base na categoria
  if classificacao_encontrada == "graves":
    resposta = (
        "Entendi. Seu sintoma se configura na classificação:"
        " **Sintomas Graves / Urgentes**."
    )
  elif classificacao_encontrada == "moderados":
    resposta = (
        "Entendi. Seu sintoma se configura na classificação:"
        " **Sintomas Moderados**."
    )
  elif classificacao_encontrada == "leves":
    resposta = (
        "Entendi. Seu sintoma se configura na classificação: **Sintomas Leves**."
    )
  else:
    resposta = (
        "Não consegui identificar com clareza a gravidade desse sintoma."
        " Procure orientação profissional se necessário."
    )

  # Devolve a resposta em formato JSON para o front-end
  return jsonify({"resposta": resposta})


if __name__ == "__main__":
  app.run(debug=True)