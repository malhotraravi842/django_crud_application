from enroll.forms import StudentRegistration
from django.shortcuts import render
from .models import User

def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # Alternative way for getting cleaned data

            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # reg = User(name=name, email=email, password=password)
            # reg.save()
            
            form.save()
            # To clean the form after submit
            form = StudentRegistration()
    else:
        form = StudentRegistration()

    return render(request, 'enroll/addAndShow.html', {'form': form})
