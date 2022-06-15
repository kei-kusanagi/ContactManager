from django.shortcuts import render

from contact.models import Contact

def frontpage(request):
    contacts = Contact.objects.all()

    return render(request, 'core/frontpage.html', {
        'contacts': contacts
    })