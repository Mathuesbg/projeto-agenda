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
             'phone',
             'email',
             'description',
             'category'
             )
        
        widgets = {
            
        }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    

    def clean_first_name(self):
        first_name= self.cleaned_data.get('first_name')
        if first_name == "ABC":
            self.add_error(
            'first_name', 
            ValidationError('Nao digite ABC neste campo (add_error)', code='invalid')
        )
        return first_name