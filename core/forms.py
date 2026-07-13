from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            "name",
            "phone",
            "email",
            "subject",
            "message"
        ]


        widgets = {

            "name": forms.TextInput(
                attrs={
                    "rows":5,
                    "placeholder":
                    "How can we help you?"
                }
            ),


            "email": forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Email address"
                }
            ),


            "subject": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Subject"
                }
            ),


            "message": forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":5,
                    "placeholder":"Your message"
                }
            )

        }