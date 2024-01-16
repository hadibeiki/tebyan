from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Layout, Column
from django import forms

from ability.models import Mability


class abilityForm(forms.ModelForm):
    class Meta():
        model = Mability
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Div(

                Row(
                    Column('photo', css_class='form-group col-md-3 mb-0'),
                    Column('editor', css_class='form-group col-md-3 mb-0'),
                    Column('camera', css_class='form-group col-md-3 mb-0'),
                    Column('news', css_class='form-group col-md-3 mb-0'),
                ),
                Row(
                    Column('madah', css_class='form-group col-md-3 mb-0'),
                    Column('adv', css_class='form-group col-md-3 mb-0 '),
                    Column('backup', css_class='form-group col-md-3 mb-0'),
                    Column('engine', css_class='form-group col-md-3 mb-0'),
                ),
                Row(
                    Column('adminis', css_class='form-group col-md-3 mb-0'),
                    Column('poemer', css_class='form-group col-md-3 mb-0'),
                    Column('teach', css_class='form-group col-md-3 mb-0 '),
                    Column('child', css_class='form-group col-md-3 mb-0 '),
                ),
                Row(
                    Column('writer', css_class='form-group col-md-3 mb-0'),
                ),
                css_class='signupform',
            )
        )
