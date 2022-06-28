from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.forms import UploadFileForm
from xml_converter.helpers import convert_xml_to_json


def upload_page(request):
    if request.method == "GET":
        return render(request, "upload_page.html")
    elif request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            xml_file = request.FILES.get('xml_file')
            content = xml_file.read()
            json_content = convert_xml_to_json(content)

            if json_content["Root"] in [None, {}]:
                json_content["Root"] = ""
            return JsonResponse(json_content)
        else:
            return JsonResponse({})
