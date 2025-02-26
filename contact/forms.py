from django.core.exceptions import ValidationError
from .models import Contact
from django import forms



class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
    ),
    label='Primeiro Nome',
    help_text='Texto de ajuda para seu usuário',
    )


    class Meta():

        model = Contact
        fields = (
             'first_name',
             'last_name',
             'phone'
             )
        
        widgets = {
            
        }
        
    def clean(self):
        #cleaned_data = self.cleaned_data
        self.add_error(
            'first_name', 
            ValidationError('Mensagem de erro', code='invalid')
        )
        self.add_error(
            'first_name',
            ValidationError('Mensagem de erro2', code='invalid')
        )
        return super().clean()