from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ViewSet

from xml_converter.helpers import convert_xml_to_json
from xml_converter.serializers import UploadSerializer


class ConverterViewSet(ViewSet):
    parser_classes = [MultiPartParser]
    serializer_class = UploadSerializer

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        if request.method == 'POST':
            xml_file = request.FILES.get('xml_file')
            content = xml_file.read()
            json_content = convert_xml_to_json(content)

            if json_content["Root"] in [None, {}]:
                json_content["Root"] = ""
        else:
            json_content = {}
        return JsonResponse(json_content)
