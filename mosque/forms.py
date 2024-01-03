from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Layout, Column, Submit
from django import forms

from contact.models import Mcontact
from mosque.models import Mmosque


class mosqueForm(forms.ModelForm):
    class Meta():
        model = Mmosque
        fields = '__all__'
        exclude = ('city',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'ثبت', css_class='btn-s'))
        self.helper.layout = Layout(
            Div(

                Row(
                    Column('name', css_class='form-group col-md-2 mb-0'),
                    Column('latitude', css_class='form-group col-md-2 mb-0'),
                    Column('longtude', css_class='form-group col-md-2 mb-0'),
                    Column('price', css_class='form-group col-md-2 mb-0'),
                    Column('sex', css_class='form-group col-md-2 mb-0'),
                    Column('velocity', css_class='form-group col-md-2 mb-0'),

                ),
                Row(
                    Column('startage', css_class='form-group col-md-2 mb-0'),
                    Column('endage', css_class='form-group col-md-2 mb-0 '),
                    Column('phone', css_class='form-group col-md-2 mb-0 '),

                ),
                Row(
                    Column('address', css_class='form-group col-md-6 mb-0'),
                    Column('description', css_class='form-group col-md-6 mb-0'),

                ),
                css_class='mosqueform',
            )
        )
