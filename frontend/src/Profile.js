import React, {Component} from 'react';
import './Profile.css';
import profPic from "./subtle lgbt.png"
import img1 from "./Disc Emote - Janna.png"
import img2 from "./misty boi.png"
import img3 from "./eggie.png"
import logo from "./MSPaintRLogo.png"

function Profile() {
  return (
    <div className="App">
      <img className="logo" src={logo}/>
      <Side_Bio/>
      <div className="App-Posts">
          <Posts/>
        </div>
    </div>
  );
}

class Side_Bio extends React.Component{
  x=420
  render(){
    return(
        <div className="Profile-Side">
          <SimpleMessage body="xX_lucid_Xx"/>
          <br/>
          <Prof_Pic imgName={profPic}/>
          <br/>
          <button> <EmoteMail/> </button>
          <span>&nbsp;</span>
          <button> <EmoteSheep count = {this.x}/> </button>
          <br/>
          <SimpleMessage body="Wassup my dudes?!? My name Jeff. I am an ~ARIST~"/>
          <br/>
        </div>
        
      )
  }
}

class Posts extends React.Component{
  render(){
    return(
      <div>
        <Post imgName={img1} text="Pls I wanna buy dj sona"/>
        <Post imgName={img2} text="Dat gorge tho"/>
        <Post imgName={img3} text="I want some eggs"/>
    </div>)
  }
}

function Post(props){
  return(
    <div className="App-Post">
      <img className="Post-Image" src={props.imgName} alt="Cannot Veiw Image"/>
      <br/>
      <button><span role="img" aria-label="star">⭐</span> </button>
      <button><span role="img" aria-label="msg">💬</span></button>
      <br/>
      <p>{props.text}</p>
    </div>
    )
}

class Prof_Pic extends React.Component{
  render(){
    return <img className="Prof-Image" src={this.props.imgName} alt="This is a pic"/>
  }
}

class SimpleMessage extends React.Component{
  render(){
    return <p>{this.props.body}</p>
  }
}

function EmoteSheep(props){
  return(
    <p><span role="img" aria-label="sheep">🐑</span> {props.count} </p>
    )
}

function EmoteMail(props){
  return(
    <p><span role="img" aria-label="mail">💌</span> {props.count} </p>
    )
}




export default Profile;
