
import flask
from flask import redirect
from Alumnos.routes import alumnos
from Maestros.routes import maestros
from BD.config import DevelopmentConfig
from Models.model import db

app = flask.Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return redirect('getalum')
    #return flask.jsonify({'Datos': 'Home'}) #mandar un json

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
