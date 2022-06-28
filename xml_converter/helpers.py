import os

import xmltodict
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xml']
    if not (ext in valid_extensions):
        raise ValidationError(u'File not supported!')


def parse(dict_obj):
    if isinstance(dict_obj, dict):
        new_list = []
        for k, v in dict_obj.items():
            if isinstance(v, dict):
                new_list.append({k: parse(v)})
            elif isinstance(v, list):
                for i in v:
                    new_list.append({k: parse(i)})
            else:
                new_list.append({k: v})
        return new_list


def convert_xml_to_json(content):
    data_dict = xmltodict.parse(content)
    data_dict = parse(data_dict["Root"])
    return {"Root": data_dict}
