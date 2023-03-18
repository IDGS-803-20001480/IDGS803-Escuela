from flask import Blueprint,render_template,redirect, request
from BD.db import get_connection, get_connection2
from Models.model import Maestro, db
from Models.forms import MaestroForm

maestros = Blueprint('maestros', __name__)

@maestros.route('/getmaestro', methods=['GET'])
def getMaestro():
    try:
        connection=get_connection2()
        maestros = []
        with connection.cursor() as cursor:
            cursor.execute('call AllMaestro()')
            resultset=cursor.fetchall()
            for row in resultset:
               maestros.append(Maestro( id = row[0], nombre = row[1], apellidos = row[2], email = row[3],materia = row[4]))
        connection.close()
        return render_template('ABCompleto.html', maestros=maestros)

    except Exception as ex:
       print(ex)
       pass
        
    #return {'Key':'Maestros'}

@maestros.route('/createMaestro', methods=['GET','POST'])
def createMaestro():
    create_form = MaestroForm(request.form)
    if request.method == 'POST':
        try:
            connection=get_connection2()
            with connection.cursor() as cursor:
                cursor.execute('call addMaestro(%s,%s,%s,%s)',(create_form.nombre.data,create_form.apellidos.data,create_form.email.data,create_form.materia.data))
                connection.commit()
            connection.close()
            return redirect('getmaestro')
        except Exception as ex:
            print(ex)
            pass
    return render_template('index.html', form=create_form)

@maestros.route('/updateMaestro', methods=['GET', 'POST'])
def updateMaestro():
    create_form = MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            connection=get_connection2()
            with connection.cursor() as cursor:
                cursor.execute('call findMaestro(%s)',(id))
                resultset=cursor.fetchall()
                for row in resultset:
                    create_form.id.data = row[0]
                    create_form.nombre.data = row[1]
                    create_form.apellidos.data = row[2]
                    create_form.email.data = row[3]
                    create_form.materia.data = row[4]
            connection.close()
            return render_template('modificar.html', form=create_form)
        except Exception as ex:
            print(ex)
            pass
    if request.method == 'POST':
        id = create_form.id.data
        try:
            connection=get_connection2()
            with connection.cursor() as cursor:
                cursor.execute('call updateMaestro(%s,%s,%s,%s,%s)',(id,create_form.nombre.data,create_form.apellidos.data,create_form.email.data,create_form.materia.data))
                connection.commit()
            connection.close()
            return redirect('getmaestro')
        except Exception as ex:
            print(ex)
            pass
    return render_template('modificar.html', form=create_form)


@maestros.route('/deleteMaestro', methods=['GET', 'POST'])
def deleteMaestro():
    create_form = MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            connection=get_connection2()
            with connection.cursor() as cursor:
                cursor.execute('call findMaestro(%s)',(id))
                resultset=cursor.fetchall()
                for row in resultset:
                    create_form.id.data = row[0]
                    create_form.nombre.data = row[1]
                    create_form.apellidos.data = row[2]
                    create_form.email.data = row[3]
                    create_form.materia.data = row[4]
            connection.close()
            return render_template('eliminar.html', form=create_form)
        except Exception as ex:
            print(ex)
            pass
    if request.method == 'POST':
        id = create_form.id.data
        try:
            connection=get_connection2()
            with connection.cursor() as cursor:
                cursor.execute('call deleteMaestro(%s)',(id))
                connection.commit()
            connection.close()
            return redirect('getmaestro')
        except Exception as ex:
            print(ex)
            pass
    return render_template('eliminar.html', form=create_form)