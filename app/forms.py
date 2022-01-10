from django.forms import ModelForm
# EmailField, DateTimeField, DateTimeInput, Select
from .models import Contact


class ContactForm(ModelForm):
    # email = EmailField(max_length=255, help_text='Bitte eine email eingeben...')

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message', 'phone')