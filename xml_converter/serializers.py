from rest_framework.serializers import Serializer, FileField

from xml_converter.helpers import validate_file_extension


class UploadSerializer(Serializer):
    xml_file = FileField(validators=[validate_file_extension])

    class Meta:
        fields = ['xml_file']
