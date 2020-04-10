#Source: Bottle


from bottle import get, route, redirect, run, static_file, view, post, request
import bottle
import json
bottle.TEMPLATES.clear()
bottle.TEMPLATE_PATH.insert(0, '../frontend/src/components/')

@get('/')
@view("Home.tpl")
def serve_home():
	"""
	format: dictionary with one key, posts, which is a list of dictionaries
	posts has 4 keys, user_name, post_image, post_id and likes
	user_name is a string containing the user who posted the image
	post_image is a string containing the name of the image to be displayed
	post_id cointains a string of the post id
	likes is an integer containing the number of likes a post has
	"""
	retVal = {"posts":[]}
	retVal["posts"] = [{"user_name": "eggie", "post_image": "eggie.png", "post_id": "eggie.png", "likes" : 8},{"likes": 9, "user_name": "eggie", "post_image": "testimage.png", "post_id": "testimage.png"}]

	return retVal

@route('/home')
def getFeed():
	redirect('/')

@post("/updoot")
def serveUpdoot():
	image_name = json.loads(request.body.read().decode('utf-8'))
	#Put code here to get the number of updoots for the given image and add 1 to it
	#return said numbers
	return json.dumps(8)

@get("/App.css")
def serveAppCSS():
	return static_file("App.css", root="../frontend/src/", mimetype="text/css")

@get("/app.js")
def serveAppCSS():
	return static_file("app.js", root="../frontend/src/", mimetype="text/javascript")

@get('/login')
def serveLogin():
	return static_file("Login.html", root="../frontend/src/components/login", mimetype="text/html")

@get("/Login.css")
def serveLoginCSS():
	return static_file("Login.css", root="../frontend/src/components/login", mimetype="text/css")

@get("/register")
def serveRegister():
	return static_file("Regristration.html", root="../frontend/src/components/register", mimetype="text/html")

@get("/Regristration.css")
def serveRegisterCSS():
	return static_file("Regristration.css", root="../frontend/src/components/register", mimetype="text/css")

@get("/profile")
@view("profile/Profile.tpl",)
def serveProfile():
	"""
	format is a dictionary with the keys user_name, user_bio and images
	user_name and user_bio hold strings that hold the user's username and bio respectively
	images holds a dicitonary where the name of each image is the key and the value is the number (integer) of likes recieve
	"""
	retVal ={"user_name" : '',"user_bio": '', "images": {}}

	retVal["user_name"] = "eggie"
	retVal["user_bio"] = "I like tofu and MS Paint"
	retVal["images"] = {"testimage.png": 7, "testimage2.png": 80, "eggie.png": 999 }

	return retVal

@get("/Profile.css")
def serveProfileCSS():
	return static_file("Profile.css", root="../frontend/src/components/profile", mimetype="text/css")

@get("/directmessages")
def serveDMS():
	return static_file("DirectMessages.html", root="../frontend/src/components/dms", mimetype="text/html")

@get("/DirectMessages.css")
def serveDMSCSS():
	return static_file("DirectMessages.css", root="../frontend/src/components/dms", mimetype="text/css")

@get("/newpost")
def serveNewPost():
	return static_file("NewPost.html", root="../frontend/src/components", mimetype="text/html")

@get("/seemore/<post_id>")
@view("SeeMore.tpl")
def serveMore(post_id):
	"""
	format: a dictionary with 4 keys user_name, post_image, comments, and likes
	user_name is a stirng containing the user who posted the image
	post_image is the name of the image file to be displayed (string)
	comments is a list of dictionaries, with two keys user and comment_body
		user is the username of the commenter
		comment_body is their comment
	likes is an integer contianing the number of likes
	"""
	retVal = {"user_name": "", "post_image": "", "comments":[], "likes" : 0 }
	retVal["user_name"] = "eggie"
	retVal["post_image"] = "../" + post_id
	print(post_id)
	retVal["comments"] = [{"user": "eggie", "comment_body": "super cool!"}, {"user": "tofu", "comment_body": "i love it!!"}]
	return retVal

@get("/MSPaintRLogo.png")
def serveLogo():
	return static_file("MSPaintRLogo.png", root="../frontend/src/components/profile/profileimages", mimetype="image/png")

@get("/testimage.png")
def serveLogo():
	return static_file("testimage.png", root="../frontend/src/components/testimages", mimetype="image/png")

@get("/testimage2.png")
def serveLogo():
	return static_file("testimage2.png", root="../frontend/src/components/testimages", mimetype="image/png")

@get("/eggie.png")
def serveLogo():
	return static_file("eggie.png", root="../frontend/src/components/profile/profileimages", mimetype="image/png")

@get("/subtle_lgbt.png")
def serveLogo():
	return static_file("subtle_lgbt.png", root="../frontend/src/components/profile/profileimages", mimetype="image/png")


run(host='0.0.0.0', port=8000)