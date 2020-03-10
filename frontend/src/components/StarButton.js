import React from "react";
import Button from "react-bootstrap/Button";
import Image from "react-bootstrap/Image";
import Star from "./testimages/upvoteimg.png";

const StarButton = () => {
  function starVote() {
    console.log("+1");
  }
  return (
    <div>
      <Button onClick={starVote} size="sm">
        <Image src={Star} />
      </Button>
        <br/>+1
    </div>
  );
};

export default StarButton;
