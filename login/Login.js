import React from "react";
import "./Login.css";
import { Component } from "react";

function Login() {
  return (
    <div className="Login">
      <h1> Welcome to MSPaintr! </h1>
      <Login_Box />
    </div>
  );
}

class Login_Box extends Component {
  render() {
    return (
      <div className="Login-Box">
        <div className="Logo">
          <EmoteArtist />
        </div>
        <div className="Credentials">
          <form>
            <label>
              Username:
              <input
                id="username"
                type="text"
                name="user"
                placeholder="Enter username..."
              />
            </label>

            <label>
              Password:
              <input
                id="password"
                type="password"
                name="passwd"
                placeholder="Enter password..."
              />
            </label>
          </form>
        </div>

        <div className="Register-Link">
          <a class="active" href="#register">
            Register
          </a>
        </div>
      </div>
    );
  }
}

function EmoteArtist(props) {
  return (
    <p>
      <span role="img" aria-label="artist">
        👩‍🎨
      </span>{" "}
    </p>
  );
}

export default Login;
