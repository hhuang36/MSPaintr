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