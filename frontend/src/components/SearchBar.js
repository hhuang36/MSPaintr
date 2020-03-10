import React from "react";
import Form from "react-bootstrap/Form";

const SearchBar = () => {
  return (
    <Form>
      <Form.Control type="text" rows="2" placeholder="Search" />
    </Form>
  );
};
export default SearchBar;
