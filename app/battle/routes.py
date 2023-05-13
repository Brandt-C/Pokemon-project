from flask import Blueprint, request, render_template
from ..models import User #fixed routing here
from flask_login import login_required
from ..services import search_pokemon #moved this to make the import cleaner and a little more broad


battle = Blueprint('battle', __name__, template_folder='battle_templates')


import random

@battle.route('/battle', methods=['GET', 'POST'])
@login_required
def poke_battle(): #Changed!
    if request.method == 'POST':
        # Get the usernames of the two users who are battling
        user1_username = request.form['user1_username']
        user2_username = request.form['user2_username']

        # Get the Pokemon for each user
        user1_pokemon = User.query.filter_by(username=user1_username).first().pokemon
        user2_pokemon = User.query.filter_by(username=user2_username).first().pokemon

        # Randomly select a Pokemon for each user
        user1_pokemon_name = random.choice(user1_pokemon).name
        user2_pokemon_name = random.choice(user2_pokemon).name

        # Get the Pokemon details from the API
        user1_pokemon_details = search_pokemon(user1_pokemon_name)
        user2_pokemon_details = search_pokemon(user2_pokemon_name)

        # Randomly select a winner
        winner = random.choice([user1_username, user2_username])

        # Render the battle results template
        return render_template('battle_results.html', user1_username=user1_username, user1_pokemon=user1_pokemon_details,
                               user2_username=user2_username, user2_pokemon=user2_pokemon_details, winner=winner)

    # Render the battle form template if the request is a GET
    return render_template('battle_form.html')
