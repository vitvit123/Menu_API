from django.shortcuts import render
from .models import MenuItem  
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Order
from .models import Order, Customer, MenuItem
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.utils.timezone import make_aware
from datetime import datetime, timedelta





def home_page(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    else:
        context['username'] = None
    return render(request, 'index.html', context)
def Login(request):
    return render(request, 'Login.html')
def product_Admin(request):
    return render(request, 'product_admin.html')

def Menu(request, storeid):
    # Filter menu items based on storeid
    menu_items = MenuItem.objects.filter(storeid=storeid) if storeid else MenuItem.objects.none()

    # Render response and set cookie if storeid is provided
    response = render(request, 'Menu.html', {
        'menu_items': menu_items,
        'storeid': storeid
    })

    if storeid:
        response.set_cookie('storeID', str(storeid))

    return response
def News(request):
    return render(request, 'News.html')
def main(request):
    superusers = User.objects.filter(is_superuser=True).select_related('customer')
    
    context = {
        'superusers': superusers
    }
    return render(request, 'MainPage.html', context)

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
    orders = Order.objects.filter(is_completed=False)
    return render(request, 'notification.html', {'orders': orders})

def get_notification_count(request):
    count = Order.objects.filter(is_completed=False).count()
    return JsonResponse({'count': count})

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
    
def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            # Set cookie to expire in 3 hours
            expiration_time = datetime.utcnow() + timedelta(hours=3)
            response = redirect('myapp:home')
            response.set_cookie('username', user.username, expires=make_aware(expiration_time))
            return response
        else:
            return render(request, 'Login.html', {'error': 'Invalid email or password'})

    return render(request, 'Login.html')
def logout(request):
    auth_logout(request)  # Log out the user
    response = redirect('myapp:home')
    
    # Delete the username cookie
    response.delete_cookie('username')
    response.delete_cookie('storeID')

    
    return response


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


def mark_order_completed(request):
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        order.is_completed = True
        order.save()
        return JsonResponse({'success': True})

def get_notification_count():
        return Order.objects.count()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Set cookie to expire in 3 hours
            expiration_time = datetime.utcnow() + timedelta(hours=3)
            response = render(request, 'index.html')
            response.set_cookie('username', user.username, expires=make_aware(expiration_time))
            
            return response

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})





