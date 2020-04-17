<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="/App.css"/>
  <script src="/app.js"></script>
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
    %image = post_image.replace("../", "")
		<img class="Post-Image" id={{image}} src={{post_image}} alt="cannot veiw image"/>
 		 <br/>
        <form onsubmit="socketComment.send(document.getElementById('comment').value); return false;"> 
          <input type ="text" id="comment" />
          <input type ="submit" value="Add Comment"/>
        </form>
      
	  	<button  class="Profile-Button" onclick="socket.send('{{image}}');"><span id="count{{image}}">{{likes}}</span>⭐</button>
	  	<br>
      <div id="comments">
  	  	% for comment in comments:
          <p>{{comment["user"]}}:{{comment["comment_body"]}}</p>
        % end
      </div>
	</div>
</body>