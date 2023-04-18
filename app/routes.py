from app import app

from flask import render_template, request, url_for, redirect, flash
from app.forms import PokemonLookUpForm
from .models import User, Pokemon, db, current_user
from .api import get_pokemon

@app.route('/')
def homePage():
    greeting = 'Welcome to Battle Pokemon. Get ready to catch and battle!'
    return render_template('home.html', g = greeting)



@app.route('/catch', methods=['GET', 'POST'])
def catchPage():
    form = PokemonLookUpForm(request.form)
    if form.validate_on_submit():
        pokemon_name = form.name.data.lower()
        user_id = current_user.id
        user = User.query.filter_by(id=user_id).first()
        if not user:
            pokemon = Pokemon.query.filter_by(name=pokemon_name, user_id=user_id).first()
        if not pokemon:
            # pokemon does not exist in database, fetch from pokeapi
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = request.get(pokemon_url)
            if response.status_code != 200:
                flash(f"Error: Could not find Pokemon with name {pokemon_name}")
            else:
                pokemon_data = response.json()
                # extract data from pokemon_data and create new Pokemon object
                # ...
                # save new Pokemon object to database
                # ...
        else:
            flash(f"You already have a {pokemon_name} in your collection")
            
    return render_template('catch.html', form=form)




@app.route('/release/<int:pokemon_id>', methods=['POST'])
def release_pokemon(pokemon_id):
    pokemon = Pokemon.query.filter_by(id=pokemon_id, user_id=current_user.id).first()
    if not pokemon:
        db.session.delete(pokemon)
        db.session.commit()
    return redirect(url_for('teamPage'))





@app.route('/team')
def teamPage():
    pass
    # return render_template('index.html', pokemon=pokemon)




