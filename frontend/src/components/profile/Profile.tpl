<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="Profile.css"/>
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
        % for image in images:
          <div class="Profile-Post">
            <img class="Post-Image" src={{image}} alt="Cannot Veiw Image"/>
            <br/>
            <button  class="Profile-Button">⭐</button>
            <button  class="Profile-Button">💬</button>
          </div>
        % end
        </div>
    </div>
</body>

