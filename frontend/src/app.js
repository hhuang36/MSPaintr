

socket = new WebSocket("ws://" + window.location.host + "/updoot")

socket.onmessage = function(evt){ 

	response = JSON.parse(evt.data)
	if( response["type"] != "updoot"){
		return;
	}
	
	document.getElementById("count" + response["imageName"]).innerHTML = response["updoots"]
}

socketComment = new WebSocket("ws://" + window.location.host + "/comment")

socketComment.onmessage = function(evt){ 
	response = JSON.parse(evt.data)
	if( response["type"] != "comment"){
		return false;
	}

	if(!document.getElementById(response["image"] ) || !document.getElementById("comments") ){
		return false;
	}

	comms = document.getElementById("comments")
	prep = document.createElement("P")
	prep.appendChild(document.createTextNode(response["message"]))
	comms.appendChild(prep)
}

function sendComment(imagename) {

	comm = document.getElementById('comment').value

	resp = {'type' : 'comment', 'message' : comm, 'image' : imagename}
	
	socketComment.send(JSON.stringify(resp))
}

function sendUpdoot(img_name){
	resp = {'type' : 'updoot', 'message' : img_name}

	socket.send(JSON.stringify(resp))
}
	

socketPost = new WebSocket("ws://" + window.location.host + "/post")

function submitPost(){
	file = document.getElementById("name").files[0]
	reader = new FileReader();
	data = new ArrayBuffer();
	reader.loadend= function(){}
	reader.onload= function(evt){
		data = evt.target.result;
		socketPost.send(data)
	}
	reader.readAsArrayBuffer(file)
}

socketPost.onmessage = function(evt){

	info = JSON.parse(evt.data)

	if( info["type"] != "image"){
		return false;
	}
		

	img = info["imagename"]
	user = info["username"]

	outer = document.createElement("DIV")
	outer.className = "Post"

	para = document.createElement("P")
	para.innerHTML = "POSTED BY: " + user

	image = document.createElement("IMG")

	image.src = "/image/" + img
	image.className = "Post-Image"
	image.id = img
	image.alt = "Cannot Veiw Image"

	button = document.createElement("BUTTON")
	button.className = "Profile-Button"
	button.onclick = sendUpdoot(img)

	spann = document.createElement("SPAN")
	spann.id = img 
	spann.innerHTML = 0

	button.appendChild(spann)
	button.appendChild(document.createTextNode("⭐"))

	seemore = document.createElement("A")
	seemore.href= "seemore/" + img
	seemore.innerHTML = "See More"

	outer.appendChild(para)
	outer.appendChild(image)
	outer.appendChild(document.createElement("BR"))
	outer.appendChild(button)
	outer.appendChild(document.createElement("BR"))
	outer.appendChild(seemore)

	document.getElementById("Subs").appendChild(outer)
}

socketMessage = new WebSocket("ws://" + window.location.host + "/message")

function messageSend(){
	msg = document.getElementById("textbox").value

	reciever = document.getElementById("messager").textContent

	info = {"messagee" : reciever, "message" : msg, "type" : "message", "open": false}

	console.log(info)

	socketMessage.send(JSON.stringify(info))
}

socketMessage.onopen = function(evt){
	socket.send(JSON.stringify({"type" : "message", "open": true}))
}

socketMessage.onmessage = function(evt){
	response = JSON.parse(evt.data)
	if(response["type"] != "message"){
		return false;
	}
	console.log("eklflfjasd")

	active = document.getElementById("messager").textContent
	user = document.getElementById("user").textContent

	curr = ""
	friend = ""

	if(response["messagee"] == user.value){
		curr = response["messagee"]
		friend =response["messager"]
	}else{
		curr = response["messager"]
		friend = response["messagee"]
	}

	if(friend != active){
		user.className = "unread"
	}else{
		li = document.createElement("LI")
		li.innerHTML = response["messager"] +": " + response["message"]
		document.getElementById("messagesList").appendChild(li)
	}


}

function follow(){
	user = document.getElementById("username").textContent
	console.log(user)
	var request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			console.log(this.response)
			document.getElementById("followbutton").innerHTML = JSON.parse(this.response) + "🐑"
		}
	}
	request.open("POST", "/follow")
	request.send(JSON.stringify(user));
}


function messageSwitch(follower){
	var request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			console.log(this.response)
			resp = JSON.parse(this.response)
			document.getElementById("messager").innerHTML = follower
			mlist = document.getElementById("messagesList")
			mlist.innerHTML = ""

			for(message of resp["messages"]){
				console.log(message)
				li = document.createElement("LI")
				li.innerHTML = message[0] + ": " + message[1]
				mlist.appendChild(li)
			}

		}
	}
	request.open("POST", "/messageSwitch")
	request.send(JSON.stringify(follower));
}