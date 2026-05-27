from apps.app import db


class Paciente(db.Model):
    __tablename__ = "pacientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)
    citas = db.relationship(
        "Cita", back_populates="paciente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Paciente {self.nombre} - Telefono: {self.telefono}>"
