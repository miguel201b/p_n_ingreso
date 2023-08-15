from flask import Flask, render_template
from horario_tabla import obtener_horario

app = Flask(__name__)

@app.route('/horarios/<letra>')
def horarios(letra):
    horario,hora_inicio = obtener_horario(letra)
    return render_template('horario_semana.html', horario=horario, hora_inicio=hora_inicio)

if __name__ == '__main__':
    app.run(debug=True)
