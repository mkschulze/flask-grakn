from flask import Blueprint
from flask import render_template


index_bp = Blueprint('main', __name__)


@index_bp.route('/')
def index():
    return render_template('home/index.html')
