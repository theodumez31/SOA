
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<hostname>/<database>'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class EgaPro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Ajoutez ici les autres champs de la table EgaPro

class EgaProSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EgaPro
        load_instance = True

ega_pro_schema = EgaProSchema()
ega_pros_schema = EgaProSchema(many=True)

@app.route('/egapro', methods=['GET'])
def get_egapro():
    all_egapro = EgaPro.query.all()
    result = ega_pros_schema.dump(all_egapro)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
