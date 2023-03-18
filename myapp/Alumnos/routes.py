from flask import Blueprint,render_template,redirect, request,url_for
from Models.model import Alumno, db
from Models.forms import UserForm


alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/getalum', methods=['GET'])
def getalum():
    create_form = UserForm(request.form)
    #select * form alumnos
    alumnos = Alumno.query.all()
    return render_template('ABCompletoAlum.html', form=create_form, alumnos=alumnos)
    #return {'Key':'Alumnos'}

@alumnos.route('/createalum', methods=['GET','POST'])
def createalum():
    create_form = UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        print('Hola')
        print(create_form.nombre.data)
        alum = Alumno(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect('getalum')
    return render_template('indexAlum.html', form=create_form)

@alumnos.route('/updatealum', methods=['GET', 'POST'])
def updatealum():
    create_form = UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select * from alumnos where id = id
        alumn1 = db.session.query(Alumno).filter(Alumno.id == id).first()
        create_form.id.data = alumn1.id
        create_form.nombre.data = alumn1.nombre
        create_form.apellidos.data = alumn1.apellidos
        create_form.email.data = alumn1.email
        return render_template('modificarAlum.html', form=create_form)
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumno).filter(Alumno.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect('getalum')
    return render_template('modificarAlum.html', form=create_form)

@alumnos.route('/deletealum', methods=['GET', 'POST'])
def deletealum():
    create_form = UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select * from alumnos where id = id
        alumn1 = db.session.query(Alumno).filter(Alumno.id == id).first()
        create_form.id.data = alumn1.id
        create_form.nombre.data = alumn1.nombre
        create_form.apellidos.data = alumn1.apellidos
        create_form.email.data = alumn1.email
        return render_template('eliminarAlum.html', form=create_form)
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumno).filter(Alumno.id == id).first()
        db.session.delete(alum)
        db.session.commit()
        return redirect('getalum')
    return render_template('eliminar.html', form=create_form)