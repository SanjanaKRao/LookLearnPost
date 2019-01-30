
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pic", methods=['GET,POST'])
def caption():
    if request.method == 'POST':
      picha = request.form['Picture']
      return render_template("next.html",name=picha)
   else:
      user = request.args.get('Picture')
      return redirect(url_for('next.html',name = picha))



if __name__ == '__main__':
    app.run(debug = True)