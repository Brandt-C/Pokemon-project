from flask_login import current_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    pokemon = db.relationship('Pokemon', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def saveUser(self):
        db.session.add(self)
        db.session.commit()

    def is_active(self):
        return True
    
    

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    ability = db.Column(db.String(50))
    body = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, pokemon_name, hp, defense, attack, img_url, ability, body, user_id):
        self.pokemon_name = pokemon_name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.img_url = img_url
        self.ability = ability
        self.body = body
        self.user_id = user_id


    def saveToTeam(self, user):
        self.team.append(user)
        db.session.commit()

    def deleteFromTeam(self, user, product):
        self.teamed.remove(user, product)
        db.session.commit()
        
    def saveChanges(self):
        db.session.commit()

    def savePokemon(self):
        db.session.add(self)
        db.session.commit()

    def deletePokemon(self):
        db.session.delete(self)
        db.session.commit()
    
  
    def to_dict(self):
        return {
            'id' : self.id,
            'pokemon_name' : self.pokemon_name,
            'hp' : self.hp,
            'defense' : self.defense,
            'attack' : self.attack,
            'img_url' : self.img_url, 
            'ability' : self.ability,
            'body' : self.body       

        }
    

