
from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
            required=True,
            widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args,**kwargs)
        self.fields['contact_name'].label = "Votre nom:"
        self.fields['contact_email'].label = "Votre email:"
        self.fields['content'].label = "Contenu:"
