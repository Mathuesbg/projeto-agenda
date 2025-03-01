from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm

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