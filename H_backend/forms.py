from django import forms
from .models import NewAllPlant, NewPlant

class PlantForm(forms.ModelForm):
    class Meta:
        model = NewAllPlant
        fields = ['name', 'image', 'scientific_name', 'family', 'genus', 'species', 'location', 'collection_date', 'collector', 'classification']

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class NewPlantForm(forms.ModelForm):
    class Meta:
        model = NewPlant
        fields = ['name', 'image', 'description', 'family', 'type']

class NewImageUploadForm(forms.Form):
    image = forms.ImageField()

class PlantSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    family = forms.CharField(max_length=100, required=False)
    locality = forms.CharField(max_length=100, required=False)
    collector = forms.CharField(max_length=100, required=False)
    collection_date = forms.DateField(required=False)