import React from "react";
import "./DirectMessages.css";
import { Component } from "react";

function DirectMessages() {
  return (
    <div className="App">
      <Nav_Bar />
      <h1>My DM's</h1>
      <Side_Bar />
      <Chat_Box />
    </div>
  );
}

class Nav_Bar extends React.Component {
  render() {
    return (
      <div className="Nav-Bar">
        <a class="active" href="#home">
          Home
        </a>
        &nbsp;
        <a href="#profile">My Profile</a>
        &nbsp;
        <a href="#about"> About</a>
      </div>
    );
  }
}

class Side_Bar extends React.Component {
  x = 420;
  render() {
    return (
      <div className="DM-Side-Bar">
        <form>
          <input type="text" name="name" placeholder="   Search username..." />
        </form>
        <ul id="messagesdisplay">
          <li>
            {" "}
            <EmotePalette /> hhuang36
          </li>
          <li>
            {" "}
            <EmotePalette /> miaencar
          </li>
          <li>
            {" "}
            <EmotePalette /> vjvitale
          </li>
          <li>
            {" "}
            <EmotePalette /> Jesse{" "}
          </li>
          <li>
            {" "}
            <EmotePalette /> Nick{" "}
          </li>
        </ul>
      </div>
    );
  }
}

class Chat_Box extends React.Component {
  render() {
    return (
      <div className="Chat-Box" id="chat">
        <ul class="messagesList" id="messagesList" />
        <form>
          <label>
            <EmotePaintbrush />
            <input
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
