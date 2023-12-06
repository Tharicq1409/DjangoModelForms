from django import forms
from .models import user_registration

class user_reg_form(forms.ModelForm):
    class Meta:
        model = user_registration
        fields = '__all__'