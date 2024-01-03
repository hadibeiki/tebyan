from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Layout, Column
from django import forms

from contact.models import Mcontact


class registerForm(forms.ModelForm):
    class Meta():
        model = Mcontact
        fields = '__all__'
        exclude = ('mobile','price','birthday','otp','otpcreatedtime',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Div(

                Row(
                    Column('name', css_class='form-group col-md-3 mb-0'),
                    Column('family', css_class='form-group col-md-3 mb-0'),
                    Column('melicode', css_class='form-group col-md-3 mb-0'),
                    Column('dad', css_class='form-group col-md-3 mb-0'),
                    Column('education', css_class='form-group col-md-3 mb-0'),
                    Column('marital', css_class='form-group col-md-3 mb-0'),

                ),
                Row(
                    Column('age', css_class='form-group col-md-3 mb-0 changerow'),
                    Column('sex', css_class='form-group col-md-3 mb-0 '),
                    Column('city', css_class='form-group col-md-3 mb-0'),

                ),
                css_class='signupform',
            )
        )
