from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):

    contacts = Contact.objects.filter(show=True).order_by("-id")[:10]
    
    print(contacts.query)

    return render(
        request=request, 
        template_name="contact/index.html",
        context={"contacts" : contacts, "title": 'Contatos -'}
        )


def contact(request, contact_id):

    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True)
        )
    title = f"{single_contact.first_name } {single_contact.last_name} -"
    return render(
        request = request, 
        template_name="contact/contact.html",
        context={
            "contact" : single_contact, 
            "title": title}
        )