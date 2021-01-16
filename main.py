from flask import Flask
import requests
from werkzeug.utils import secure_filename
from goprocam import GoProCamera, constants

###################################################################
## Global

app = Flask(__name__)
APIKEY = ''
ROOT_PATH='/workspace'

ALLOWED_EXTENSIONS = {'mp4','jpg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

###################################################################
## Primary functions

@app.route('/newEvent/<opt>', methods=['GET'])
def transformEvent():

	return "200"



###################################################################
# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5001)