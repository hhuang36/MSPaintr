import React from "react";
import "./DirectMessages.css";
import { Component } from "react";

function DirectMessages() {
  return (
    <div className="DirectMessages">
      <h1 className="DMsH1">My DM's</h1>
      <SideBar />
      <ChatBox />
    </div>
  );
}

class SideBar extends React.Component {
  x = 420;
  render() {
    return (
      <div className="DM-Side-Bar">
        <form>
          <input className="DMInput" type="text" name="name" placeholder="   Search username..." />
        </form>
        <ul className="messagesDisplay" id="messagesdisplay">
          <li className="DMLi">
            {" "}
            <EmotePalette /> hhuang36
          </li>
          <li className="DMLi">
            {" "}
            <EmotePalette /> miaencar
          </li>
          <li className="DMLi">
            {" "}
            <EmotePalette /> vjvitale
          </li>
          <li className="DMLi">
            {" "}
            <EmotePalette /> Jesse{" "}
          </li>
          <li className="DMLi">
            {" "}
            <EmotePalette /> Nick{" "}
          </li>
        </ul>
      </div>
    );
  }
}

class ChatBox extends React.Component {
  render() {
    return (
      <div className="Chat-Box" id="chat">
        <ul class="messagesList" id="messagesList" />
        <form>
          <label>
            <EmotePaintbrush />
            <input className="DMInput"
              id="textbox"
              type="text"
              name="message"
              placeholder="  Enter Message..."
            />
          </label>
        </form>
      </div>
    );
  }
}

function EmotePaintbrush(props) {
  return (
    <p>
      <span role="img" aria-label="paintbrush">
        🖌️
      </span>{" "}
    </p>
  );
}

function EmotePalette(props) {
  return (
    <p>
      <span role="img" aria-label="palette">
        🎨
      </span>{" "}
    </p>
  );
}

export default DirectMessages;
