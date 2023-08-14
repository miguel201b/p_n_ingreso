from flask import Flask, render_template, request, redirect, url_for,Response,jsonify
import csv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from io import StringIO
import os
from unidecode import unidecode
from horario_tabla import obtener_horario

def formato_apellido(input_str):
    return unidecode(input_str).lower()

def assign_group(apellido):
    if 'a' <= apellido[0] <= 'f':
        time_slot = "9"
    elif 'g' <= apellido[0] <= 'm':
        time_slot = "11"
    else:
        time_slot = "13"
    group = Groups.query.filter_by(time_slot=time_slot).filter(Groups.current_students < Groups.max_students).order_by(Groups.id).first()
    if not group:
        raise Exception(f"No hay grupos disponibles para el horario {time_slot}")
    return group

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SECRET_KEY'] = "random_string"
 
#Modelo de la base de datos
db = SQLAlchemy(app)
 
class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    apellido = db.Column(db.String(100),nullable = False)
    cuenta = db.Column(db.String(10), nullable = False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=True)
    group = db.relationship('Groups', backref=db.backref('students', lazy=True))
    def __repr__(self):
        return '<Name %r>' % self.id

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    max_students = db.Column(db.Integer, default=55)
    current_students = db.Column(db.Integer, default=0)
    time_slot = db.Column(db.String(10), nullable=False) # Esto puede ser "9", "11" o "13"

    
@app.route('/download_csv')
def download_csv():
    # Realizar la consulta
    students = Students.query.all()

    # Usa StringIO para simular un archivo en memoria
    si = StringIO()
    writer = csv.writer(si)

    # Escribe los encabezados y datos en el "archivo"
    writer.writerow(['ID', 'Apellido', 'Cuenta'])
    for student in students:
        writer.writerow([student.id, student.apellido, student.cuenta])

    # Crea una respuesta con el contenido del "archivo"
    response = Response(si.getvalue(), content_type='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=students.csv'

    return response

@app.route('/instructivo')
def instructivo():
    return render_template('Instructivo.html')

@app.route('/calendario')
def calendario():
    return render_template('Calendario.html')

@app.route('/horario')
def horario():
    return render_template('Horario.html')

@app.route('/horario/<letra>')
def horarios(letra):
    horario,hora_inicio = obtener_horario(letra)
    return render_template('horario_semana.html', horario=horario, hora_inicio=hora_inicio)

@app.route('/index')
def idex1():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('Horario.html')

@app.route('/registrados')
def registrados():
    title = 'Alumnos registrados'
    students = Students.query.all() 
    return render_template('registrados.html', title=title,students=students)

@app.route('/horario', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        apellido = request.form['apellido']
        apellido = formato_apellido(apellido)
        letra = apellido[0]
        cuenta = request.form['cuenta']
        if not cuenta.startswith(("324", "1")):
            return jsonify({"success": False, "message": "Número de cuenta inválido."})
        
        else:
            group = assign_group(apellido)
            group.current_students += 1

            try:
                student = Students(apellido=apellido, cuenta=cuenta,group = group)
                db.session.add(student)
                db.session.commit()
                return jsonify({"success": True, "message": "Estudiante registrado con éxito!"})
            except Exception as e:
                print(e)  
                return jsonify({"success": False, "message": "Error registrando al estudiante. Por favor, inténtalo de nuevo."})
            
    return redirect(url_for('foo'))

@app.route('/foo')
def foo():
    return 'Hello Foo!'

if __name__ == "__main__":
    app.run(debug = True)
