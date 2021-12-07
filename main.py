from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
import pandas as pd
import csv
import os

app=Flask(__name__)

@app.route('/')
def upload_this():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def upload_files():
    if request.method=='POST':
        f=request.files['file']
        filename=secure_filename(f.filename)
        f.save(os.path.join(r'C:\Users\keith\flask_csvupload',filename))

        return 'file upload successfully'
#app.config["UPLOAD_PATH"]=r"C:\Users\keith\flask_csvupload"



if __name__=="__main__":
    app.run(debug=True)