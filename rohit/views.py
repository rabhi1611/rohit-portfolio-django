from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, response

from rohit import models
# Create your views here.
from .forms import create_person_form



def home(request):
    form = create_person_form()

    if request.method == 'POST':
        form = create_person_form(request.POST)
        #print(form.cleaned_data['Name'])
        if form.is_valid():
            form.save()
            return redirect('success', form.instance.id)
    
    context = {
        'form': form
    }
    return render(request, 'rohit/index.html', context)


def success(request, pk):
    obj = models.Person.objects.get(pk=pk)
    context = {
        'name': obj.name
    }
    return render(request, 'rohit/success.html', context)