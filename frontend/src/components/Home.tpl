<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="/App.css"/>
	<script src="app.js"></script>
	<title>Home</title>
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
      <br />
    </div>
	<img src="MSPaintRLogo.png" class="Profile-Logo"/>
	<div class="SubscriptionFeed" id= "Subs">
		% for post in posts:
			<div class="Post">
			
				<p>POSTED BY: {{post["user_name"]}}</p>
				<img class="Post-Image" id={{post["post_id"]}} src="/image/{{post['post_image']}}" alt="Cannot Veiw Image"/>
	     		 <br/>
			  	<button  class="Profile-Button" onclick="socket.send('{{post["post_image"]}}');"><span id="count{{post["post_image"]}}">{{post["likes"]}}</span>⭐</button>
			  	<br>
			  	<a href= seemore/{{post["post_id"]}}>See More</a>
			
			</div>
		% end
		
	</div>
</body>