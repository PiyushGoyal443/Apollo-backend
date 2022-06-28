import os

import xmltodict
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xml']
    if not (ext in valid_extensions):
        raise ValidationError(u'File not supported!')


def convert_xml_to_json(content):
    data_dict = xmltodict.parse(content)
    return data_dict
