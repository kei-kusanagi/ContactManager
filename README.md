Creamos una nueva carpeta e instalamos un entorno virtual donde correremos la app
```virtualenv -p pytho env```
y lo activamos
```.\env\Scripts\activate```


vamos a www.gotignore.io y creamos creamos uno añadiendo django y lo pegamos en nuestro .gitignore dentro de la carpeta /env/.gitignore

creamos nuestro archivo re requerimientos en la terminal atravez del comando
```pip freeze > requirements.txt```
![[Pasted image 20220614145530.png]]

iniciamos nuestro archivo git con el comando ```git init```  y ahora si a empezar

Luego creamos instalamos django
```pip install django```

Ahora si podemos crear un nuevo proyecto de Django con el comando 
```django-admin startproject contactmanager```

y dos app's adicionales, core y contact
``` django-admin startapp core```
``` django-admin startapp contact```

Importante ir inmediatamente a contactmanager/settings.py y declaramos las apps en INSTALED_APS
![[Pasted image 20220613220621.png]]

Ahora crearemos nuestros templates para la pagina, vamos a /core y creamos una carpeta llamada /templates y luego otra llamada /core
```core/templates/core```
y dentro creamos 2 archivos, base.html y frontpage.html y dentro de base copiamos el archivo inicial en https://tailwindcss.com/docs/installation/play-cdn

![[Pasted image 20220613220949.png]]

eso lo copiamos y pegamos en base.html y en frontpage.html solo ponemos
```{% extends 'core/base.html' %}```

Luego tenemos qe crear la views.py y declarar el path en urls.py asi que creemos la vista primero, vamos a core/views.py y escribimos lo siguiente

```
from django.shortcuts import render

  

def frontpage(request):

    return render(request, 'core/frontpage.html')
```

ahora en /core/urls.py agregamos su path asi
```
from django.contrib import admin

from django.urls import path

  

from core.views import frontpage

  

urlpatterns = [

    path('', frontpage, name='frontpage'),

    path('admin/', admin.site.urls),

]
```

ahora corremos el servidor desde la terminal con ```python manage.py runserver``` y vemos la magia
![[Pasted image 20220613222336.png]]

Ahora procederemos a darle algo de estilo para que se paresca mas a la tabla que queremos al final

Agregamos lo siguiente a base.html

```
<nav class="py-6 px-4 bg-gray-900 flex justify-between items-center">

		<h1 class="text-white text-2xl">Contact Manager</h1>

        <a href="#" class="p-3 bg-green-400 text-white text-xl rounded-xl">+</a>
        
</nav>
```
![[Pasted image 20220614154918.png]]

ahora crearemos las tablas que usaremos en la base de datos, vamos a contact/models.py y agregamos lo siguiente

```
class Category(models.Model):

    title = models.Charfield(max_length=255)
```

para agregar una tabla de tipo caracter con capasidad maxima de 255 caracteres

Y ahora una tabla FOREIGNKEY que es una columna que sirve para señalar cual es la llave primaria de otra tabl

```
class Contact(models.Model):

    category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE)

    first_name = models.Charfield(max_length=255)

    last_name = models.Charfield(max_length=255)

    email = models.EmailField()

    phone = models.Charfield(max_length=255)

    address = models.Charfield(max_length=255)

    zipcode = models.Charfield(max_length=255)

    city = models.Charfield(max_length=255)
```

(quitamos ese molesto texto rojo haciendo el ```python manage.py makemigrations``` y el ```python manage.py migrate``` )
![[Pasted image 20220614160439.png]]

como siguiente paso activaremos el boton de add asi que vamos a la pagina base.html y le añadimos esto al body solo para diferenciarlo del fondo de la pagina

```<body class="bg-gray-300">```

ahora vamos a la app de contact y modificaremos el archivo views.py (para añadir lo que hara el boton) mediante la siguiente funcion

```
from django.shortcuts import render

  

def add(request):

    return render(request, 'contact/add.html')
    
```

y luego importamos esto a contactmanager/urls.py, mandando a llamar primero la vista de contact atraves de la linea ```from contact import views as contact_views```

y luego agragammos la linia del path para que quede asi todo ```path('add/', contact_views.add, name='add'),```

```
from django.contrib import admin

from django.urls import path

  

from core.views import frontpage

from contact import views as contact_views

  

urlpatterns = [

    path('', frontpage, name='frontpage'),

    path('add/', contact_views.add, name='add'),

    path('admin/', admin.site.urls),
```

y luego vamos a nuestro base.html y activamos el boton
```<a href="{% url 'add' %}" class="p-3 bg-green-400 text-white```
luego añadimos el archivo y carpetas teplates y add.html contact/templates/contact/add.html y dentro extendemos la base

![[Pasted image 20220614203415.png]]

y en base.html quitamos el hello world y ponemos (el div es para darle pading a todo lo que este dentro del block content)
```
    <div class="px-6 py-4">

        {% block content %}

        {% endblock %}

    </div>
```
de esta forma para extender todo esto a las demas plantillas
![[Pasted image 20220614205314.png]]

y luego en add.html ponemos 
```
{% extends 'core/base.html' %}

{% block content %}

    <div class="bg-gray-500 rounded-xl">

        asdf

    </div>

{% endblock %}

```
![[Pasted image 20220614205331.png]]


ya con el estilo correcto, regresamos a add.html y agregamos lo siguiente para pdoer escribir en la base de datos el dato correspondiente y agregamos ```name=first_name```

```
{% extends 'core/base.html' %}

{% block content %}

    <div class="p-6 bg-gray-500 rounded-xl">

        <form method="post" action="." class="space-y-4">

            {% csrf_token %}

            <div>

                <label>First name</label><br>

                <input type="text" name="first_name" class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">

            </div>

{% endblock %}
```

![[Pasted image 20220614211659.png]]

ahora copiamos y pegamos el div para Last name, Email, Phone, Zipcode y City

y agregamos un boton de Sumbit al final para que quede asi
```
<div>

	<button class="p-3 bg-green-400 text-white text-xl rounded-xl">Sumbit</button>

</div>
```
![[Pasted image 20220614212446.png]]

podemos agregar un enlase para que cada que demos click en el titulo nos regrese a la pantalla principal
```
<a href="{% url 'frontpage' %}" class="text-white text-2xl">Contact Manager</a>
```

Hermoso, ahora tenemos que agregar las categorias en el sitio de administracion, ais que nos vamos a /contact/admin.py

```
from django.contrib import admin
 
from .models import Category

admin.site.register(Category
```

ahora creamos un super usuario, regresamos a la terminal y ponemos el siguiente comando
```python manage.py creatseuperuser```
y llenamos los datos
![[Pasted image 20220614212926.png]]

nos vamos a nuestro servidor al area de administracion http://127.0.0.1:8000/admin/ y nos logeamos
![[Pasted image 20220614213039.png]]

cramos una nueva categoria y le ponemos "Private" y otra para "Work"
![[Pasted image 20220614213202.png]]

creadas nuestras categorias, ahora vamos a dar la opcion de seleccionarlo dentro de nuestra pagina para añadir

```
<div>
	<label>Category</label><br>
	<select name="category" class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">
		<option value="">Please select</option>
		{% for category in categories %}
			<option value="{{ category.id }}">{{ category.title }}</option>
		{% endfor %}
	</select>
</div>
```

y en nuestro archivo de /contact/views.py tenemos que agregar lo siguiente para que funcione el loop de las categorias a seleccionar

```
from django.shortcuts import render

  

from .models import Category

  

def add(request):

    categories = Category.Objects.all()

  

    return render(request, 'contact/add.html', {

        'categories': categories

        })
```


![[Pasted image 20220614214640.png]]
![[Pasted image 20220614214656.png]]

Ahora solo necesitamos manejar el envio de la forma en las vistas, asi que regresamos a /contact/views.py y agregamos cada campo dentro de un if y luego con ``Contact.objects.create`` los asignamos a un nuebo objeto y añadimos al final ``return redirect('frontpage')`` para que nos regrese a la pagina principal

![[Pasted image 20220614220127.png]]

checamos que el servidor no arroje ningun error y procedemos a llenar datos de prueba y darle el boton Submit para checar que lo guarde en la base de datos
![[Pasted image 20220614221250.png]]

y al darle en Sumbit nos regresara a la primera pagina y en la terminal nos mostrara lo siguiente

![[Pasted image 20220614221457.png]]


a continuacion mostraremos la lista de contactos en nuestra frontpage, para esto necesitamos ir a /core/views.py y creamos la bariable contacts asignandole los objetos, de la sigueinte manera

```
from django.shortcuts import render

from contact.models import Contact
 

def frontpage(request):

    contacts = Contact.objects.all()

    return render(request, 'core/frontpage.html', {

        'contacts': contacts

    })
```

y ahora en nuestra frontpage.html agregamos el sigueinte codigo que nos permitira hacer un bucle for por cada contacto en nuestra lista de contactos

```
{% extends 'core/base.html' %}

{% block content %}

    {% for contact in contacts %}

    <ddiv class="px-4 py-6 text-center">

        <h2 class="text-xl">{{ contact.first_name }} {{ contact.last_name }}</h2>

    </ddiv>

{% endblock %}
```

Y ahora al recargar la pagina principal nos mostrara los contactos ya agregados

![[Pasted image 20220615171822.png]]

Le agregaremos algo de estilo para que nos aparesca mas informacion sobre los contactos, quedando asi

```
{% extends 'core/base.html' %}

  
{% block content %}

    <div class="space-y-5">

        {% for contact in contacts %}

            <div class="px-4 py-6 text-center bg-gray-500 rounded-xl">

                <h2 class="mb-2 text-xl">{{ contact.first_name }} {{ contact.last_name }}</h2>

                <h3 class="text-5m text-gray-900">{{ contact.category.title }}</h3>

  

                <p><strong>E-mail:</strong>{{ contact.email }}</p>

                <p><strong>Phone:</strong>{{ contact.phone }}</p>

  

                <p class="mt-6">

                    {{ contact.address }}<br>

                    {{ contact.zipcode }} {{contact.city }}

                </p>

            </div>

        {% endfor %}

    </div>

{% endblock %}
```
![[Pasted image 20220615193017.png]]

ahora pondremos la funcionalidad de poder editar los contactos añadidos, nos vamos a /contact/views.py  y añadimos la siguiente funcion

```
...
from django.shortcuts import get_object_or_404, render, redirect
...

def edit(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

  

    return render(request, 'contact/edit.html', {

        'contact': contact

    })

```

ahora en /contactmanager/urls.py devemos agregar ese path

``` 
...
path('contacts/<int:pk>/', contact_views.edit, name='edit'),
...

```

y copiamos practicamente todo el archivo de add.html en la misma carpeta de /contact/templates/contact y le ponemos edit.html, ahora si vamos a la direccion
http://127.0.0.1:8000/contacts/1/ nos mostrara la misma plantilla de añadir, bien ahora solo tendremos que editarla

![[Pasted image 20220615195325.png]]

ahora a cada ``<div>``  le agregamos un ``value="{{ contact.control }}"`` y quedaria asi

```
<div>
	<label>First name</label><br>
		<input type="text" value="{{ contact.first_name }}" name="first_name" class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">

</div>
```

ahora copiamos y pegamos esto en todos los demas ``<div>`` 's
![[Pasted image 20220615195914.png]]

para la categoria agregamos un {% if %} quedando asi

```
<div>
	<label>Category</label><br>
	<select name="category" class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">
		<option value="">Please select</option>
		{% for category in categories %}
			<option
				value="{{ category.id }}"
				{% if category.id == contact.category_id %} selected {% endif %}
			>
				{{ category.title }}
			</option>
		{% endfor %}
	</select>
</div>
```

y en /contacts/views.py agregamos a la funcion el objecto categories

```
def edit(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    categories = Category.objects.all()

  

    return render(request, 'contact/edit.html', {

        'contact': contact,

        'categories': categories

    })
```

![[Pasted image 20220615200856.png]]

ahora agregamos todos los objetos a la funcion para que al momento de salvar mande los nuevos datos a la categorya, nombre yo dato correspondiente

```
def edit(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    categories = Category.objects.all()

  

    if request.method == 'POST':

        contact.category_id = request.POST.get('category')

        contact.first_name = request.POST.get('first_name')

        contact.last_name = request.POST.get('last_name')

        contact.email = request.POST.get('email')

        contact.phone = request.POST.get('phone')

        contact.address = request.POST.get('address')

        contact.zipcode = request.POST.get('zipcode')

        contact.city = request.POST.get('city')

  

        contact.save()

        return redirect('frontpage')

  

    return render(request, 'contact/edit.html', {

        'contact': contact,

        'categories': categories

    })
```

ahora agregaremos el entrar a este modo de editar al darle click a la tarjeta de contacto, para esto vamos a frontpage.html

```
<div class="mt-6 items-end text-left">
	<a href="{% url 'edit' contact.id %}" class="px-4 py-2 bg-green-800 text_white rounded-xl">Edit</a>
</div>
```
![[Pasted image 20220615203302.png]]

y ya al darle click nos llevara a la pagina edit del contacto (por eso le pusimos el ``{% url 'edit' contact.id %}`` )


ahora podemos ponerle la funcion de borrar contacctos, asiq ue vamos a /contact/views.py y agregamos la siguiente funcion

```
def delete(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    contact.delete()

    return redirect('frontpage')
```

ahora vamos a /contactmanager/urls.py y agregamos el siguiente path

```
path('contacts/<int:pk>/delete', contact_views.delete, name='delete'),
```

ahora vamos a nuestro frontpage.html y copiamos y pegamos el mismo boton de edit pero lo cambiamos para que al presionarlo llame la funcion "delete"

![[Pasted image 20220616162830.png]]

Ya casi acavamos, agregaremos una barra de busqueda, asi que vamos a frontpage.html y agregemos el siguiente div
```
{% block content %}
	<div class="mb-4">
		<form method="get" action=".">
            <input type="text" name="query" placeholder="Search..." class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">
        </form>
    </div>
```
![[Pasted image 20220616164620.png]]

ahora le pondremos su funcion para buscar, vamos a /core/views.py y agregamos lo siguiente en la funcion de frontpage(request)

```
query = request.GET.get('query', '')

    if query:
        contacts = contacts.filter(first_name__icontains=query)
```

ahora al buscar algo que contenfa first name dentro de los contactos nos arrojara solo ese contacto

![[Pasted image 20220616171708.png]]

si queremos hacer lo mismo ya sea con el email, direccion ocualquier otro dato necesitamos un modelo de django llamado Q y lo importamos alli mismo en /core/views.py
``from django.db.models import Q`` 

y modificamos el "if" para que quede de la siguiente manera

```
    if query:

        contacts = contacts.filter(

            Q(first_name__icontains=query)

            |

            Q(last_name__icontains=query)

            |

            Q(email__icontains=query)

            |

            Q(phone__icontains=query)

            |

            Q(address__icontains=query)

            |

            Q(zipcode__icontains=query)

            |

            Q(city__icontains=query)

        )
```
 y listo, cada que escribamos algo que este contenido en el nombre o apellidos o email, telefono o cualquier dato aparecera en nuestra busqueda

![[Pasted image 20220616173016.png]]

ahora podemos agregar lo siguiente justo antes de terminar el bucle for en frontpage.html para que si al buscar no nos arroja ningun resultado salga un mensaje de "No results..."

```
        {% empty %}

            <div class="px-4 py-6 text-center bg-gray-500 rounded-xl">

                <p>No results...</p>

            </div>

        {% endfor %}
```
![[Pasted image 20220616173400.png]]