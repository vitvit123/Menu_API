from django.shortcuts import render
from .models import MenuItem  
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Order
from .models import Order, Customer, MenuItem

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
def notification(request):
    orders = Order.objects.all()
    return render(request, 'notification.html', {'orders': orders})


def get_item_details(request):
    item_id = request.GET.get('item_id')
    try:
        item = get_object_or_404(MenuItem, id=item_id)
        item_details = {
            'item_id': item.id,
            'item_name': item.item_name,
            'description': item.description,
            'price': str(item.price),
            'image': item.image.url if item.image else ''
        }
        return JsonResponse(item_details)
    except MenuItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)
    



def makeorder(request):
    if request.method == 'GET':
        try:
            # Assuming these are GET parameters sent from your JavaScript AJAX request
            customer_id = request.GET.get('userid')  # Assuming userid corresponds to customer id
            menu_item_id = request.GET.get('foodid')
            quantity = int(request.GET.get('qty'))
            total_price = float(request.GET.get('totalprice'))

            # Retrieve Customer and MenuItem instances
            customer = get_object_or_404(Customer, id=customer_id)
            menu_item = get_object_or_404(MenuItem, id=menu_item_id)

            # Create Order instance
            order = Order.objects.create(
                customer=customer,
                menu_item=menu_item,
                quantity=quantity,
                total_price=total_price
            )

            return JsonResponse({'message': 'Order placed successfully.'})
        
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found.'}, status=404)
        
        except MenuItem.DoesNotExist:
            return JsonResponse({'error': 'Menu item not found.'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

