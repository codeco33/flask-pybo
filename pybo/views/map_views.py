from flask import Blueprint, render_template

bp = Blueprint('map', __name__, url_prefix='/map')

@bp.route('/')
def _map():
    return render_template('map/map_form.html')

