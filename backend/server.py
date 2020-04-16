#Source: Bottle


from bottle import get, route, redirect, run, static_file, view, post, request
import bottle
import bottle_mysql
import json

bottle.TEMPLATE_PATH.insert(0, 'frontend/src/components/')
app = bottle.Bottle()
plugin = bottle_mysql.MySQLPlugin(dbname='mspaintrdb')
app.install(plugin)

@get('/')
@app.route('/')
@view("Home.tpl")
def serve_home(db):
	"""
	format: dictionary with one key, posts, which is a list of dictionaries
	posts has 4 keys, user_name, post_image, post_id and likes
	user_name is a string containing the user who posted the image
	post_image is a string containing the name of the image to be displayed
	post_id cointains a string of the post id
	likes is an integer containing the number of likes a post has
	"""
	db.execute('SELECT * FROM POSTS')
	row = db.fetchone()
	posts = []
	while row is not None:
		postDetails = {"user_name": row['Users_username'], "post_image": row['image'], "post_id": row['postid'],
					   "likes": row['upvotes']}
		posts.append(postDetails)
		row = db.fetchone()
		retVal = {"posts": posts}
	return retVal


@route('/home')
def getFeed():
	redirect('/')

@post("/updoot")
@app.route('/updoot', 'POST')
def serveUpdoot(db):
	image_name = json.loads(request.body.read().decode('utf-8'))
	db.execute('SELECT * FROM Posts where image=' + image_name)
	row = db.fetchone()
	upvoted = row['upvotes'] + 1
	db.execute('UPDATE Posts SET upvotes=' + upvoted + 'where image=' + image_name)
	return upvoted

@post('/image-form')
	# Add code to add image to a folder

@app.route('/insert/post', 'POST')
@post('/insert/post')
def insertPost(db):
	username = json.loads(request.body.read().decode('utf-8'))['username']
	image = json.loads(request.body.read().decode('utf-8'))['image']
	numPosts = db.execute('SELECT COUNT (postid) FROM Posts')
	postid = numPosts+1
	db.execute(
	'INSERT INTO Posts(postid, image, upvotes, Users_username) VALUES({}, {}, {}, {}, {})'
		.format(username, postid, image, 0))

@app.route('insert/comment/<post_id>' 'POST')
@post('insert/comment/<post_id>')
def insertComment(post_id, db):
	comment = json.loads(request.body.read().decode('utf-8'))['comment']
	username = json.loads(request.body.read().decode('utf-8'))['username']
	commentid = db.execute('SELECT COUNT (postid) FROM Comments where postid=' + post_id) + 1
	db.execute(
		'INSERT INTO Comments(commentid, comment, Posts_postid, Users_username) VALUES({}, {}, {}, {})'
			.format(commentid, comment, post_id, username))

''' We don't need this for Phase 2'''
@app.route('insert/user', 'POST')
@post('/insert/user')
def insertUserInfo(db):
	username = json.loads(request.body.read().decode('utf-8'))['username']
	password = json.loads(request.body.read().decode('utf-8'))['password']
	bio = json.loads(request.body.read().decode('utf-8'))['bio']
	db.execute('INSERT INTO Users(username, password, bio, followers) VALUES ({}, {}, {}, {})'
			   .format(username, password, bio, 0))

@get("/App.css")
def serveAppCSS():
	return static_file("App.css", root="frontend/src/", mimetype="text/css")

@get("/app.js")
def serveAppCSS():
	return static_file("app.js", root="frontend/src/", mimetype="text/javascript")

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

@get("/profile/<username>")
@app.route('/profile/<username>')
@view("profile/Profile.tpl")
def serveProfile(username, db):
	"""
	format is a dictionary with the keys user_name, user_bio and images
	user_name and user_bio hold strings that hold the user's username and bio respectively
	images holds a dicitonary where the name of each image is the key and the value is the number (integer) of likes recieve
	"""
	username = 'defaultuser' # One user for now
	db.execute('SELECT * FROM Users where username=' + username)
	row = db.fetchone()
	retVal ={"user_name" : '',"user_bio": '', "images": {}}
	db.execute('SELECT * FROM Posts where Users_username=' + username)
	images = {}
	getImageRow = db.fetchone()
	while getImageRow is not None:
		upvotes = getImageRow['upvotes']
		getImageRow = db.fetchone()
		images.update({getImageRow['image'] : upvotes})
	retVal["user_name"] = username # One user for now
	retVal["user_bio"] = row['bio']
	retVal["images"] = images
	return retVal

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

@get("/seemore/<post_id>")
@app.route('/seemore/<post_id>')
@view("SeeMore.tpl")
def serveMore(post_id, db):
	"""
	format: a dictionary with 4 keys user_name, post_image, comments, and likes
	user_name is a stirng containing the user who posted the image
	post_image is the name of the image file to be displayed (string)
	comments is a list of dictionaries, with two keys user and comment_body
		user is the username of the commenter
		comment_body is their comment
	likes is an integer contianing the number of likes
	"""
	db.execute('SELECT * FROM Posts WHERE postid=' + post_id)
	row = db.fetchone()
	db.execute('SELECT * FROM Comments WHERE postid=' + post_id)
	comments = []
	commentThread = db.fetchone()
	while commentThread is not None:
			comments.append(commentThread['comment'])
			commentThread = db.fetchone()

	if row:
		retVal = {"user_name": "", "post_image": "", "comments":[], "likes" : 0 }
		retVal["user_name"] = 'defaultuser' # One user for now
		retVal["post_image"] = "../" + post_id
		print(post_id)
		retVal["comments"] = comments
		retVal["likes"] = row['upvotes']
		return retVal
	return bottle.HTTPError(404, "No posts found for post ID: " + post_id)

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