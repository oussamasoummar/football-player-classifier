
from flask import Flask, request, jsonify
import util
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    img_data = request.form['image_data']
    print(util.classify_image(img_data))
    
    response = jsonify(util.classify_image(img_data))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

 
if __name__ == "__main__":
    print("starting flask server to image classification")
    util.load_saved_artifacts()
    app.run(port=5000)
