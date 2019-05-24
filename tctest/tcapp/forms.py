from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class InfoForm(UserCreationForm):
    class Meta():
        model = models.User
        fields = ('first_name','last_name','username','email','age','gender','color','password1','password2')
        age = forms.IntegerField()
        COLOR_CHOICES = (
                ('', 'Select a color'),
                ('red', 'red'), #First one is the value of select option and second is the displayed value in option
                ('blue', 'blue'),
                ('green', 'green'),
                ('pink', 'pink'),
                ('orange', 'orange'),
                ('white', 'white'),
                ('black', 'black'),
                )
        widgets = {
            'color': forms.Select(choices=COLOR_CHOICES,attrs={'class': 'form-control'}),
        }
