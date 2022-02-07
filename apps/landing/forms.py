from django import forms
from apps.landing.models import Contact


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ('name', 'connection', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'connection': forms.TextInput(attrs={'placeholder': 'Ваш email или телефон'}),
            'text': forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'rows':4, 'cols':15}),
        }