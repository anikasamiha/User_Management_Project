from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParentForm, ChildForm #, AddressForm
from .models import Address, Parent, Child

# Create your views here.
def home(request):
    return render(request, 'family_register/home.html', {})

##For Parents##
def parent_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = ParentForm()
        else:
            parent = Parent.objects.get(pk=id)
            form = ParentForm(instance=parent)
        heading = 'Create Parent'
        context = {'form': form, 'heading': heading}
        return render(request, 'family_register/parent_form.html', context)

    elif request.method == 'POST':
        if id==0:
            form = ParentForm(request.POST)
        else:
            parent = Parent.objects.get(pk=id)
            form = ParentForm(request.POST, instance=parent)
        heading = 'Create Child'
        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()

            form.save_m2m()

            parent = form.cleaned_data.get('first_name', 'last_name')
            messages.success(request, 'Parent  was created for ' + parent + '.')
            return redirect('/parent-list/')

    context = {'form': form, 'heading': heading}
    return render(request, 'family_register/parent_form.html', context)

def parent_list(request):
    context = {'parent_list': Parent.objects.all()}
    return render(request, 'family_register/parent_list.html', context)

def parent_delete(request, id):
    parent = Parent.objects.get(pk=id)
    parent.delete()
    return redirect('/parent-list/')


##For Chlildren##

#chlidren get created and updated here
def child_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = ChildForm()
        else:
            child = Child.objects.get(pk=id)
            form = ChildForm(instance=child)
        heading = 'Create Child'
        context = {'form': form, 'heading': heading}
        return render(request, 'family_register/child_form.html', context)

    elif request.method == 'POST':
        if id==0:
            form = ChildForm(request.POST)
        else:
            child = Child.objects.get(pk=id)
            form = ChildForm(request.POST, instance=child)
            #form = ParentForm(request.POST, instance=parent)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()

            form.save_m2m()

            child = form.cleaned_data.get('first_name', 'last_name')
            messages.success(request, 'Child  was created for ' + child + '.')
            return redirect('/child-list/')
    heading = 'Create Child'
    context = {'form': form, 'heading': heading}
    return render(request, 'family_register/child_form.html', context)

def child_list(request):
    context = {'child_list': Child.objects.all()}
    return render(request, 'family_register/child_list.html', context)

def child_delete(request, id):
    child = Child.objects.get(pk=id)
    child.delete()
    return redirect('/child-list/')
    

