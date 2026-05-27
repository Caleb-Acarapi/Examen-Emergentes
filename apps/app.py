from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///medicontrol.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # 1. Importacion de los blueprints(cada modulo)
    from apps.core.routes import bp_core
    from apps.Medicos.routes import bp_medicos
    from apps.Pacientes.routes import bp_pacientes
    from apps.Citas.routes import bp_citas

    # 2. Registrar los blueprints(cada modulo)
    app.register_blueprint(bp_core)
    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")

    return app
