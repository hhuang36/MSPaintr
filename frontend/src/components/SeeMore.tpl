<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="/App.css"/>
	<title>Home</title>
</head>
<body>
	<div className="LeftAlign">
    <a href="/home">MSPaintr</a>
    <br/>
            <a href="/login">Sign in</a>
      <br/>
            <a href="/profile">Profile</a>
      <br/>
            <a href="/directmessages">DMs</a>
      <br/>
      <a href="/newpost">Add Post</a>
       <br />
      <input type ="text" id="search" />
    <input type ="submit" value="Search"/>
  </div>
	<img src="../MSPaintRLogo.png" class="Profile-Logo"/>
	<div class="Post">
		<p>POSTED BY: {{user_name}}</p>
		<img class="Post-Image" src={{post_image}} alt="cannot veiw image"/>
 		 <br/>
         <input type ="text" id="user_name" />
        <input type ="submit" value="Add Comment"/>
	  	<button  class="Profile-Button">⭐</button>
	  	<br>
	  	% for comment in comments:
        <p>{{comment["user"]}}:{{comment["comment_body"]}}</p>
      % end
	</div>
</body>