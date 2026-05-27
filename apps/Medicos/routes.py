from flask import Blueprint, render_template, request, url_for, redirect
from apps.app import db
from apps.Medicos.models import Medico

bp_medicos = Blueprint("bp_medicos", __name__, template_folder="templates")


@bp_medicos.route("/")
def listar():
    medicos = Medico.query.all()
    return render_template("medicos/listar.html", medicos=medicos)


@bp_medicos.route("/create", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        especialidad = request.form["especialidad"]
        nuevo_medico = Medico(nombre=nombre, especialidad=especialidad)
        db.session.add(nuevo_medico)
        db.session.commit()
        return redirect(url_for("bp_medicos.listar"))
    return render_template("medicos/crear.html")


@bp_medicos.route("/edit/<int:id>", methods=["GET", "POST"])
def editar(id):
    medico = Medico.query.get(id)
    if request.method == "POST":
        medico.nombre = request.form["nombre"]
        medico.especialidad = request.form["especialidad"]
        db.session.commit()
        return redirect(url_for("bp_medicos.listar"))
    return render_template("medicos/editar.html", medico=medico)


@bp_medicos.route("/delete/<int:id>", methods=["POST"])
def eliminar(id):
    medico = Medico.query.get(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for("bp_medicos.listar"))
