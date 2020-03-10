import React from "react";
import "./App.css";
import "./components/SubscriptionFeed.js";
import SubscriptionFeed from "./components/SubscriptionFeed.js";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import SeeMorePage from "./components/SeeMorePage";
import NaviBar from "./components/NaviBar";
import Login from "./components/login/Login.js";
import Register from ""
import DMs from "./components/dms/DirectMessages.js"
import Profile from "./profile/Profile.js"

export default function App() {
  return (
    <div className="App">
        <NaviBar/>
        <Router>
            <Switch>
                <Route path={"/"} exact component={SubscriptionFeed}></Route>
                <Route path={"/more"} component={SeeMorePage}></Route>
                <Route path={"/login"} component={Login}></Route>
                <Route path={"/register"} component={Register}></Route>
                <Route path={"/directmessages"} component={DMs}></Route>
                <Route path={"/profile"} component={Profile}></Route>
            </Switch>
        </Router>
    </div>

  );
}