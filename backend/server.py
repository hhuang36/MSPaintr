#Source: Bottle


from bottle import get, route, redirect, run, static_file


@get('/')
def serve_home():
	return static_file("Home.html", root="frontend/src/components", mimetype="text/html")

@route('/home')
def getFeed():
	redirect('/')

@get("/App.css")
def serveAppCSS():
	return static_file("App.css", root="frontend/src/", mimetype="text/css")

@get('/login')
def serveLogin():
	return static_file("Login.html", root="frontend/src/components/login", mimetype="text/html")

@get("/Login.css")
def serveLoginCSS():
	return static_file("Login.css", root="frontend/src/components/login", mimetype="text/css")

@get("/register")
def serveRegister():
	return static_file("Regristration.html", root="frontend/src/components/register", mimetype="text/html")

@get("/Regristration.css")
def serveRegisterCSS():
	return static_file("Regristration.css", root="frontend/src/components/register", mimetype="text/css")

@get("/profile")
def serveProfile():
	return static_file("Profile.html", root="frontend/src/components/profile", mimetype="text/html")

@get("/Profile.css")
def serveProfileCSS():
	return static_file("Profile.css", root="frontend/src/components/profile", mimetype="text/css")

@get("/directmessages")
def serveDMS():
	return static_file("DirectMessages.html", root="frontend/src/components/dms", mimetype="text/html")

@get("/DirectMessages.css")
def serveDMSCSS():
	return static_file("DirectMessages.css", root="frontend/src/components/dms", mimetype="text/css")

@get("/newpost")
def serveNewPost():
	return static_file("NewPost.html", root="frontend/src/components", mimetype="text/html")

@get("/seemore")
def serveMore():
	return static_file("SeeMore.html", root="frontend/src/components", mimetype="text/html")

@get("/MSPaintRLogo.png")
def serveLogo():
	return static_file("MSPaintRLogo.png", root="frontend/src/components/profile/profileimages", mimetype="image/png")

@get("/testimage.png")
def serveLogo():
	return static_file("testimage.png", root="frontend/src/components/testimages", mimetype="image/png")

@get("/testimage2.png")
def serveLogo():
	return static_file("testimage2.png", root="frontend/src/components/testimages", mimetype="image/png")

@get("/eggie.png")
def serveLogo():
	return static_file("eggie.png", root="frontend/src/components/profile/profileimages", mimetype="image/png")

@get("/subtle_lgbt.png")
def serveLogo():
	return static_file("subtle_lgbt.png", root="frontend/src/components/profile/profileimages", mimetype="image/png")


run(host='0.0.0.0', port=8000)