from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Layout, Column, Submit
from django import forms

from gallery.models import Mgallery


class galleryForm(forms.ModelForm):
    class Meta():
        model = Mgallery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'ثبت', css_class='btn-s'))
        self.helper.layout = Layout(
            Div(

                Row(
                    Column('mosqe', css_class='form-group col-md-3 mb-0'),
                    Column('mFile', css_class='form-group col-md-3 mb-0'),

                ),
                css_class='mosqueform',
            )
        )
