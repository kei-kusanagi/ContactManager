from django.contrib import admin
from django.urls import path

from core.views import frontpage
from contact import views as contact_views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('add/', contact_views.add, name='add'),
    path('contacts/<int:pk>/', contact_views.edit, name='edit'),
    path('admin/', admin.site.urls),
]
