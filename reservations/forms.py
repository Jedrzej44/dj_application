from django import forms
from django.core.exceptions import ValidationError
from datetime import date


class ConfirmReservationForm(forms.Form):
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=16)
    #start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birth_day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    """def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("Fill reservation dates properly!")

        return cleaned_date"""

    def clean_birth_day(self):
        birth_day = self.cleaned_data['birth_day']
        today = date.today()
        age = today.year - birth_day.year - ((today.month, today.day) < (birth_day.month, birth_day.day))

        if age < 18:
            raise ValidationError("You must be at least 18 years old to reserve a car")
        return birth_day
class CarFilterForm(forms.Form):
    car_type = forms.ChoiceField(choices=[("None", "All"), ("SUV", "SUV"), ("SPORT", "Sport"), ("STANDARD", "Standard")], required=False)
    color = forms.ChoiceField(choices=[("None", "All"), ("BLACK", "Black"), ("WHITE", "White"), ("RED", "Red"), ("GRAPHITE", "Graphite")], required=False)
    seats = forms.IntegerField(min_value=1, required=False)
    price_per_day = forms.DecimalField(required=False)


