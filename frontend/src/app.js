function updoot(imageName){
	console.log("What the fuck")
	const request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(this.readyState === 4 && this.status === 200){
			console.log(this.response)
			document.getElementById("count" + imageName).innerHTML = this.response
		}
	};
	request.open("POST", "/updoot")
	let data =document.getElementById(imageName).src

	request.send(JSON.stringify(data))
}

function postImage(user){
	var request2 = new XMLHttpRequest();
	request2.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			console.log(this.response);
		}
	}
	imageName = document.getElementById("image");
	request2.open("POST", "/insert/post");
	request2.send(JSON.stringify({username : user, image: imageName}))
}

function insertComment(user, postid){
	var request3= new XMLHttpRequest();
	request3.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			console.log(this.response);
		}
	}

	var comment = document.getElementById("comment");
	request3.open("POST", "/insert/comment/" + postid);
	request3.send(JSON.stringify({username : user, comment: comment}))
}
