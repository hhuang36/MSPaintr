import React from "react";
import ReactDOM from "react-dom";

import DirectMessages from "./DirectMessages";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <React.StrictMode>
    <DirectMessages />
  </React.StrictMode>,
  rootElement
);

//ReactDOM.render(<DirectMessages />, document.getElementById("root"));

var messages = document.getElementById("messagesList");
var textbox = document.getElementById("textbox");
textbox.addEventListener("keydown", function(e) {
  if (e.keyCode === 13) {
    var newMessage = document.createElement("li");
    newMessage.innerHTML = textbox.value;
    messages.appendChild(newMessage);
    textbox.value = "";
  }
});
