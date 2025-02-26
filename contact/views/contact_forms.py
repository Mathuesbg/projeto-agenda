from django.shortcuts import render
from contact.forms import ContactForm


def create(request):

    if request.method == "POST":
        context = {"form" : ContactForm(request.POST)}

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