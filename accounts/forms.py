from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

Gender = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('Other', 'Other'),
    ('NA', 'Prefer not to say'),
)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    age = forms.IntegerField(required=False)
    gender = forms.ChoiceField(choices=Gender)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'age', 'gender', 'email', 'password1', 'password2', )