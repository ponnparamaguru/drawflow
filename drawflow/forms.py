from django import forms
from .models import Node

class NodeForm(forms.ModelForm):
    image = forms.ImageField(label='Upload Image', required=False)  # No need for choices

    class Meta:
        model = Node
        fields = ['name', 'image', 'no_of_inputs', 'no_of_outputs']
