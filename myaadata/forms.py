from django import forms
from django.forms import ModelForm
from myaadata.models import CBCresults

from django.forms import formset_factory, modelformset_factory



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
# class CBCform(forms.Form):
#     class meta:
#         model = CBCresults
#         fields = ('Date', 'HCT_percent', 'Hgb', 'MCV', 'NRBC', 'Platelets', 'RBCs', 'RDW_RBC_percent', 'WBC')
#         widgets = {
#             'Date': forms.DateInput(attrs={'required': True,'class':'datepicker form-control-lg', 'autocomplete':'off'}),
#             'HCT_percent': forms.NumberInput(attrs={'class':'form-control'}),
#             'Hgb': forms.NumberInput(attrs={'class':'form-control'}),
#             'MCV': forms.NumberInput(attrs={'class':'form-control'}),
#             'NRBC': forms.NumberInput(attrs={'class':'form-control'}),
#             'Platelets': forms.NumberInput(attrs={'class':'form-control'}),
#             'RBCs': forms.NumberInput(attrs={'class':'form-control'}),
#             'RDW_RBC_percent': forms.NumberInput(attrs={'class':'form-control'}),
#             'WBC': forms.NumberInput(attrs={'class':'form-control'}),
#         }

class CBCform(forms.Form):
    Date = forms.DateInput(attrs={'required': True,'class':'datepicker form-control-lg', 'autocomplete':'off'})
    HCT_percent = forms.NumberInput(attrs={'class':'form-control'})
    Hgb = forms.NumberInput(attrs={'class':'form-control'})
    MCV = forms.NumberInput(attrs={'class':'form-control'})
    NRBC = forms.NumberInput(attrs={'class':'form-control'})
    Platelets = forms.NumberInput(attrs={'class':'form-control'})
    RBCs = forms.NumberInput(attrs={'class':'form-control'})
    RDW_RBC_percent = forms.NumberInput(attrs={'class':'form-control'})
    WBC = forms.NumberInput(attrs={'class':'form-control'})