from flask_sqlalchemy import SQLAlchemy
   
from  flask import Flask, render_template, session, redirect, request, url_for

app = Flask(__name__)
app.secret_key= 'c2a4af45faf9707ac9e7c9c8646c3e8a8f3122e9'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db1.sqlite"

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    nombre = db.Column(db.Text, nullable=False)

with app.app_context():
   db.create_all()


@app.route("/")
def index():
   return render_template('index.html')


@app.route("/segura")
def segura():
    if session : 
        return render_template('segura.html')
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=['GET','POST'])
def login():
   if request.method == 'POST':
      email = str(request.form.get('email'))
      password = request.form.get('password')
      usuario = Usuario.query.filter_by(email=email).first()
      if Usuario:
         session['name']= usuario.nombre
         return redirect(url_for('segura'))
   return render_template('login.html')


@app.route("/error")
def error():
   return render_template('error.html')

@app.route("/logout")
def logout():
   session.clear()
   return redirect(url_for('login'))

@app.route('/profile')
def profile():
    current_user = get_current_user()  
    return render_template('profile.html', user=current_user)

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        current_user = get_current_user()
        new_password = request.form['new_password']
        current_user.set_password(new_password)
        db.session.commit()
        Flask('Contraseña actualizada exitosamente.', 'success')
        return redirect(url_for('perfil'))
    return render_template('change_password.html')


if __name__ == '__main__':
 app.run(debug=True) 