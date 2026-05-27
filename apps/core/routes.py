from flask import Blueprint, render_template
from apps.Medicos.models import Medico
from apps.Pacientes.models import Paciente
from apps.Citas.models import Cita

bp_core = Blueprint("bp_core", __name__, template_folder="templates")


@bp_core.route("/")
def index():
    medicos_count = Medico.query.count()
    pacientes_count = Paciente.query.count()
    citas_count = Cita.query.count()
    
    # Obtener las últimas 3 citas para la ilustración/dashboard
    proximas_citas = Cita.query.order_by(Cita.fecha.desc(), Cita.hora.desc()).limit(3).all()
    
    return render_template(
        "core/index.html", 
        medicos_count=medicos_count, 
        pacientes_count=pacientes_count, 
        citas_count=citas_count,
        proximas_citas=proximas_citas
    )
