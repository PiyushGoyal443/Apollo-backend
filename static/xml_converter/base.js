function makeRequest(input) {
  let formData = new FormData();
  if (input.files.length > 0) {
    formData.append("xml_file", input.files[0]);
    formData.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').attr('value'));
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });
    var json = JSON.stringify(object);
    console.log(json);


    fetch("/connected/", { method: "POST", body: formData })
    .then((response) => response.json())
    .then(function (data) {
    console.log(data);
      $('.xml-upload-wrap').hide();
      $('.file-upload-content').show();
      _json = JSON.stringify(data, undefined, 4);
      $('.xml-to-json-result').html(_json);
    })
    .catch(function (error) {
      // If there is any error you will catch them here
      console.log(error);
    });
  }
}

function removeUpload() {
  $(".file-upload-input").replaceWith($(".file-upload-input").clone());
  $(".file-upload-content").hide();
  $(".xml-upload-wrap").show();
}
$(document).ready(function () {
  $(".xml-upload-wrap").bind("dragover", function () {
    $(".xml-upload-wrap").addClass("xml-dropping");
  });

  $(".xml-upload-wrap").bind("dragleave", function () {
    $(".xml-upload-wrap").removeClass("xml-dropping");
  });
});