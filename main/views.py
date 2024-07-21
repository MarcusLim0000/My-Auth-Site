from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import Group
from .forms import RegisterForm
from .models import CustomUser

def home(request):
    return render(request, "main/home.html", {})


def create_user(request):
    user_group = None
    if request.user.groups.filter(name='Head Office').exists():
        user_group = 'Head Office'
    elif request.user.groups.filter(name='District Office').exists():
        user_group = 'District Office'
    elif request.user.groups.filter(name='Branch Office').exists():
        user_group = 'Branch Office'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data.get('group')
            # Below are conditionals to check the group status of the logged in user, and if fails redirects to permission_error.html
            # Check if the user is trying to create a Head Office user without permission
            if group and group.name == 'Head Office' and not request.user.groups.filter(name='Head Office').exists():
                return redirect('permission_error')
            # Check if the user is a Branch Office user
            if request.user.groups.filter(name='Branch Office').exists():
                return redirect('permission_error')
            # Check if a District Office user is trying to create a Head Office or District Office user
            if request.user.groups.filter(name='District Office').exists() and group and group.name in ['Head Office', 'District Office']:
                return redirect('permission_error')
            # Check if a Head Office user is trying to create another Head Office user
            if request.user.groups.filter(name='Head Office').exists() and group and group.name == 'Head Office':
                return redirect('permission_error')

            user = form.save(commit=False)
            user.created_by = request.user.username  # Set the created_by field to the creator's username
            user.save()
            if group:
                user.groups.add(group)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form, 'user_group': user_group})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Automatically assign the "Head Office" group to the new user
            head_office_group = Group.objects.get(name='Head Office')
            user.groups.add(head_office_group)
            auth_login(request, user)  # Logs the user in after registration
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form}) #If authorization fails, redirect to register.html

def view(request):
    # Fetch users created by the logged-in user
    created_users = CustomUser.objects.filter(created_by=request.user.username)
    
    # Check if the user is in the "Branch Office" group
    if request.user.groups.filter(name='Branch Office').exists():
        return render(request, 'main/viewbr.html', {'created_users': created_users})
    
    # Pass the filtered users to the default template
    return render(request, 'main/view.html', {'created_users': created_users})


def user_login(request):
    return render(request, 'main/login.html', {})

def permission_error(request):
    return render(request, "main/permission_error.html")

