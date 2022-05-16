from django.forms import ModelForm
from .models import Input


class InputForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(InputForm, self).__init__(*args, **kwargs)
    #     self.fields['translated_code'].disabled = True

    class Meta:
        model = Input

        fields = ['source_language', 'source_code', 'target_language', 'translated_code']