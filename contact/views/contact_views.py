from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):

    contacts = Contact.objects.filter(show=True).order_by("-id")[:10]
    
    print(contacts.query)

    return render(
        request, 
        "contact/index.html",
        {"contacts" : contacts}
        )


def contact(request, contact_id):

    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True)
        )
    return render(
        request, 
        "contact/contact.html",
        {"contact" : single_contact}
        )