var messages = document.getElementById("messagesList");
var textbox = document.getElementById("textbox");

textbox.addEventListener("keydown", function(e){
   if(e.keyCode == 13) {
      var newMessage = document.createElement("li");
      newMessage.innerHTML = textbox.value;
      messages.appendChild(newMessage);
      textbox.value = "";
   }

});