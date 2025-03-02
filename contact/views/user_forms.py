from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm



def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        context = {
            'form': form,
            }
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Usuario registrado")
            return redirect("contact:index")

    context = {'form': form}

    return render(
        request=request, 
        template_name="contact/register.html",
        context = context
        )


def login_view(request):

    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request=request, user=user)
            messages.success(request=request, message="Logado com sucesso!")
            return redirect('contact:index')
        messages.error(request=request, message="Login invalido!")

    context = {'form': form}

    return render(
        request=request, 
        template_name="contact/login.html",
        context = context
        )


def logout_view(request):
    auth.logout(request=request)
    return redirect('contact:login')

