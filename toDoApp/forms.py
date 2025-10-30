from django import forms
from .models import Tache

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['tache']
        widgets = {
            'tache': forms.TextInput(attrs={
                'class': 'border-2 w-[100%] mb-[20px] focus:border-white bg-gradient-to-r from-[var(--bodyColor)] to-white h-[35px] rounded-[10px] px-[10px] py-[5px]',
                'placeholder': 'Ex: I will range my choose',
            }),
        }
