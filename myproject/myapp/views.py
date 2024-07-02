from django.shortcuts import render
from .models import MenuItem  


def home_page(request):
    return render(request, 'index.html')
def Login(request):
    return render(request, 'Login.html')

def Menu(request):
    # Fetch all MenuItem objects from the database
    menu_items = MenuItem.objects.all()
    
    # Pass menu_items to the template context
    context = {
        'menu_items': menu_items
    }
    
    return render(request, 'Menu.html', context)
def News(request):
    return render(request, 'News.html')
def Dish(request):
    return render(request, 'dish.html')
def Contact(request):
    return render(request, 'Contact.html')
def Admin(request):
    return render(request, 'admin.html')
def About(request):
    return render(request, 'about.html')