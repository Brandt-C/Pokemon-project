from app import app

from flask import render_template, request, url_for, redirect, flash
from app.forms import PokemonLookUpForm
from .models import User, Pokemon, db, current_user
from .api import get_pokemon

@app.route('/')
def homePage():
    greeting = 'Welcome to Battle Pokemon. Get ready to catch and battle!'
    return render_template('home.html', g = greeting)

