from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField

from wtforms import validators
    
class AnimeForms(Form):
    id=IntegerField('id',[validators.number_range(min=1, max=20, message='Valor no validado')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='Valor no valido')])
    anio=StringField('Año',{
        validators.DataRequired(message='Valor no valido')})
    autor=StringField('Autor',[
        validators.DataRequired(message='Valor no valido')])
    precio=StringField('prcio',[
        validators.DataRequired(message='Valor no valido')])
    imagen=StringField('imagen',[
        validators.DataRequired(message='Valor no valido')])
    