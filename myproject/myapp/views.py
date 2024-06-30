from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')
def Login(request):
    return render(request, 'Login.html')
def Menu(request):
    return render(request, 'Menu.html')
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