from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)

    return jsonify(cafe=random_cafe.to_dict())

    # return jsonify(cafe={"can_take_calls": "true" if random_cafe.can_take_calls else "false",
    #                     "coffee_price": random_cafe.coffee_price,
    #                     "has_sockets": "true" if random_cafe.can_take_calls else "false",
    #                     "has_toiles": "true" if random_cafe.has_toilet else "false",
    #                     "has_wifi": "true" if random_cafe.has_wifi else "false",
    #                     "id": random_cafe.id,
    #                     "img_url": random_cafe.img_url,
    #                     "location": random_cafe.location,
    #                     "map_url": random_cafe.map_url,
    #                     "name": random_cafe.name,
    #                     "seats": random_cafe.seats
    #                     })

@app.route('/all')
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])

@app.route('/search')
def get_find_cafe():
    found_cafe = db.session.query(Cafe).filter_by(location=request.args.get("loc")).first()
    if found_cafe:
        return jsonify(cafe=found_cafe.to_dict())
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe in that location"})

## HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def  post_add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"sucess": "Succesfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def patch_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.session.query(Cafe).get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"sucess": "Succesfully updated the price."})

    return jsonify(error={"Not Found": "Sorry, we don't have a cafe with that id"})

## HTTP DELETE - Delete Record
TopSecretAPIKey=''
@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api_key") == TopSecretAPIKey:
        cafe_to_be_deleted = db.session.query(Cafe).get(cafe_id)
        if cafe_to_be_deleted:
            db.session.delete(cafe_to_be_deleted)
            db.session.commit()
            return jsonify(response={"sucess": "Succesfully deleted the coffee shop."}),200

        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe with that id"}), 404

    else:
        return jsonify(error={"Not Found": "Sorry, you don't have authority"}), 403


if __name__ == '__main__':
    app.run(debug=True)
