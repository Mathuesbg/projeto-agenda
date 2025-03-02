from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request=request)
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    
    if request.method == "POST":
        form = RegisterUpdateForm(data=request.POST, instance=request.user )
        if form.is_valid():
            form.save()
            messages.success(request=request, message="usuario atualizado com sucesso!")
            return redirect('contact:user_update')
    else:
        form = RegisterUpdateForm(instance=request.user)    
    return render(
        request=request, 
        template_name="contact/user_update.html",
        context = {'form': form}
        )

    