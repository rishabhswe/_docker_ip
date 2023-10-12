from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, DOCKER is Working from inside AWS EC2 or AWS APP RUNNER!</p>"

pets = ["Pet1: dog", "Pet2: cat", "Pet3: donkey"]
@app.route("/pets")
def getPetResponse():
    return f"<h1>Pets</h1><ul>{''.join(list(map(getLi, pets)))}</ul>"
def getLi(pet):
    return f"<li>{pet}</li>"

@app.route("/pets/<int:pet_id>")
def getPetSpecific(pet_id):
    return f"<h1>Pet</h1><ul><li>{pets[pet_id - 1]}</li></ul>"
