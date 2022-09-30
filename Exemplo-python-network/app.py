import flask
from flask import request, json, jsonify 
import requests

app = flask.Flask(__name__) # inicia um Flask
app.config["DEBUG"] = True # ver no terminal as mensagens que ele roda

@app.route("/", methods=["GET"]) # rota da api e recepção de dados da api externa
def index(): # função para a rota, simplesmente recebe dados
  data = requests.get('https://randomuser.me/api') # faz um request para essa api que retorna informações de um user gerado aleatoriamente
  return data.json() # retorna o dado no formato .json

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port="5000") # roda no localhost na porta 5000, como descrita no Dockerfile
  