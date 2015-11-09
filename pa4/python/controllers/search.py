from flask import *
import requests
import json

from utils import *

search = Blueprint('search', __name__, template_folder='views')


@search.route(append_key('/search'), methods=['GET'])
def search_route():

    query = request.args.get('query')
    if query is None:
       query = ''
    result_obj = requests.get('http://eecs485-09.eecs.umich.edu:6288/search?q=%s' % (query))
    # result_obj = requests.get('http://localhost:4000/search?q=%s' % (query))
    result = json.loads(result_obj.text)
    photo_info = []
    con = mysql.connection
    result_list = result['hits']
    for obj in result_list:

        cur = con.cursor()
        cur.execute("SELECT url FROM Photo WHERE picid= %s " % (obj['id']))
        url = cur.fetchall()

        cur.execute("SELECT caption FROM Contain WHERE picid= %s " % (obj['id']))
        caption = cur.fetchall()

        info = {}
        info['url'] = url[0][0]
        info['caption'] = caption[0][0]
        photo_info.append(info)

    return render_template('search.html', query = query, photos = photo_info)
