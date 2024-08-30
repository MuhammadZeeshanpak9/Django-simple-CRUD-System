from django import forms
from .models import Members  # Use your actual model name

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'