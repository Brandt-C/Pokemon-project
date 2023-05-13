from flask import Blueprint, render_template, request
from ..models import User, db
from ..services import search_pokemon #moved this to make the import cleaner and a little more broad

catch = Blueprint('catch', __name__, template_folder='catch_templates')


@catch.route('/catch', methods=['POST'])
def catch_pokemon(username, pokemon_name):
    pokemon_name = request.form.get('pokemon_name')
    # Check if the user already has the Pokemon in their account
    user = User.query.filter_by(username=username).first()
    if user and pokemon_name in user.pokemon:
        return False  # Pokemon is already in the user's account
    # Get the Pokemon's details from the API
    pokemon = search_pokemon(pokemon_name)
    # Create a new CaughtPokemon instance for the user
    caught_pokemon = CaughtPokemon(name=pokemon_name, sprite_url=pokemon['sprites']['front_default'])
    # Add the new caught Pokemon to the user's account
    if user:
        user.pokemon.append(caught_pokemon)
    else:
        user = User(username=username, pokemon=[caught_pokemon])
        db.session.add(user)

    db.session.commit()
    return True 

@catch.route('/release', methods=['POST'])
def release_pokemon(username, pokemon_name):
    pokemon_name = request.form.get('pokemon_name')
    User = User.query.filter_by(username=username).first()
    if not User or pokemon_name not in User.pokemon:
        return False  
    caught_pokemon = next((p for p in User.pokemon if p.name == pokemon_name), None)
    if not caught_pokemon:
        return False  
    User.pokemon.remove(caught_pokemon)

    db.session.commit()
    return True  


