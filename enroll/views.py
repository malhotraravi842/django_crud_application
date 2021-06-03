from enroll.forms import StudentRegistration
from django.shortcuts import render, HttpResponseRedirect
from .models import User

# Function for adding data and showing
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # form.save()

            # Alternative way for getting cleaned data
            roll = form.cleaned_data['roll']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            reg = User(roll=roll, name=name, email=email)
            reg.save()

            # To clean the form after submit
            return HttpResponseRedirect('/')
    else:
        form = StudentRegistration()
    
    stu = User.objects.all()
    return render(request, 'enroll/addAndShow.html', {'form': form, 'stu': stu})


#function for deleting data
def delete_data(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()

        return HttpResponseRedirect('/')


#function for updating data
def update_data(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        user = User.objects.get(pk=id)
        form = StudentRegistration(instance=user)

    return render(request, 'enroll/updateStudent.html', {'form': form})