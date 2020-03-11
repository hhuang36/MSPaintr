import React from "react";
import "../App.css";
import SearchBar from "./SearchBar";
import NewPost from "./NewPost.js";


const NaviBar = () => {
  return (
    <div className="LeftAlign">
        <a href="/home">MSPaintr</a>
        <br />
                <a href="/login">Sign in</a>
          <br />
                <a href="/profile">Profile</a>
          <br />
                <a href="/directmessages">DMs</a>
          <br />
          <NewPost />
          <SearchBar />
      <br />
      <br />
    </div>
  );
};
export default NaviBar;
