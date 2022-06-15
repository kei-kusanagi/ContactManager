from django.contrib import admin
from django.urls import path

from core.views import frontpage
from contact import views as contact_views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('add/', contact_views.add, name='add'),
    path('admin/', admin.site.urls),
]
