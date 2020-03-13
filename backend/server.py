#Source: Bottle


from bottle import get, post, request, route,redirect, run, response


def readFile(filename):
	result = ""
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			result += line + '\r\n'
	return result 

def createImageFile(filename):
	body = ""
	with open(filename, "rb") as f:
		body = f.read()

	return body


@get('/')
def serve_home():
	return readFile("../frontend/src/components/Home.html")

@route('/home')
def getFeed():
	redirect('/')

@get("/App.css")
def serveAppCSS():
	response.content_type = 'text/css; charset=utf-8'
	return readFile("../frontend/src/App.css")

@get('/login')
def serveLogin():
	return readFile("../frontend/src/components/login/Login.html")

@get("/Login.css")
def serveLoginCSS():
	response.content_type = 'text/css; charset=utf-8'
	return readFile("../frontend/src/components/login/Login.css")

@get("/register")
def serveRegister():
	return readFile("../frontend/src/components/register/Regristration.html")

@get("/Regristration.css")
def serveRegisterCSS():
	response.content_type = 'text/css; charset=utf-8'
	return readFile("../frontend/src/components/register/Regristration.css")

@get("/profile")
def serveProfile():
	return readFile("../frontend/src/components/profile/Profile.html")

@get("/Profile.css")
def serveProfileCSS():
	response.content_type = 'text/css; charset=utf-8'
	return readFile("../frontend/src/components/profile/Profile.css")

@get("/directmessages")
def serveDMS():
	return readFile("../frontend/src/components/dms/DirectMessages.html")

@get("/DirectMessages.css")
def serveDMSCSS():
	response.content_type = 'text/css; charset=utf-8'
	return readFile("../frontend/src/components/dms/DirectMessages.css")

@get("/newpost")
def serveNewPost():
	return readFile("../frontend/src/components/NewPost.html")

@get("/seemore")
def serveMore():
	return readFile("../frontend/src/components/SeeMore.html")

@get("/MSPaintRLogo.png")
def serveLogo():
	response.content_type = "image/png; charset=ascii"
	return createImageFile("../frontend/src/components/profile/profileimages/MSPaintRLogo.png")

@get("/testimage.png")
def serveLogo():
	response.content_type = "image/png; charset=ascii"
	return createImageFile("../frontend/src/components/testimages/testimage.png")

@get("/testimage2.png")
def serveLogo():
	response.content_type = "image/png; charset=ascii"
	return createImageFile("../frontend/src/components/testimages/testimage2.png")

@get("/eggie.png")
def serveLogo():
	response.content_type = "image/png; charset=ascii"
	return createImageFile("../frontend/src/components/profile/profileimages/eggie.png")

@get("/subtle_lgbt.png")
def serveLogo():
	response.content_type = "image/png; charset=ascii"
	return createImageFile("../frontend/src/components/profile/profileimages/subtle_lgbt.png")

if __name__ == "__main__":
	run(host='localhost', port=8000)