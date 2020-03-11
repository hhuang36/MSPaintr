import React from "react";
import Form from "react-bootstrap/Form";

const CommentBox = () => {
  return (
    <div>
      <Form>
        <Form.Control as="textarea" rows="1" placeholder="Comment" />
        <br />
        <button>Submit Comment</button>
      </Form>
    </div>
  );
};

export default CommentBox;
