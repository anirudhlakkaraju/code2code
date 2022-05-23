from django.forms import ModelForm
from .models import Input
from django_ace import AceWidget

class InputForm(ModelForm):

    class Meta:

        # Model from which forms' fields are from
        model = Input

        # Adding ACE editor 
        # widgets = {
        #     'source_code': AceWidget(mode="python", theme="twilight"),
        #     'translated_code': AceWidget(mode="python", theme="chrome"),
        # }

        # The fields to include from Input model
        fields = ['source_language', 'source_code', 'target_language', 'translated_code']