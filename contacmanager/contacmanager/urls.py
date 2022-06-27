from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    
    path('signup/', signup, name='signup'),

    path('', include('contact.urls')),    
    
    path('admin/', admin.site.urls),
]
