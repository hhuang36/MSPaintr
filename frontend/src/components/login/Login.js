import React from "react";
import "./Login.css";
import { Component } from "react";

function Login() {
  return (
    <div className="Login">
      <h1 className="LoginH1"> Welcome to MSPaintr! </h1>
      <Login_Box />
    </div>
  );
}

class Login_Box extends Component {
  render() {
    return (
      <div className="Login-Box">
        <div className="LoginLogo">
          <EmoteArtist />
        </div>
        <div className="Credentials">
          <form>
            <label className="LoginLabel">Username:</label>
              <input className="LoginInput"
                id="username"
                type="text"
                name="user"
                placeholder="Enter username..."
              />

            <label className="LoginLabel">Password:</label>
              <input className="LoginInput"
                id="password"
                type="password"
                name="passwd"
                placeholder="Enter password..."
              />
          </form>
        </div>

        <div className="Register-Link">
          <a class="active" href="/register" className="LoginHyperlink">
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
