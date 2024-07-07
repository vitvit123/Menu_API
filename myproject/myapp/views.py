from django.shortcuts import render
from .models import MenuItem  
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


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
def register(request):
    return render(request, 'register.html')

def get_item_details(request):
    item_id = request.GET.get('item_id')
    try:
        item = get_object_or_404(MenuItem, id=item_id)
        item_details = {
            'item_name': item.item_name,
            'description': item.description,
            'price': str(item.price),
            'image': item.image.url if item.image else ''
        }
        return JsonResponse(item_details)
    except MenuItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)