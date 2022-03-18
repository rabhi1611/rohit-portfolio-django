from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
# Create your views here.
from .forms import create_person_form

def home(request):
    form = create_person_form()

    if request.method == 'POST':
        form = create_person_form(request.POST)
        #print(form.cleaned_data['Name'])
        if form.is_valid():
            form.save()
            return redirect('success')
    
    context = {
        'form': form
    }
    return render(request, 'rohit/index.html', context)


def success(request):
    return render(request, 'rohit/success.html', {})