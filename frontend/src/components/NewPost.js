import React from "react";
import Modal from "react-bootstrap/Modal";

const NewPost = () => {
  const [show, setShow] = React.useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  return (
    <>
      <button variant="primary" onClick={handleShow}>
        New Post
      </button>

      <Modal
          show={show}
          onHide={handleClose}
          size="lg"
          centered>
        <Modal.Header closeButton>
          <Modal.Title>Create a New Post</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Upload your artwork!
          <br />
          <input type="file" accept="image/png" />
        </Modal.Body>
        <Modal.Footer>
          <button variant="secondary" onClick={handleClose}>
            Cancel
          </button>
          <button variant="primary" onClick={handleClose}>
            Post
          </button>
        </Modal.Footer>
      </Modal>
    </>
  );
};
export default NewPost;
