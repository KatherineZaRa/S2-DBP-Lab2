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

# Método GET/anime
@app.route('/anime',methods=['GET'])
def get_anime():
    return jsonify(animes)
# Método GET/anime/{id}

# Método POST/anime

# Método PUT/anime/{id}

# Método PATCH/anime/{id}

# Método DELETE/anime/{id}



if __name__ == '__main__':
    app.run()
