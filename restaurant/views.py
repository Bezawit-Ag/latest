# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)
def menu(request):
    context={'menu_items':Menu.objects.all()}
    return render(request, 'menu.html', context)
def display(request,pk=None):
    if pk:
        menu_item=Menu.objects.get(pk=pk)
   
    else:
        menu_item=None
    return render(request, 'menu-display.html', {'menu':menu_item})


# Add your code here to create new views