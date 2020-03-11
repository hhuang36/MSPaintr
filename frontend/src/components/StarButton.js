import React from "react";
import Star from "./testimages/upvoteimg.png";

const StarButton = () => {
  function starVote() {
    console.log("+1");
  }
  return (
    <div>
      <button onClick={starVote} size="sm">
        <img src={Star} alt="Star button"/>
      </button>
        <br/>+1
    </div>
  );
};

export default StarButton;
