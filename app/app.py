import os

from flask import Flask, render_template, request, jsonify,redirect,url_for,send_from_directory
from werkzeug import secure_filename
import cv2
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher

# create flask instance

app = Flask(__name__, static_url_path = "", static_folder = "static")
app.config['UPLOAD_FOLDER'] = 'static/dataset1/'
app.config['ALLOWED_EXTENSIONS']=set(['txt','pdf','jpg','png','gif'])
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']
INDEX = os.path.join(os.path.dirname(__file__), 'index.csv')


# main route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():

    if request.method == "POST":

        RESULTS_ARRAY = []

        # get url
        image_url = 'static/'+request.form.get('img')
        print image_url

        try:

            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))

            # load the query image and describe it
            from skimage import io
            query = io.imread(image_url)
            print query.shape
            features = cd.describe(query)

            # perform the search
            searcher = Searcher(INDEX)
            results = searcher.search(features)

            # loop over the results, displaying the score and image name
            for (score, resultID) in results:
                RESULTS_ARRAY.append(
                    {"image": str(resultID), "score": str(score)})

            # return success
            return jsonify(results=(RESULTS_ARRAY[::-1][:3]))

        except:

            # return error
           return jsonify({"sorry": "Sorry, no results! Please try again."}), 500

@app.route('/upload',methods=['POST'])
def upload():
    file=request.files['file']
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    if request.method == "POST":

        RESULTS_ARRAY = []

        # get url


        try:

            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))

            # load the query image and describe it
            from skimage import io
            filename='static/dataset1/'+filename
            print filename
            query = io.imread(filename)
            print query.shape
            features = cd.describe(query)

            # perform the search
            searcher = Searcher(INDEX)
            results = searcher.search(features)

            # loop over the results, displaying the score and image name
            for (score, resultID) in results:
                RESULTS_ARRAY.append(
                    {"image": str(resultID), "score": str(score)})

            # return success
            return jsonify(results=(RESULTS_ARRAY[::-1][:3]))

        except:

            # return error
           return jsonify({"sorry": "Sorry, no results! Please try again."}), 500
        #return redirect(url_for('uploaded_file',filename=filename))
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
# run!
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
