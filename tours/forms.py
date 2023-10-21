# Assistance from CI - Boutique Ado walkthrough
from django import forms
from .models import Tours, Category


class ToursForm(forms.ModelForm):
    """
    A form for admin users to add, view
    and edit tour experiences
    """
    class Meta:
        model = Tours
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_names()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-2'