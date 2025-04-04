from flask import Flask
from .db import db, migrate
from .models import customer, rental, video
from .routes.customer_routes import customers_bp
from .routes.rental_routes import rentals_bp
from .routes.video_routes import videos_bp
import os

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(customers_bp)
    app.register_blueprint(rentals_bp)
    app.register_blueprint(videos_bp)

    return app