import React from "react";
import Navbar from "react-bootstrap/Navbar";
import SearchBar from "./SearchBar";
import NewPost from "./NewPost.js";
import Link from "react-router-dom/Link";

const NaviBar = () => {
  return (
    <div>
      <Navbar className="LeftAlign">
        <Navbar.Brand href="#home">MSPaintr</Navbar.Brand>
        <br />
        <Navbar.Text>
          Signed in as: <Link to={"/login"}>myusername</Link>
          <br />
          <Link to={"/profile"}>Profile</Link>
          <br />
          <Link to={"/directmessages"}>DMs</Link>
          <br />
          <NewPost />
          <SearchBar />
        </Navbar.Text>
      </Navbar>
      <br />
      <br />
    </div>
  );
};
export default NaviBar;
