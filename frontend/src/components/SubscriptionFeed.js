import React from "react";
import Post from "./Post";
import CardColumns from "react-bootstrap/CardColumns";

const SubScriptionFeed = () => {
  return (
    <div className="App">
      <CardColumns>
          <Post />
      </CardColumns>
    </div>
  );
};

export default SubScriptionFeed;
