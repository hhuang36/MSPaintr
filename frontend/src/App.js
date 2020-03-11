import React from "react";
import "./App.css";
import "./components/SubscriptionFeed.js";
import SubscriptionFeed from "./components/SubscriptionFeed.js";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import SeeMorePage from "./components/SeeMorePage";
import NaviBar from "./components/NaviBar";
import Login from "./components/login/Login.js";
import Register from "./components/register/Regristration.js";
import DMs from "./components/dms/DirectMessages.js";
import Profile from "./components/profile/Profile.js";
import logo from "./components/profile/profileimages/MSPaintRLogo.png";

export default function App() {
  return (
    <div className="App">
        <NaviBar/>
        <img className="Profile-Logo" src={logo}/>
        <Router>
          <Switch>
              <Route exact path={"/"} component={SubscriptionFeed}></Route>
              <Route exact path={"/home"} component={SubscriptionFeed}></Route>
              <Route exact path={"/more"} component={SeeMorePage}></Route>
              <Route exact path={"/login"} component={Login}></Route>
              <Route exact path={"/register"} component={Register}></Route>
              <Route exact path={"/directmessages"} component={DMs}></Route>
              <Route exact path={"/profile"} component={Profile}></Route>
          </Switch>
        </Router>
      </div>

  );
}
