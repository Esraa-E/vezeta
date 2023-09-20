from django import forms
from .models import profile , reservation,comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class reservationform(forms.ModelForm):
    class Meta:
        model=reservation
        exclude=['doc']




# class reservform(forms.ModelForm):
#     class Meta:
#         model=reservation
#         fields='__all__'



class mysignup(UserCreationForm):
    first_name=forms.CharField(max_length=15)
    last_name=forms.CharField(max_length=15)
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')



class commentform(forms.ModelForm):
    class Meta:
        model=comment
        exclude=['post']


class proform(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'