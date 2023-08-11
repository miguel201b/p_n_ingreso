from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random_string"

db = SQLAlchemy(app)


@app.route('/instructivo')
def instructivo():
    return render_template('Instructivo.html')

class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    apellido = db.Column(db.String(100))
    cuenta = db.Column(db.String(10))

@app.route('/')
def index():
    return render_template('Horario.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        apellido = request.form['apellido']
        cuenta = request.form['cuenta']
        
        # Aquí deberías verificar la disponibilidad del grupo y asignar al estudiante a un grupo.
        # Por simplicidad, sólo estamos registrando al estudiante.

        student = Students(apellido=apellido, cuenta=cuenta)
        db.session.add(student)
        db.session.commit()
        flash('Estudiante registrado con éxito!')
        
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
