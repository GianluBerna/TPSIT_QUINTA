from flask import Flask, request, render_template
from AlphaBot import AlphaBot
alphabot=AlphaBot()
alphabot.stop()
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])          #decoratore
def index():

    if request.method == 'POST':
        dir = request.form['direzione']
        switcher = {
            "forward": alphabot.forward,
            "backward": alphabot.backward,
            "right": alphabot.right,
            "left": alphabot.left,
            "stop": alphabot.stop
        }
        switcher[dir]()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.1.12', debug='on')
