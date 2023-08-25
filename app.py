from flask import Flask,request,jsonify

app = Flask(__name__)

# Lista de animes

animes = [

    {
    "id": 1,
    "titulo": "Gintama: THE FINAL",
    "puntaje": 91,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Accion","Comedia","Drama"]
    },

    {
    "id": 2,
    "titulo": "Gintama°",
    "puntaje": 90,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Accion","Comedia","Drama"]
    },

    {
    "id": 3,
    "titulo": "Fruits Basket: The Final",
    "puntaje": 90,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Comedia","Drama","Romance"]
    },

    {
    "id": 4,
    "titulo": "Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST",
    "puntaje": 90,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Accion","Aventura","Drama","Fantasia"]
    },

    {
    "id": 5,
    "titulo": "Kaguya-sama wa Kokurasetai: Ultra Romantic",
    "puntaje": 90,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Comedia","Romance"]
    },

    {
    "id": 6,
    "titulo": "Shingeki no Kyojin 3 Part 2",
    "puntaje": 90,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Accion","Misterio","Drama"]
    },

    {
    "id": 7,
    "titulo": "3-gatsu no Lion 2",
    "puntaje": 89,
    "tipo" : "Serie",
    "season": "GT",
    "generos": ["Drama"]
    }

]

@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'

# Método GET/anime
@app.route('/anime',methods=['GET'])
def get_anime():
    return jsonify(animes)
# Método GET/anime/{id}
@app.route('/anime/<id>',methods=['GET'])
def get_id_anime(id):
    for ids in animes:
        if ids['id']==int(id):
            return jsonify(ids)
    return {}
# Método POST/anime
@app.route('/anime',methods=['POST'])
def post_anime():
    agregar = request.get_json()
    agregar['id'] = len(animes) + 1
    animes.append(agregar)
    return jsonify(agregar)
# Método PUT/anime/{id}
@app.route('/anime/<id>',methods=['PUT'])
def put_anime(id):
    numero = request.get_json()
    for i, u in enumerate(animes):
        if u['id']== numero['id']:
            animes[i]=numero
    return jsonify(numero)
# Método PATCH/anime/{id}
#@app.route('/anime/<id>',methods=['PATCH'])
#def patch_anime(id):
#    numero = request.get_json()
#    for i, u in enumerate(animes):
#        if u['id']== numero['id']:
#            animes[i]=numero
#    return jsonify(numero)
# Método DELETE/anime/{id}
@app.route('/anime/<id>',methods=['DELETE'])
def delete_anime(id):
    for ids in animes:
        if ids['id']==int(id):
            animes.remove(ids)
    return {}


if __name__ == '__main__':
    app.run()
