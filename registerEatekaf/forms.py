from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Layout, Column
from django import forms

from registerEatekaf.models import Mregistereatekaf


class registereatekafform(forms.ModelForm):
    class Meta():
        model = Mregistereatekaf
        fields = '__all__'

