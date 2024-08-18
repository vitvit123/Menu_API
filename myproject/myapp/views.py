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
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

def home_page(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    else:
        context['username'] = None
    return render(request, 'index.html', context)
def Login(request):
    return render(request, 'Login.html')

def adminproduct(request):
    store_id = request.COOKIES.get('CustomerID')
    
    if store_id:
        menu_items_list = MenuItem.objects.filter(storeid=store_id)
    else:
        menu_items_list = MenuItem.objects.none()

    paginator = Paginator(menu_items_list, 10)  # Show 10 menu items per page
    page_number = request.GET.get('page')
    menu_items = paginator.get_page(page_number)

    return render(request, 'adminproduct.html', {'menu_items': menu_items})
def success_page(request):
    return render(request, 'success.html')
def paydeli(request, id):
    # Get the specific order or return a 404 if not found
    order = get_object_or_404(Order, id=id)
    
    # Update the paymentmethod field to '1'
    order.paymentmethod = '1'
    order.save()    
    return render(request, 'success.html')
def payment(request):
    customer_id = request.COOKIES.get('CustomerID')

    if customer_id:
        orders = Order.objects.filter(is_completed=False, customer__id=customer_id,paymentmethod__isnull=True)
    else:
        orders = Order.objects.none()

    return render(request, 'payment.html', {'orders': orders})


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
    if not request.COOKIES.get('username'):
        return redirect('http://127.0.0.1:8000/myapp/login/')
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
            response.set_cookie('CustomerID', user.id, expires=make_aware(expiration_time))
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
            customer_id = request.COOKIES.get('CustomerID')
            menu_item_id = request.GET.get('foodid')
            quantity = int(request.GET.get('qty'))
            total_price = float(request.GET.get('totalprice'))

            customer = get_object_or_404(Customer, id=customer_id)
            menu_item = get_object_or_404(MenuItem, id=menu_item_id)

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

            expiration_time = datetime.utcnow() + timedelta(hours=3)
            response = render(request, 'index.html')
            response.set_cookie('username', user.username, expires=make_aware(expiration_time))
            
            return response

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def upload_qrbill(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        uploaded_file = request.FILES['photo']
        
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        order.qrseller = file_url  # Assuming this is the correct field
        order.save()
        
        return render(request, 'success.html')  # Ensure this template exists
    
    return HttpResponse('Invalid request', status=400)
def upload_billPayment(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        uploaded_file = request.FILES.get('image')  # Ensure you use the correct field name
        
        if uploaded_file:
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            
            order.paymentbill = file_url  # Assuming this is the correct field
            order.save()
            
            return render(request, 'success.html')  # Ensure this template exists
        
        return HttpResponse('No file uploaded', status=400)
    
    return HttpResponse('Invalid request', status=400)

def delete_menu_item(request, id):
    menu_item = get_object_or_404(MenuItem, id=id)

    menu_item.delete()    
    store_id = request.COOKIES.get('storeID')
    
    if store_id:
        menu_items_list = MenuItem.objects.filter(storeid=store_id)
    else:
        menu_items_list = MenuItem.objects.none()

    paginator = Paginator(menu_items_list, 10)  # Show 10 menu items per page
    page_number = request.GET.get('page')
    menu_items = paginator.get_page(page_number)

    return render(request, 'adminproduct.html', {'menu_items': menu_items})
from django.shortcuts import render, redirect
from .models import MenuItem

def additem(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')  # Get the uploaded image

        # Retrieve storeid from cookies
        store_id = request.COOKIES.get('CustomerID', 'default_value')

        # Create and save the MenuItem instance
        new_item = MenuItem(
            item_name=item_name,
            description=description,
            price=price,
            image=image,  # Use the uploaded image
            storeid=store_id
        )
        new_item.save()

        return redirect('adminproduct')

    return render(request, 'admin_add_item.html')

def adminprofile(request):
    superusers = User.objects.filter(is_superuser=True).select_related('customer')
    
    context = {
        'superusers': superusers
    }

    # Pass the user data to the template
    return render(request, 'adminprofile.html', {'customer': superusers})