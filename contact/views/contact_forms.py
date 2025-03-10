from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            "form" : form,
            "form_action" : form_action
            }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(
                request=request,
                message="Contato criado com sucesso!"
                )
            return redirect('contact:contact', contact_id = contact.id)
        
        return render(
            request=request, 
            template_name="contact/create.html",
            context=context
        )

    context = {
            "form" : ContactForm(),
            "form_action" : form_action
            }

    return render(
            request=request, 
            template_name="contact/create.html",
            context=context
        )


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        klass=Contact, 
        pk = contact_id, 
        show=True, 
        owner=request.user)
    
    form_action = reverse('contact:update', args=(contact_id,))
   
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            "form" : form,
            "form_action" : form_action
            }

        if form.is_valid():
            contact = form.save()
            messages.success(
                request=request,
                message="Contato atualizado com sucesso!"
                )
            return redirect('contact:contact', contact_id = contact.pk)
        
        return render(
            request=request, 
            template_name="contact/create.html",
            context=context
        )

    context = {"form" : ContactForm(instance=contact), "form_action" : form_action}

    return render(
            request=request, 
            template_name="contact/create.html",
            context=context
        )


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, owner=request.user)
    confirmation = request.POST.get('confirmation', 'no')
    print("confirmation", confirmation)

    if confirmation == 'yes':
        contact.delete()
        messages.success(
                request=request,
                message="Contato deletado com sucesso!"
                )
        return redirect('contact:index')
    
    context = {
        "contact" : contact,
        "confirmation" : confirmation
    }
    


    return render(
        request=request,
        template_name= "contact/contact.html",
        context=context
        )