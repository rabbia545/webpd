from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    interest = Interests.objects.all().order_by('?')[0:12]
    testmonials = Testmonials.objects.all()
    service = Services.objects.all()[0:3]
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'form':form,
        'testmonials':testmonials,
        'service':service,
        'interest':interest,
    }
    return render(request,'temp_app/index.html', context)