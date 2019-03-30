from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    # Define fields here if you want custom validation
    # ie. FirstName = forms.Charfield(blah blah blah)
    class Meta():
        model = User
        fields = '__all__'