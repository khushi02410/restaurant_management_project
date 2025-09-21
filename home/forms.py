from djanago import forms
from .models import Feedback
from .models import Contact
from utils.validation_utils import is_valid_email

class FeedbackForm(forms.modelForm):
    class M:
        Model = Feedback
        field = ["comments"]
        widgets = {
            "comments": forms.Texrarea(attrs={
                "rows":5,
                "placeholder":"Leave your feedback here"
            })
        }
        labels = {"comments":"your Feedback"}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email", 'message']

class SignupForm(forms.Form):
    email = self.cleaned_data.get("email")
    if not is_valid_email(email):
        raise forms.validateionError("please enter a valid email id address")
    return email        