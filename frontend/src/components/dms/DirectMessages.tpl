<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title> Messages </title>
    <link rel="stylesheet" type="text/css" href="/DirectMessages.css"/>
    <script type="text/javascript" src=/app.js></script>
</head>

<body>
<div class="navigationbar">
    <a class="active" href="/home">Home</a>
    <a href="/profile">My Profile</a>
</div>

<br>
<h1 align="center"> {{user}}'s DM's 🖌️</h1>
<p id="user" style="display: none;">{{user}}</p>
<div class="chatbox" >
    <div class="sidebar" id="sidebar">
        <div class ="messagesdisplay" >
            <ul id="messages">
                <br>
                %for follower in followers:
                   %if int(follower[1]) == 1:
			             <li><a href="/directmessages/{{follower[0]}}">🎨 {{follower[0]}}</a></li>

                        <li id="{{follower[0]}}" class="read"><button onclick="messageSwitch('{{follower[0]}}'); return false;" class="DMer-Button">🎨 {{follower[0]}}</button></li>
                    %else:
                    <li><a href="/directmessages">🎨 {{follower[0]}}</a></li><li id="{{follower[0]}}" class="unread"><button onclick="messageSwitch('{{follower[0]}}'); return false;" class="DMer-Button">🎨 {{follower[0]}}</button></li>
                    %end
                %end
            </ul>

        </div>
    </div>
    <div class="chat" id="chat" style="overflow-y: scroll; height: 545px" >
        <p id="messager" style="display: none;">{{messager}}</p>
        <ul class="messagesList" id = "messagesList">
            %for message in messages:
                <li>{{message[0]}}: {{message[1]}}</li>
            %end
        </ul>
        <input id="textbox" type="text" placeholder="  Enter message...">
        <button onclick="messageSend();return false;">Send</button>
    </div>
</div>
<!--
<script src="script.js"></script>
-->
</body>

</html>
