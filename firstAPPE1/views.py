
from pickle import FALSE, TRUE
from pydoc import describe
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def renderTripulacion1(request):
    data = {

        'isTripulacion1' : True,
        "personaje1" : '/static/img/jimbei.png',
        #Informacion personaje 1#
        "nombre_l" : 'Jimbei',
        "apellido_l" : 'Hijo del mar',
        "profesion_l" : 'Navegador ',
        "edad_l" : '44 años',
        "ciudad_l" : 'Isla Gyojin',
        
        #Informacion personaje 2#
        "personaje2" : '/static/img/zoro.png',
        "nombre_k" : 'Zoro',
        "apellido_k" : 'Roronoa',
        "profesion_k" : 'Cazador de piratas',
        "edad_k" : '21',
        "ciudad_k" : 'East Blue',
         
        #Informacion personaje 3#
        "personaje3" : '/static/img/sanji.png',
        "nombre_b" : 'Sanji',
        "apellido_b" : 'Visnmoke',
        "profesion_b" : 'Cocinero',
        "edad_b" : '21 años',
        "ciudad_b" : 'North Blue',
       
      
    }
    return render(request, 'index.html', data)

def renderTripulacion2(request):
    data = {

        'isTripulacion1' : True,
        "personaje1" : '/static/img/king.png',
        #Informacion personaje 1#
        "nombre_l" : 'King',
        "apellido_l" : 'La Conflagacion',
        "profesion_l" : 'Jefe Asalto',
        "edad_l" : '47 años',
        "ciudad_l" : 'Onigashima',
        
        #Informacion personaje 2#
        "personaje2" : '/static/img/queen.png',
        "nombre_k" : 'Queen',
        "apellido_k" : 'La plaga',
        "profesion_k" : 'Inventor',
        "edad_k" : '23',
        "ciudad_k" : 'Onigashima',
         
        #Informacion personaje 3#
        "personaje3" : '/static/img/jack.png',
        "nombre_b" : 'Jack',
        "apellido_b" : 'La Sequia',
        "profesion_b" : 'Jefe Bestias',
        "edad_b" : '23 años',
        "ciudad_b" : 'Gyojin',

    }
    return render(request, 'index.html', data)

def renderTripulacion3(request):
    data = {
        'isTripulacion1' : True,
        "personaje1" : '/static/img/katakuri.png',
        #Informacion personaje 1#
        "nombre_l" : 'Katakuri',
        "apellido_l" : 'Charlotte',
        "profesion_l" : 'General Dulce 1',
        "edad_l" : '48 años',
        "ciudad_l" : 'Komugi',
        
        #Informacion personaje 2#
        "personaje2" : '/static/img/cracker.png',
        "nombre_k" : 'Cracker',
        "apellido_k" : 'Charlotte',
        "profesion_k" : 'General dulce 2',
        "edad_k" : '45',
        "ciudad_k" : 'Isla Biscuit',
         
        #Informacion personaje 3#
        "personaje3" : '/static/img/smoothie.png',
        "nombre_b" : 'Smoothie',
        "apellido_b" : 'Charlotte',
        "profesion_b" : 'General Dulce 3',
        "edad_b" : '35 años',
        "ciudad_b" : 'Isla chocolate',

    }
    return render(request, 'index.html', data)

def renderPagina1(request):
    data = {
        "imagen1" : '/static/img/youtube.png',
        "nombre" : 'Youtube',
        "fecha" : '19 de agosto de 2005',
        "cliente" : 'Lo puede utilizar toda persona interesada en aprender a programar mediante video tutoriales ',
        "descripcion" : 'YouTube es un sitio web de origen estadounidense dedicado a compartir videos. Contiene una variedad de clips de películas, programas de televisión y videos musicales, así como contenido amateur como vlogs y juegos de YouTube. En esta gran variedad de videos, encontramos personas dedicadas a la enseñanza de la programación desde lo más básico hasta lo más amplio y complejo, que se apoya mucho a medida que se desarrolla y aprende.',
        "link" : 'https://www.youtube.com/c/Programaci%C3%B3nATS',
        "tutoriales" : ' La pagina cuenta con videos que enseñan : HTML, CSS, JavaScript, SQL, PHP, XML. Entre otros',
        "idioma" : 'El idioma en el cual se basa es inglés, pero cuenta con la opción de cambiarlo a español lo que ayuda a su entendimiento',

    }
    return render(request, 'paginas.html',data)

def renderPagina2(request):
    data = {
        "imagen1" : '/static/img/django.png',
        "nombre" : 'Django',
        "fecha" : 'El año 2008',
        "cliente" : 'Lo puede utilizar toda persona interesada en aprender a programar',
        "descripcion" : 'Django es un framework web extremadamente popular y completamente funcional, escrito en Python. El módulo muestra por qué Django es uno de los frameworks de servidores web más populares, cómo configurar un entorno de desarrollo y cómo empezar a usarlo para crear tus propias aplicaciones web.',
        "link" : 'https://www.djangoproject.com/',
        "idioma" : 'El idioma en el cual se basa es inglés, pero cuenta con la opción de cambiarlo a español lo que ayuda a su entendimiento',
        "tutoriales" : ' Cuenta con tutoriales completos para empezar desde cero y aprender a programar de una manera eficiente utilizando esta plataforma',

    }
    return render(request, 'paginas.html',data)


def renderPagina3(request):
    data = {
        "imagen1" : '/static/img/bootstrap.png',
        "nombre" : 'Bootstrap',
        "fecha" : 'El año 2011',
        "cliente" : 'Lo puede utilizar toda persona que se encuentre interesada en aprender a programar .',
        "descripcion" : 'Bootstrap es un framework CSS y Javascript diseñado para la creación de interfaces limpias y con un diseño responsive. Además, ofrece un amplio abanico de herramientas y funciones, de manera que los usuarios pueden crear prácticamente cualquier tipo de sitio web haciendo uso de los mismos.',
        "link" : 'https://getbootstrap.com/',
        "idioma" : 'Los videos tutoriales se pueden encontrar en una gran variedad de idiomas ',
        "tutoriales" :' Esta pagina cuenta con guias de : HTML, CSS, java Entre otros',
    }
    return render(request, 'paginas.html',data)



#para mostrar en pagina de inicio#

