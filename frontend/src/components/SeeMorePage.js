import React from "react";
import StarButton from "./StarButton.js";
import Image from "react-bootstrap/Image";
import CommentBox from "./CommentBox.js";
import TestImage from "./testimages/testimage.png";

const SeeMorePage = () => {
  return (
    <div className="SeeMorePage">
      <Image variant="top" src={TestImage}/><br/>
        <a href="#usernameprofile">username</a><br/>
      <StarButton />
        <CommentBox /><br/>
        <p>n00b_user: first comment!!!!!</p>
        <p>test123: wow!! such beauty</p>
    </div>
  );
};

export default SeeMorePage;
