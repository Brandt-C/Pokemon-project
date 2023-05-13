from flask import Flask 

from config import Config


from .auth.routes import auth
from .team.routes import team
from .search.routes import search
from .catch.routes import catch
from .battle.routes import battle


from .models import db, User
from flask_login import LoginManager
from flask_migrate import Migrate




app = Flask(__name__)

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view='auth.loginPage'

app.register_blueprint(auth)
app.register_blueprint(team) #team, search, and battle are all currently named functions which is preventing their registration as blueprints
# Careful with naming conventions- best practice is to be specific even if it means you need to type more!
# I'm going to go to the routes and re-name to fix i.e.: the route was def team(): and now is get_team():
app.register_blueprint(search)
app.register_blueprint(catch)
app.register_blueprint(battle)

from . import routes
