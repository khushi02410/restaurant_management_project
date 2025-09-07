from djanago import forms
from .models import Feedback
from .models import Contact

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