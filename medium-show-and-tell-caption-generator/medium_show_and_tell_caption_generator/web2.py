
import subprocess
import subprocess
import shlex


"""def shll():

    cmd = ["docker","run","-v","$PWD:/opt/app" ,"-e", "PYTHONPATH=$PYTHONPATH:/opt/app","-it", "medium-show-and-tell-caption-generator",  "python3" ,"/opt/app/medium_show_and_tell_caption_generator/inference.py", "--model_path", "/opt/app/etc/show-and-tell.pb", "--input_files", "/opt/app/imgs/\"download 1\".jpeg" ,"--vocab_file", "/opt/app/etc/word_counts.txt"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    print (out)
    return out"""

from flask import Flask, render_template, request, redirect, url_for,flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route("/")
def my_form():
    """if request.method == 'POST':
        picha = request.form['Picture']
        return redirect(url_for('caption',name=picha))
    else:
        user = request.args.get('Picture')
        return redirect(url_for('caption',name = picha))
    return render_template('index.html')"""
    return render_template("index.html")

UPLOAD_FOLDER = './static/thumbs'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


"""@app.route("/caption",methods=['POST'])
def caption():
  if request.method =='POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return hello()
  return render_template('next.html',te="ahoy")"""
  
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            
            subprocess.call(['bash','run.sh',filename])
            return redirect(url_for('hello', filename="thumbs/"+filename))
            #return render_template('next2.html', filename="thumbs/"+filename)
    return 'OK'

    
@app.route('/hello')
def hello():
    
    filename = request.args.get('filename')
   
    text = open('out.txt', 'r')
    content = text.readlines()
    line1=content[6]
    line2=content[7]
    line3=content[8]
    
    text.close()
    #return render_template('content.html', text=content)
    print(content)
    

    return render_template('next2.html',text1=line1,text2=line2,text3=line3,filename=filename)

if __name__ == '__main__':
    app.run(debug = True)
