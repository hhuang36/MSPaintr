

socket = new WebSocket("ws://" + window.location.host + "/updoot")

socket.onmessage = function(evt){ 
	response = JSON.parse(evt.data)
	document.getElementById("count" + response["imageName"]).innerHTML = response["updoots"]
}

socketComment = new WebSocket("ws://" + window.location.host + "/comment")

socketComment.onmessage = function(evt){ 
	comms = document.getElementById("comments")
	prep = document.createElement("P")
	prep.appendChild(document.createTextNode(evt.data))
	comms.appendChild(prep)
}


socketPost = new WebSocket("ws://" + window.location.host +"/post")

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
	button.onclick = "socket.send('imagename');"

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

