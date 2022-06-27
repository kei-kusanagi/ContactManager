Creamos una nueva carpeta e instalamos un entorno virtual donde correremos la app
```virtualenv -p pytho env```
y lo activamos
```.\env\Scripts\activate```


vamos a www.gotignore.io y creamos creamos uno añadiendo django y lo pegamos en nuestro .gitignore dentro de la carpeta /env/.gitignore

creamos nuestro archivo re requerimientos en la terminal a través del comando
```pip freeze > requirements.txt```
![image](img/Pasted%20image%2020220614145530.png)

iniciamos nuestro archivo git con el comando ```git init```  y ahora si a empezar

Luego creamos instalamos django
```pip install django```

Ahora si podemos crear un nuevo proyecto de Django con el comando 
```django-admin startproject contactmanager```

y dos app's adicionales, core y contact
``` django-admin startapp core```
``` django-admin startapp contact```

Importante ir inmediatamente a contactmanager/settings.py y declaramos las apps en INSTALED_APS
![image](img/Pasted%20image%2020220613220621.png)

Ahora crearemos nuestros templates para la pagina, vamos a /core y creamos una carpeta llamada /templates y luego otra llamada /core
```core/templates/core```
y dentro creamos 2 archivos, base.html y frontpage.html y dentro de base copiamos el archivo inicial en https://tailwindcss.com/docs/installation/play-cdn

![image](img/Pasted%20image%2020220613220949.png)

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
![image](img/Pasted%20image%2020220613222336.png)

Ahora procederemos a darle algo de estilo para que se parezca mas a la tabla que queremos al final

Agregamos lo siguiente a base.html

```
<nav class="py-6 px-4 bg-gray-900 flex justify-between items-center">

		<h1 class="text-white text-2xl">Contact Manager</h1>

        <a href="#" class="p-3 bg-green-400 text-white text-xl rounded-xl">+</a>
        
</nav>
```
![image](img/Pasted%20image%2020220614154918.png)

ahora crearemos las tablas que usaremos en la base de datos, vamos a contact/models.py y agregamos lo siguiente

```
class Category(models.Model):

    title = models.Charfield(max_length=255)
```

para agregar una tabla de tipo carácter con capacidad máxima de 255 caracteres

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
![image](img/Pasted%20image%2020220614160439.png)

como siguiente paso activaremos el botón de add asi que vamos a la pagina base.html y le añadimos esto al body solo para diferenciarlo del fondo de la pagina

```<body class="bg-gray-300">```

ahora vamos a la app de contact y modificaremos el archivo views.py (para añadir lo que hará el boton) mediante la siguiente función

```
from django.shortcuts import render

  

def add(request):

    return render(request, 'contact/add.html')
    
```

y luego importamos esto a contactmanager/urls.py, mandando a llamar primero la vista de contact a traves de la linea ```from contact import views as contact_views```

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
luego añadimos el archivo y carpetas templates y add.html contact/templates/contact/add.html y dentro extendemos la base

![image](img/Pasted%20image%2020220614203415.png)

y en base.html quitamos el hello world y ponemos (el div es para darle pading a todo lo que este dentro del block content)
```
    <div class="px-6 py-4">

        {% block content %}

        {% endblock %}

    </div>
```
de esta forma para extender todo esto a las demás plantillas
![image](img/Pasted%20image%2020220614205314.png)

y luego en add.html ponemos 
```
{% extends 'core/base.html' %}

{% block content %}

    <div class="bg-gray-500 rounded-xl">

        asdf

    </div>

{% endblock %}

```
![image](img/Pasted%20image%2020220614205331.png)


ya con el estilo correcto, regresamos a add.html y agregamos lo siguiente para poder escribir en la base de datos el dato correspondiente y agregamos ```name=first_name```

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

![image](img/Pasted%20image%2020220614211659.png)

ahora copiamos y pegamos el div para Last name, Email, Phone, Zipcode y City

y agregamos un botón de Sumbit al final para que quede asi
```
<div>

	<button class="p-3 bg-green-400 text-white text-xl rounded-xl">Sumbit</button>

</div>
```
![image](img/Pasted%20image%2020220614212446.png)

podemos agregar un enlace para que cada que demos clic en el titulo nos regrese a la pantalla principal
```
<a href="{% url 'frontpage' %}" class="text-white text-2xl">Contact Manager</a>
```

Hermoso, ahora tenemos que agregar las categorías en el sitio de administración, así que nos vamos a /contact/admin.py

```
from django.contrib import admin
 
from .models import Category

admin.site.register(Category
```

ahora creamos un super usuario, regresamos a la terminal y ponemos el siguiente comando
```python manage.py creatseuperuser```
y llenamos los datos
![image](img/Pasted%20image%2020220614212926.png)

nos vamos a nuestro servidor al área de administración http://127.0.0.1:8000/admin/ y nos logamos
![image](img/Pasted%20image%2020220614213039.png)

creamos una nueva categoría y le ponemos "Private" y otra para "Work"
![image](img/Pasted%20image%2020220614213202.png)

creadas nuestras categorías, ahora vamos a dar la opción de seleccionarlo dentro de nuestra pagina para añadir

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

y en nuestro archivo de /contact/views.py tenemos que agregar lo siguiente para que funcione el loop de las categorías a seleccionar

```
from django.shortcuts import render

  

from .models import Category

  

def add(request):

    categories = Category.Objects.all()

  

    return render(request, 'contact/add.html', {

        'categories': categories

        })
```


![image](img/Pasted%20image%2020220614214640.png)
![image](img/Pasted%20image%2020220614214656.png)

Ahora solo necesitamos manejar el envió de la forma en las vistas, así que regresamos a /contact/views.py y agregamos cada campo dentro de un if y luego con ``Contact.objects.create`` los asignamos a un nuevo objeto y añadimos al final ``return redirect('frontpage')`` para que nos regrese a la pagina principal

![image](img/Pasted%20image%2020220614220127.png)

checamos que el servidor no arroje ningún error y procedemos a llenar datos de prueba y darle el botón Sumbit para checar que lo guarde en la base de datos
![image](img/Pasted%20image%2020220614221250.png)

y al darle en Sumbit nos regresara a la primera pagina y en la terminal nos mostrara lo siguiente

![image](img/Pasted%20image%2020220614221457.png)


a continuación mostraremos la lista de contactos en nuestra frontpage, para esto necesitamos ir a /core/views.py y creamos la variable contacts asignándole los objetos, de la siguiente manera

```
from django.shortcuts import render

from contact.models import Contact
 

def frontpage(request):

    contacts = Contact.objects.all()

    return render(request, 'core/frontpage.html', {

        'contacts': contacts

    })
```

y ahora en nuestra frontpage.html agregamos el siguiente código que nos permitirá hacer un bucle for por cada contacto en nuestra lista de contactos

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

![image](img/Pasted%20image%2020220615171822.png)

Le agregaremos algo de estilo para que nos aparezca mas información sobre los contactos, quedando asi

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
![image](img/Pasted%20image%2020220615193017.png)

ahora pondremos la funcionalidad de poder editar los contactos añadidos, nos vamos a /contact/views.py  y añadimos la siguiente función

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

ahora en /contactmanager/urls.py debemos agregar ese path

``` 
...
path('contacts/<int:pk>/', contact_views.edit, name='edit'),
...

```

y copiamos prácticamente todo el archivo de add.html en la misma carpeta de /contact/templates/contact y le ponemos edit.html, ahora si vamos a la dirección
http://127.0.0.1:8000/contacts/1/ nos mostrara la misma plantilla de añadir, bien ahora solo tendremos que editarla

![image](img/Pasted%20image%2020220615195325.png)

ahora a cada ``<div>``  le agregamos un ``value="{{ contact.control }}"`` y quedaria asi

```
<div>
	<label>First name</label><br>
		<input type="text" value="{{ contact.first_name }}" name="first_name" class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">

</div>
```

ahora copiamos y pegamos esto en todos los demas ``<div>`` 's
![image](img/Pasted%20image%2020220615195914.png)

para la categoría agregamos un {% if %} quedando asi

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

y en /contacts/views.py agregamos a la función el objeto categories

```
def edit(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    categories = Category.objects.all()

  

    return render(request, 'contact/edit.html', {

        'contact': contact,

        'categories': categories

    })
```

![image](img/Pasted%20image%2020220615200856.png)

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

ahora agregaremos el entrar a este modo de editar al darle clic a la tarjeta de contacto, para esto vamos a frontpage.html

```
<div class="mt-6 items-end text-left">
	<a href="{% url 'edit' contact.id %}" class="px-4 py-2 bg-green-800 text_white rounded-xl">Edit</a>
</div>
```
![image](img/Pasted%20image%2020220615203302.png)

y ya al darle clic nos llevara a la pagina edit del contacto (por eso le pusimos el ``{% url 'edit' contact.id %}`` )


ahora podemos ponerle la función de borrar contactos, así que vamos a /contact/views.py y agregamos la siguiente función

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

ahora vamos a nuestro frontpage.html y copiamos y pegamos el mismo botón de edit pero lo cambiamos para que al presionarlo llame la función "delete"

![image](img/Pasted%20image%2020220616162830.png)

Ya casi acabamos, agregaremos una barra de búsqueda, así que vamos a frontpage.html y agreguemos el siguiente div
```
{% block content %}
	<div class="mb-4">
		<form method="get" action=".">
            <input type="text" name="query" placeholder="Search..." class="w-full py-4 px-6 rounded-xl bg-gray-700 text-white">
        </form>
    </div>
```
![image](img/Pasted%20image%2020220616164620.png)

ahora le pondremos su función para buscar, vamos a /core/views.py y agregamos lo siguiente en la función de frontpage(request)

```
query = request.GET.get('query', '')

    if query:
        contacts = contacts.filter(first_name__icontains=query)
```

ahora al buscar algo que contenga first name dentro de los contactos nos arrojara solo ese contacto

![image](img/Pasted%20image%2020220616171708.png)

si queremos hacer lo mismo ya sea con el email, dirección o cualquier otro dato necesitamos un modelo de django llamado Q y lo importamos allí mismo en /core/views.py
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
 y listo, cada que escribamos algo que este contenido en el nombre o apellidos o email, teléfono o cualquier dato aparecerá en nuestra búsqueda

![image](img/Pasted%20image%2020220616173016.png)

ahora podemos agregar lo siguiente justo antes de terminar el bucle for en frontpage.html para que si al buscar no nos arroja ningún resultado salga un mensaje de "No results..."

```
        {% empty %}

            <div class="px-4 py-6 text-center bg-gray-500 rounded-xl">

                <p>No results...</p>

            </div>

        {% endfor %}
```
![image](img/Pasted%20image%2020220616173400.png)

para terminar necesitamos que al momento de ver un contacto nos aparezca su nombre como nombre de la app, así que agregamos el siguiente archivo a /contact/urls.py 

```
from django.urls import path

from . import views

  

app_name='contact'

urlpatterns = [

    path('add/', views.add, name='add'),

    path('contacts/<int:pk>/', views.edit, name='edit'),

    path('contacts/<int:pk>/delete', views.delete, name='delete'),

]
```

y vamos a nuestro archivo /contactmanager/urlp.py y borramos los paths de arriba ya que los utilizaremos aqui y añadiremos el siguiente path y el 'include'
``path('', include('contact.urls')),``  
para que valla y tome esto de nuestra app de contactos, quedando asi:

![image](img/Pasted%20image%2020220616205103.png)

para que funcione solo tenemos que ir a nuestro archivo base.html y modificar donde mandamos a llamar las funciones de add

![image](img/Pasted%20image%2020220616205502.png)

y luego a frontpage, donde también llamamos el edit y delete

![image](img/Pasted%20image%2020220616205607.png)


esto aun no acaba, unas semana después el buen Stain subió una actualización donde añadiremos una sección de log in para poder agregar contactos e implementar o añadir forms de django

Así que para empezar nos dirigiremos a /core/views y definiremos una nueva funcion:

primero empezamos importando la siguiente libreria
``from django.contrib.auth.forms import UserCreationForm``

y luego declaramos nuestra función que servirá para crear ingresar y por el momento le daremos  ``"pass"`` 
```
def signup(request):

    if request.method == 'POST':

        pass

    else:

        form = UserCreationForm

  
    return render(request, 'core/signup.html',{

        'form': form

    })
```

ahora vamos a /core/templates/core para agregar la plantilla que acabamos de declarar en la función signup.html (le agregamos la misma clase al botón de add + para que se vea mejor)

```
{% extends 'core/base.html' %}
  

{% block content %}
	<h1 class="mb-3 text-2xl">Sign up</h1>
    <form method="post" action=".">

        {% csrf_token %}

  
        {{ form.as_p }}
  

        <button class="mt-2 p-3 bg-green-400 text-white text-xl rounded-xl">Submit</button>

    </form>

{% endblock %}
```

ahora para que esta témplate funcione debemos declararla en nuestro archivo /contactmanager/urls.py (el principal), primero lo llamamos en el from core.views y luego añadimos su path

```
from django.contrib import admin

from django.urls import path, include


from core.views import frontpage, signup
  

urlpatterns = [
    path('', frontpage, name='frontpage'),

    path('signup/', signup, name='signup'),

	path('', include('contact.urls')),    
    path('admin/', admin.site.urls),

]
```

ahora vamos a nuestro buscador y ponemos http://127.0.0.1:8000/signup/ y nos deberá salir algo así

[[Pasted image 20220627163826.png]]
![[Pasted image 20220627164014.png]]

ahora si lo llenamos y le damos mandar nos saldrá obviamente un error ya que no hemos creado nuestra form para captar esos datos

![[Pasted image 20220627164129.png]]

así que regresamos a nuestro archivo /contact/views.py y dentro de nuestra función signup agregamos lo siguiente en donde estaba el ``"pass"``  

primero añadimos esta librería 
``from django.contrib.auth import login``

luego añadimos esto
```
def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)


        if form.is_valid():

            user = form.save()
  

            login(request, user)
  

            return redirect('frontpage')

    else:

        form = UserCreationForm

  

    return render(request, 'core/signup.html',{

        'form': form

    })
```

si recargamos y le volvemos a dar los datos nos llevara a la pagina de inicio, ahora pongamos un botón de logout en base.html y modificamos nuestro nav

```
    <nav class="py-6 px-4 bg-gray-900 flex justify-between items-center">

        <a href="{% url 'frontpage' %}" class="text-white text-2xl">Contact Manager</a>

        {% if request.user.is_authenticated %}

            <a href="{% url 'contact:add' %}" class="p-3 bg-green-400 text-white text-xl rounded-xl">+</a>

            <a href="/logout/" class="p-3 bg-green-400 text-white text-xl rounded-xl">Log out</a>

        {% else %}

            <a href="/login/" class="p-3 bg-green-400 text-white text-xl rounded-xl">Log in</a>

            <a href="/signup/" class="p-3 bg-green-400 text-white text-xl rounded-xl">Sign up</a>

        {% endif %}

    </nav>
```

