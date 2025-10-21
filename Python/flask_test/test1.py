from flask import Flask 

app = Flask(__name__)

@app.route("/")

def home():
    return "Bonjour mon  Lieutenant colonel"

if __name__=="__main__":
    app.run(debug=True )

# Le blueprint, ce sont des modules flask qui permet de gerer les routes et la logique de l'application. Il sert à rendre le projet plus lisible et scalable