import React from "react";
import Card from "react-bootstrap/Card";
import StarButton from "./StarButton.js";
import CommentBox from "./CommentBox.js";
import TestImage from "./testimages/testimage.png";
import Link from "react-router-dom/Link";


const Post = (props) =>{
    const { artwork, username, upvotes, comments } = props;

    return (
      <div className="Post">
        <Card>
          <Card.Img variant="top" src={TestImage} style={{ width: "25rem" }} />
          <Card.Body>
              <Card.Title><a href="#usernameprofile">{username}</a></Card.Title>
            <StarButton />
            <CommentBox />
              <Link to={"/more"}>See More</Link>
          </Card.Body>
        </Card>
      </div>
    );
}

Post.defaultProps = {
  artwork: {TestImage},
  username: "username",
  upvotes: 0,
  comments: "None"
};

export default Post;
