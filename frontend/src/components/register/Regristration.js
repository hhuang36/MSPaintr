import React, {Component} from 'react';
import './Regristration.css';

function Regristration() {
  return (
    <div className="Regristration">
      <h1 className="Registration-Heading1">Regristration</h1>
      <br/>
      <br/>
      <RegForm/>
    </div>
  );
}


class RegForm extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      user_name: '',
      password: '',
    };

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleSubmit(event){
    this.setState({user_name: event.target.user_name, password: event.target.password})
  }

  handleChange(event){
    console.log('User Name: ' + this.state.user_name + ' Password: ' + this.state.password)
    event.preventDefault();
  }

  render(){
    return(
      <form onSubmit={this.handleSubmit}>
        <label>
          User Name:
          <input type ="text" user_name={this.state.user_name} onChange={this.handleChange} />
        </label>
        <br/>
        <br/>
        <label>
          Password:
          <input type="text" password={this.state.password} onChange={this.handleChange} />
        </label>
        <br/>
        <br/>
        <input type ="submit" value="Register"/>
      </form>
      )
  }
}

export default Regristration;