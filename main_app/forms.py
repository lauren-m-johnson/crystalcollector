from django.forms import ModelForm
from .models import Aquired

class AquiredForm(ModelForm):
    class Meta:
        model = Aquired
        fields = ['date', 'location']