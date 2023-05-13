from flask import Blueprint, render_template, json, request
from app.forms import PokemonLookUpForm
from ..models import Pokemon, db
import requests
from ..api import get_pokemon
from ..services import search_pokemon #moved this to make the import cleaner and a little more broad

search = Blueprint('search', __name__, url_prefix='/search')


#took out some misplaced noise in here. . . 




@search.route('/')  #app.route is for the general routes.py file in the app folder so this address is now /search
def search_poke():      #Changed!
    name = request.args.get('name')
    pokemon = search_pokemon(name)
    return render_template('search.html', pokemon=pokemon)



@search.route('/catch', methods=['GET', 'POST'])
def api_search_pokemon():
    form = PokemonLookUpForm()
    if form.validate_on_submit():
        pokemon_name = form.pokemon_name.data
        pokemon = Pokemon.query.filter_by(name=pokemon_name).first()
        if pokemon is None:
            # Fetch the Pokemon's information from the PokeAPI
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
            response = requests.get(url)
            if response.ok == 200:
                pokemon_data = json.loads(response.content)
                hp = pokemon_data['stats'][0]['base_stat']
                defense = pokemon_data['stats'][3]['base_stat']
                attack = pokemon_data['stats'][4]['base_stat']
                image_url = pokemon_data['sprites']['front_shiny']
                ability = pokemon_data['abilities'][0]['ability']['name']
                pokemon = Pokemon(name=pokemon_name, hp=hp, defense=defense, attack=attack, image_url=image_url, ability=ability)
                db.session.add(pokemon)
                db.session.commit()
            else:
                return 'Pokemon not found!'
        return render_template('search.html', pokemon=pokemon, form=form)
    else:
        return render_template('teams.html', form=form)




