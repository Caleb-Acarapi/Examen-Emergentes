from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Debes iniciar sesión para acceder a esta página.'
login_manager.login_message_category = 'warning'


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "medicontrol-secret-key-2026"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///medicontrol.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        from apps.models import User
        return User.query.get(int(user_id))

    # 1. Importacion de los blueprints (cada modulo)
    from apps.core.routes import bp_core
    from apps.Medicos.routes import bp_medicos
    from apps.Pacientes.routes import bp_pacientes
    from apps.Citas.routes import bp_citas
    from apps.auth import auth_bp

    # 2. Registrar los blueprints (cada modulo)
    app.register_blueprint(bp_core)
    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app
