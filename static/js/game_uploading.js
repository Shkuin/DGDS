document.getElementById("upload-button").addEventListener("click", function() {
    var files = document.getElementById("game-files-upload").files;
    
    var formData = new FormData();
    for (var i = 0; i < files.length; i++) {
      formData.append("game_files", files[i]);
    }
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/upload-folder/", true);
    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
    
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // Handle the server response
        console.log(xhr.responseText);
      }
    };
    
    xhr.send(formData);
  });