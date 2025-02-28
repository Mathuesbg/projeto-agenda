from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q



def index(request):

    contacts = Contact.objects.filter(show=True).order_by("-id")
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    

    return render(
        request=request, 
        template_name="contact/index.html",
        context={
            "page_objects" : page_object,
            "title": 'Contatos -'}
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


def search(request):
    search_values = request.GET.get('q', '').strip()

    if search_values == '':
        return redirect('index')
    

    contacts = Contact.objects.filter(
            Q(first_name__icontains=search_values)| 
            Q(last_name__icontains=search_values)|  
            Q(phone__icontains=search_values)| 
            Q(email__icontains=search_values),
            show=True, 
            ).order_by("-id")
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(
        request=request, 
        template_name="contact/index.html",
        context={
            "page_objects" : page_object,
            "title": 'Contatos -',
            }
        )
