from django.shortcuts import render, redirect

from .models import Category, Contact

def add(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')

        Contact.objects.create(
            category_id=category_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            zipcode=zipcode,
            city=city,
        )

        return redirect('frontpage')

    categories = Category.objects.all()

    return render(request, 'contact/add.html', {
        'categories': categories
        })