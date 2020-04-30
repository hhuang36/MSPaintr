<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title> Messages </title>
    <link rel="stylesheet" type="text/css" href="DirectMessages.css"/>
    <script type="text/javascript" src=/app.js></script>
</head>

<body>
<div class="navigationbar">
    <a class="active" href="/home">Home</a>
    <a href="/profile">My Profile</a>
</div>

<br>
<h1 align="center"> My DM's 🖌️</h1>

<div class="chatbox" >
    <div class="sidebar" id="sidebar">
        <input id="searchmessages" type="text" placeholder="  Search Messages...">
        <div class ="messagesdisplay" >
            
            <ul id="messages">
                <br>
                %for follower in followers:
                <li onclick="messageSwitch({{follower}});"> 🎨 {{follower}}</li>
                %end
            </ul>

        </div>
    </div>
    <div class="chat" id="chat" style="overflow-y: scroll; height: 545px">
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