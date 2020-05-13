import json
import sys

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.sql.expression import text
from sqlalchemy import insert
from config import Config
import pars

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class JsonModel(object):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Post(db.Model, JsonModel):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    domain = db.Column(db.Integer, index=True)
    text = db.Column(db.String(500))
    likes = db.Column(db.Integer)

    def __init__(self, aid, date, domain, text, likes):
        self.id = aid
        self.date = date
        self.domain = domain
        self.text = text
        self.likes = likes


def filter_posts():
    posts = pars.take_posts('jumoreski')
    posts.extend(pars.take_posts('baneksbest'))
    filtered_posts = []
    for post in posts:
        if not post['marked_as_ads'] and 'attachments' not in post and post['likes']['count'] > 1000:
            data = Post(post['id'],
                        post['date'],
                        post['from_id'],
                        post['text'],
                        post['likes']['count'])
            filtered_posts.append(data)
    return filtered_posts


# fp = filter_posts()
db.create_all()
# db.session.query(Post).delete()
# db.session.commit()
# for p in fp:
#     db.session.add(p)
# db.session.commit()


@app.route("/", methods=['GET'])
def index():
    return json.dumps([p.as_dict() for p in db.session.query(Post).all()])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
