from flask import Flask, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Debug Toolbar
from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)


@app.route("/")
def homepage():
    """Home page"""

    pets = Pet.query.order_by(Pet.species).all()

    return render_template("index.html", pets=pets)


@app.route("/add", methods=['GET', 'POST'])
def add_form():
    """Form to add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/")

    else:
        return render_template("add.html", form=form)


@app.route("/<int:pet_id>", methods=['GET', 'POST'])
def pet_detail(pet_id):
    """Pet Detail Page"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect("/")
    else:
        return render_template("edit_pet.html", pet=pet, form=form)