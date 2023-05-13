from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required
from ..models import User, Pokemon, db, current_user


team = Blueprint('team', __name__, template_folder='team_templates')

@team.route('/team', methods=['GET', 'POST'])
@login_required
def get_team():     #Changed!
    # Get the current user's Pokemon
    user_pokemon = User.query.filter_by(username=current_user.username).first().pokemon

    if request.method == 'POST':
        # Get the user's team
        team = request.form.getlist('team')

        # Save the user's team to the database
        current_user.team = team
        db.session.commit()

        flash('Team saved!')
        return redirect(url_for('team'))

    # Render the team form template if the request is a GET
    return render_template('team_form.html', pokemon=user_pokemon, team=current_user.team)


@team.route('/team', methods=['POST'])
@login_required
def remove_from_team():
    # Get the name of the Pokemon to remove
    pokemon_name = request.form['pokemon_name']

    # Remove the Pokemon from the user's team
    current_user.team.remove(pokemon_name)
    db.session.commit()

    flash('Pokemon removed from team!')
    return redirect(url_for('team.html'))
