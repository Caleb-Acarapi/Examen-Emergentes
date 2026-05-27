from apps.app import db


class Medico(db.Model):
    __tablename__ = "medicos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    citas = db.relationship(
        "Cita", back_populates="medico", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Medico {self.nombre} - {self.especialidad}>"
