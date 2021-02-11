from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])        #decoratore
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion == False:
            error = "Credenziali non valide. Riprova"
        else:
            #return redirect(url_for('secret'))
            return (f"Credenziali esatte")
    #return render_template('index.html', error=error)
    return (f"Credenziali giuste")

def validate(username,password):
    db_connection = sqlite3.connect('static/credenziali.db')
    db_cursor = db_connection.cursor()

    for row in db_cursor.execute(f'SELECT username,password FROM credenziali'):
        if row[0] == username and row[1] == password:
            db_connection.close()
            print("Credenziali giuste")
            return True

    db_connection.close()
    print("Credenziali errate")
    return False

@app.route('/secret')
def secret():
    return "Pagina Segreta"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug='on')
