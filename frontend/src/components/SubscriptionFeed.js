import React from "react";
import "../App.css";
import Post from "./Post";
import CardColumns from "react-bootstrap/CardColumns";

const SubscriptionFeed = () => {
  return (
    <div className="SubscriptionFeed">
      <CardColumns>
          <Post />
          <Post />
      </CardColumns>
    </div>
  );
};

export default SubscriptionFeed;
