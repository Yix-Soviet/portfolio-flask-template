from flask import Flask
from flask_cors import CORS

# APP Blueprints
from projects import create_resources as create_projects_res
from messages import create_resources as create_messages_res
from portfolio import create_resources as create_portfolio_res


# Database
from databases.conf_db import db
from databases.extensions.init_ext import ma_serializer, migrate

app = Flask(__name__)

# Flask Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app=app)

# Database
db.init_app(app)
ma_serializer.init_app(app)
migrate.init_app(app, db)



# Blueprints
app.register_blueprint(create_projects_res())
app.register_blueprint(create_messages_res())
app.register_blueprint(create_portfolio_res(subdomain=True), subdomain="portfolio")
app.register_blueprint(create_portfolio_res(subdomain=False))

if __name__ == '__main__':
    website_url = 'yixsoviet.gfg:5000'
    app.config['SERVER_NAME'] = website_url
    # app.run(host="127.0.0.1", port=8000, debug=True)
    app.run(debug=True)