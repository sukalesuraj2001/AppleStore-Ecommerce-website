from django import forms
from ecomapp.models import Apple_Product
from django.contrib.auth.forms import UserCreationForm
# for inhritance
from django.contrib.auth.models import User


class EmpForm(forms.Form):
    name=forms.CharField(max_length=50)
    dept=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    salary=forms.FloatField()


class Apple_ProductModelForm(forms.ModelForm):
    name=forms.CharField()
    cat=forms.IntegerField()
    price=forms.FloatField()
    status=forms.BooleanField()
    pimage=forms.ImageField()

    class Meta:
        model=Apple_Product
        fields=['name','cat','price','status','pimage']


class UserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

