from .models import User
from django import forms


class studentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(render_value=True, attrs={
                'class': 'form-control'
            })
        }
