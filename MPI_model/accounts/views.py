from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from accounts.models import Account
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

#Authen
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    header_str = 'Hello'
    template = loader.get_template('login.html')
    account = Accounts.objects.filter(username='phpond')
    context = {
        'var1': header_str,
        'user': account[0].username
    }
    return HttpResponse(template.render(context, request))

def login_request(request):
    form = AuthenticationForm()
    #request POST
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
