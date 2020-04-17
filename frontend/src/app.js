

socket = new WebSocket("ws://localhost:8000/updoot")

socket.onmessage = function(evt){ 
	response = JSON.parse(evt.data)
	document.getElementById("count" + response["imageName"]).innerHTML = response["updoots"]
}

socketComment = new WebSocket("ws://localhost:8000/comment")

socketComment.onmessage = function(evt){ 
	comms = document.getElementById("comments")
	prep = document.createElement("P")
	prep.appendChild(document.createTextNode(evt.data))
	comms.appendChild(prep)
}


socketPost = new WebSocket("ws://localhost:8000/post")

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