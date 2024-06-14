from django import forms

class ConfirmReservationForm(forms.Form):
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=16)
    birth_day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))