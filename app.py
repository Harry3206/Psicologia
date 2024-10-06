from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulamos una base de datos de pacientes como una lista
pacientes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_paciente', methods=['GET', 'POST'])
def agregar_paciente():
    if request.method == 'POST':
        # Recogemos los datos del formulario
        nombre = request.form['nombre']
        edad = request.form['edad']
        telefono = request.form['telefono']
        fecha_primera_consulta = request.form['fecha_primera_consulta']
        notas = request.form['notas']
        
        # Creamos un diccionario con los datos del paciente y lo agregamos a la lista
        nuevo_paciente = {
            'nombre': nombre,
            'edad': edad,
            'telefono': telefono,
            'fecha_primera_consulta': fecha_primera_consulta,
            'notas': notas
        }
        pacientes.append(nuevo_paciente)

        # Redirigimos a la página de listado de pacientes
        return redirect(url_for('listar_pacientes'))
    
    return render_template('agregar_paciente.html')

@app.route('/listar_pacientes')
def listar_pacientes():
    # Pasamos la lista de pacientes a la plantilla
    return render_template('listar_pacientes.html', pacientes=pacientes)

if __name__ == '__main__':
    app.run(debug=True)
