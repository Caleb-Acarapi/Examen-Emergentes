from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required
from apps.app import db
from apps.Pacientes.models import Paciente

bp_pacientes = Blueprint("bp_pacientes", __name__, template_folder="templates")


@bp_pacientes.route("/")
@login_required
def listar():
    pacientes = Paciente.query.all()
    return render_template("pacientes/listar.html", pacientes=pacientes)


@bp_pacientes.route("/create", methods=["GET", "POST"])
@login_required
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        nuevo_paciente = Paciente(nombre=nombre, telefono=telefono)
        db.session.add(nuevo_paciente)
        db.session.commit()
        return redirect(url_for("bp_pacientes.listar"))
    return render_template("pacientes/crear.html")


@bp_pacientes.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    paciente = Paciente.query.get(id)
    if request.method == "POST":
        paciente.nombre = request.form["nombre"]
        paciente.telefono = request.form["telefono"]
        db.session.commit()
        return redirect(url_for("bp_pacientes.listar"))
    return render_template("pacientes/editar.html", paciente=paciente)


@bp_pacientes.route("/delete/<int:id>", methods=["POST"])
@login_required
def eliminar(id):
    paciente = Paciente.query.get(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for("bp_pacientes.listar"))
