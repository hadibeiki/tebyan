from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Layout, Column, Submit
from django import forms

from mosqueopinion.models import MmosqueOpinion


class mosqueOpiniojnForm(forms.ModelForm):
    class Meta():
        model = MmosqueOpinion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = True
        self.helper.add_input(Submit('submit', 'ثبت', css_class='btn-primary'))
        self.helper.layout = Layout(
            Div(

                Row(
                    Column('peopleconvidienc', css_class='form-group col-md-3 mb-0'),
                    Column('mosqueconvidient', css_class='form-group col-md-3 mb-0'),

                ),
                Row(
                    Column('backupworker', css_class='form-group col-md-3 mb-0'),
                    Column('backupsolver', css_class='form-group col-md-3 mb-0'),
                    Column('backupaccess', css_class='form-group col-md-3 mb-0'),
                    Column('averagconnect', css_class='form-group col-md-3 mb-0'),
                ),
                Row(

                    Column('youropinion', css_class='form-group col-md-3 mb-0'),
                    Column('yourexprienc', css_class='form-group col-md-3 mb-0'),
                    Column('solver', css_class='form-group col-md-3 mb-0 '),
                    Column('mosquechoices', css_class='form-group col-md-3 mb-0'),
                    Column('paymethod', css_class='form-group col-md-3 mb-0'),

                ),
                Row(
                    Column('description', css_class='form-group col-md-6 mb-0'),
                ),
                css_class='opinionform',
            )
        )
