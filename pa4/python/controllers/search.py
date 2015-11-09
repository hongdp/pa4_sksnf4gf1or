from flask import *

from utils import *

search = Blueprint('search', __name__, template_folder='views')


@search.route(append_key('/search'), methods=['GET'])
def search_route():
