import React from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

const CommentBox = () => {
  return (
    <div>
      <Form>
        <Form.Control as="textarea" rows="1" placeholder="Comment" />
        <br />
        <Button>Submit Comment</Button>
      </Form>
    </div>
  );
};

export default CommentBox;
