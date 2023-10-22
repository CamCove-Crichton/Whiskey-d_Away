# Assistance from CI - Boutique Ado walkthrough
from django import forms
from .models import Tours, Category
from .widgets import CustomClearableFileInput


class ToursForm(forms.ModelForm):
    """
    A form for admin users to add, view
    and edit tour experiences
    """
    class Meta:
        model = Tours
        fields = '__all__'
    
    tour_image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['tour_category'].choices = friendly_names
        for field_name, field in self.fields.items():
            # set the label class
            field.label_classes = ['text-yellow']

            # set the class for the input
            field.widget.attrs['class'] = 'rounded-2'