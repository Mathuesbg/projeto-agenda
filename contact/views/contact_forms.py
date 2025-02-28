from django.shortcuts import render, redirect
from contact.forms import ContactForm


def create(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {"form" : form}

        if form.is_valid():
            form.save()
            return redirect('contact:create')
        
        return render(
            request=request, 
            template_name="contact/create.html",
            context=context
        )

    context = {"form" : ContactForm()}

    return render(
            request=request, 
            template_name="contact/create.html",
            context=context
        )