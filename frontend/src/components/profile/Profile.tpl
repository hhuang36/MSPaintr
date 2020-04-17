<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="Profile.css"/>
  <script src="app.js"></script>
	<title>Profile</title>
</head>
<body>
  <div class="LeftAlign">
        <a href="/home">MSPaintr</a>
        <br />
                <a href="/login">Sign in</a>
          <br />
                <a href="/profile">Profile</a>
          <br />
                <a href="/directmessages">DMs</a>
          <br />
          <a href="/newpost">Add Post</a>
           <br />
          <input type ="text" id="search" />
        <input type ="submit" value="Search"/>
    </div>
	<img src="MSPaintRLogo.png" class="Profile-Logo"/>
	<div class="Profile">
      <div class="Profile-Side">
          <p>{{user_name}}<p/>
          
          <button class="Profile-Button">💌</button>
          <span>&nbsp;</span>
          <button class="Profile-Button"> 🐑 </button>
          <br/>
          <p>{{user_bio}}</p>
          <br/>
        </div>
      <div class="Profile-Posts">
        % for image in images.keys():
          <div class="Profile-Post">
            <img class="Post-Image" id={{image}} src={{image}} alt="Cannot Veiw Image"/>
            <br/>
            <button  class="Profile-Button" onclick="socket.send('{{image}}');"><span id="count{{image}}">{{images[image]}}</span>⭐</button>
            <br>
            <a href= seemore/{{image}}>See More</a>
          </div>
        % end
        </div>
    </div>
</body>

