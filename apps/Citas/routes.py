from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required
from apps.app import db
from apps.Citas.models import Cita
from apps.Medicos.models import Medico
from apps.Pacientes.models import Paciente

bp_citas = Blueprint("bp_citas", __name__, template_folder="templates")


@bp_citas.route("/")
@login_required
def listar():
    citas = Cita.query.all()
    return render_template("citas/listar.html", citas=citas)


@bp_citas.route("/create", methods=["GET", "POST"])
@login_required
def crear():
    if request.method == "POST":
        from datetime import datetime
        fecha_str = request.form["fecha"]
        hora_str = request.form["hora"]
        
        # Convertir a objetos datetime
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        hora = datetime.strptime(hora_str, '%H:%M')
        
        medico_id = request.form["medico_id"]
        paciente_id = request.form["paciente_id"]
        nueva_cita = Cita(
            fecha=fecha, hora=hora, medico_id=medico_id, paciente_id=paciente_id
        )
        db.session.add(nueva_cita)
        db.session.commit()
        return redirect(url_for("bp_citas.listar"))
    
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template("citas/crear.html", medicos=medicos, pacientes=pacientes)


@bp_citas.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    cita = Cita.query.get(id)
    if request.method == "POST":
        from datetime import datetime
        cita.fecha = datetime.strptime(request.form["fecha"], '%Y-%m-%d')
        cita.hora = datetime.strptime(request.form["hora"], '%H:%M')
        cita.medico_id = request.form["medico_id"]
        cita.paciente_id = request.form["paciente_id"]
        db.session.commit()
        return redirect(url_for("bp_citas.listar"))
        
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template("citas/editar.html", cita=cita, medicos=medicos, pacientes=pacientes)


@bp_citas.route("/delete/<int:id>", methods=["POST"])
@login_required
def eliminar(id):
    cita = Cita.query.get(id)
    db.session.delete(cita)
    db.session.commit()
    return redirect(url_for("bp_citas.listar"))
