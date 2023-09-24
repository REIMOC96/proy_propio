from django.http import HttpResponse
from django.template import Template, Context

"""intento de primer index"""

"""
definir index como objeto 
"""

def index(request):
   """
   creamos una variable donde guardar la plantilla y 
   abrimos html como plantilla usando la funcion open e invcluyendo la ruta del archivo"""
   doc_ext = open("A:/P_django/proyecto_ini/plantillas/index.html")

   """leer archivo html usando template y funcion read y guardamos su resultado en plt"""
   plt = Template(doc_ext.read())   

   """cerrar el archivo externo ya que tenemos su lectura guardada en la variable plt"""
   doc_ext.close()

   """crear variable y guardar la funcion context ahi"""
   ctx=Context()

   """para renderizar todo se crea una variable y se llama a la variable que tiene el
    template cargado osea plt y llamar a la funcion render usando ctx para referenciar al
     contexto, todo esto se guarda en la variable rndr """
   rndr = plt.render(ctx)

   """retornamos un http de respuesta haciendo llamado a la variable que tiene el render 
   del archivo template y el contexto, en este caso se llama rndr"""
   return HttpResponse(rndr)
"""notas
importar librerias necesarias de django:
from django.Http import HttpResponse
from django.template import Template, Context

definir la plantilla:
 def nombre_plantilla():

las plantillas se usan en tres pasos:
crear objeto de tipo template

"""