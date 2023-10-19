"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.Form):

    # def clean(self): 
    #     cleaned_description = int(self.cleaned_data['quantity'])

    #     if not cleaned_description in range(0,51): 
    #         self.add_error('quantity','Quantity must be between 0 and 50 inclusive.')
       

    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length=120,widget=forms.Textarea())
    quantity = forms.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(50)],widget=forms.NumberInput())

       
