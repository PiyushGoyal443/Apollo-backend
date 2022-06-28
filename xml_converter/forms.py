from django import forms

from xml_converter.helpers import validate_file_extension


class UploadFileForm(forms.Form):
    xml_file = forms.FileField(validators=[validate_file_extension])
