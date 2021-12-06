from datetime import datetime
from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


app = Flask(__name__,
            static_folder = "./fronted/dist/static",
            template_folder = "./fronted/dist")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/roll'
app.config['SQLALCHEMY_TRACK_MODIFICATIONSI'] = False

CORS(app)

db = SQLAlchemy(app)
ma=Marshmallow(app)
class Articles(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    correo = db.Column(db.String(100))
    edad = db.Column(db.String(20))
    sexo = db.Column(db.String(100))
    redsocialfav = db.Column(db.String(100))
    tfacebook = db.Column(db.Integer)
    twhatsapp = db.Column(db.Integer)
    ttwitter = db.Column(db.Integer)
    tinstagram = db.Column(db.Integer)
    ttiktok = db.Column(db.Integer)
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    
    def __init__(self,correo,edad,sexo,redsocialfav,tfacebook,twhatsapp,ttwitter,tinstagram,ttiktok):
        self.correo = correo
        self.edad = edad
        self.sexo = sexo
        self.redsocialfav = redsocialfav
        self.tfacebook= tfacebook
        self.twhatsapp=	twhatsapp
        self.ttwitter= ttwitter
        self.tinstagram= tinstagram
        self.ttiktok= ttiktok

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id','correo','edad','sexo','redsocialfav','tfacebook','twhatsapp','ttwitter','tinstagram','ttiktok','date')
article_schema=ArticleSchema() 
articles_schema=ArticleSchema(many=True)

@app.route('/get', methods = ['GET'])
def get_articles():
    all_articles= Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)

@app.route('/get/<id>/', methods = ['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)

    

@app.route('/add', methods = ['POST'])
def add_article():
    correo = request.json['correo']
    edad = request.json['edad']
    sexo = request.json['sexo']
    redsocialfav = request.json['redsocialfav']
    tfacebook = request.json['tfacebook']
    twhatsapp = request.json['twhatsapp']
    ttwitter = request.json['ttwitter']
    tinstagram = request.json['tinstagram']
    ttiktok = request.json['ttiktok']
    articles = Articles(correo,edad,sexo,redsocialfav,tfacebook,twhatsapp,ttwitter,tinstagram,ttiktok)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def dender_vue(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)