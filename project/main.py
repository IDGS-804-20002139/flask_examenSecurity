import os
from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_security import login_required, current_user
from flask_security.decorators import roles_required,roles_accepted
from . import db, forms
from project.models import Role, animesdb
from werkzeug.utils import secure_filename

main = Blueprint('main',__name__)

#Definimos las rutas

#Definimos la ruta para la página principal
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contacto')
def contacto():
    return render_template('contacto.html')


@main.route('/guardar')
@login_required
@roles_required('admin')
@roles_accepted()
def guardar():
    return render_template('guardar.html')

@main.route('/guardar', methods=['POST'])
@login_required
@roles_required('admin')
@roles_accepted()
def guardar_post():
    nombre= request.form.get('nombre')
    anio= request.form.get('anio')
    autor= request.form.get('autor')
    precio= request.form.get('precio')
    imagen= request.form.get('imagen')

    if request.method=='POST':
        ani=animesdb(nombre=nombre, anio=anio, autor=autor, precio=precio, imagen=imagen)
        db.session.add(ani)
        db.session.commit()
        return redirect(url_for('main.anime'))

    return render_template('guardar.html',name=current_user.name)



@main.route('/anime')
@login_required
def anime():

    anime = animesdb.query.all()
    
    return render_template('anime.html', name = current_user.name, anime=anime)





@main.route("/modificar", methods=['GET','POST'])
@login_required
@roles_required('admin')
@roles_accepted()
def modificar():
    create_form=forms.AnimeForms(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        ani=db.session.query(animesdb).filter(animesdb.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=ani.nombre
        create_form.anio.data=ani.anio
        create_form.autor.data=ani.autor
        create_form.precio.data=ani.precio
        create_form.imagen.data=ani.imagen

    if request.method=='POST':
        id=create_form.id.data
        ani=db.session.query(animesdb).filter(animesdb.id==id).first()
        ani.nombre=create_form.nombre.data
        ani.anio=create_form.anio.data
        ani.autor=create_form.autor.data
        ani.precio=create_form.precio.data
        ani.imagen=create_form.imagen.data
        db.session.add(ani)
        db.session.commit()
        return redirect(url_for('main.anime'))
    return render_template('modificar.html',form=create_form)

@main.route("/eliminar", methods=['GET','POST'])
@login_required
@roles_required('admin')
@roles_accepted()
def eliminar():
    create_form=forms.AnimeForms(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        ani=db.session.query(animesdb).filter(animesdb.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=ani.nombre
        create_form.anio.data=ani.anio
        create_form.autor.data=ani.autor
        create_form.precio.data=ani.precio
        create_form.imagen.data=ani.imagen

    if request.method=='POST':
        id=create_form.id.data
        ani=db.session.query(animesdb).filter(animesdb.id==id).first()
        db.session.delete(ani)
        db.session.commit()
        return redirect(url_for('main.anime'))
    return render_template('eliminar.html',form=create_form)