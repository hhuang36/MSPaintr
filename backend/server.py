# Source: Bottle


from bottle import get, route, redirect, run, Bottle, static_file, view, post, request
import bottle
import json
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
import mysql.connector
import bcrypt
import random

app = Bottle()

# mydb = mysql.connector.connect(host="mysqldb",
# 							   user="default",
# 							   passwd="changeme",
# 							   database="mspaintrdb"
# 							   )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS Users(username VARCHAR(20) NOT NULL, password VARCHAR(45), "
# 				 "bio VARCHAR(255), followers INT)")
# mycursor.execute("CREATE TABLE IF NOT EXISTS Posts (postid VARCHAR(255), image VARCHAR(255), upvotes INT, "
# 				 "Users_username VARCHAR (20))")
# mycursor.execute("CREATE TABLE IF NOT EXISTS Comments(commentid INT, comment VARCHAR(255), Posts_postid VARCHAR(255),"
# 				 "Users_username VARCHAR(20))")
# sql_stmt = (
# 	"INSERT INTO Users (username, password, bio, followers) "
# 	"VALUES (%s, %s, %s, %s)"
# )
# val = ("eggie", "defaultpass", "This is the default bio.", "0")
# mycursor.execute(sql_stmt, val)
# mydb.commit()
#
# testpost = ("INSERT INTO Posts (postid, image, upvotes, Users_username) VALUES (%s, %s, %s, %s)")
# testvals = ("eggie.png", "eggie.png", "0", "eggie")
# mycursor.execute(testpost, testvals)
# mydb.commit()

bottle.TEMPLATE_PATH.insert(0, 'frontend/src/components/')
bottle.TEMPLATES.clear()


@app.get('/')
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
    retVal = {"posts": []}
    mycursor.execute('SELECT * FROM Posts')
    row = mycursor.fetchone()
    posts = []
    while row is not None:
        postDetails = {"user_name": row[3], "post_image": row[1], "post_id": row[0], "likes": row[2]}
        posts.append(postDetails)
        row = mycursor.fetchone()
    retVal["posts"] = posts
    return retVal

    return retVal


@app.route('/home')
def getFeed():
    redirect('/')


@app.route("/updoot")
def serveUpdoot():
    wsock = request.environ.get('wsgi.websocket')
    while True:
        try:
            message = wsock.receive()

            if not (message == None):

                messy = json.loads(message)

                if messy["type"] == 'updoot':

                    # message is the name of the image
                    # update the image and reutrn a json object
                    # format:
                    # "imageName" : <imagename>
                    # "updoots" : <newupodots>

                    resp = {"type": "updoot", "imageName": messy["message"], "updoots": 81}

                    for client in server.clients.values():
                        client.ws.send(json.dumps(resp))



        except WebSocketError:
            break


@app.post("/login-confirm")
def confirmLogin():
    username = request.forms["user"]
    password = request.forms["passwd"]
    print(username)
    print(password)
    file = open("../frontend/src/components/login/users.csv", "r")
    for line in file:
        credentials = line.split(",")
        if credentials[0] == str(username):
            if bcrypt.checkpw(str(password).encode('utf-8'), str(credentials[1][0:len(credentials[1])-1]).encode('utf-8')):
                sessions = open("../frontend/src/components/login/sessions.csv", 'a')
                token = generateToken()
                print(token)
                sessions.write(str(username) + "," + token + "\n")
                bottle.response.add_header('Set-Cookie', "token=" + token)
                return "Confirmed."
            else:
                return "Incorrect Password."

    return "User does not exist."
# 				mycursor.execute('SELECT * FROM Users WHERE username=' + username)
# 				row = mycursor.fetchone()
# 				if row is not None:
# 					if bcrypt.checkpw(password, row["password"]):
# 						redirect('/')
# 					else:
# 						resp = bottle.HTTPError("Incorrect credentials.")
# 						return resp
# 				else:
# 					resp = bottle.HTTPError("User not found.")
# 					return resp

@app.post("/register-process")
def processRegister():
    username = request.forms["username"]
    password = request.forms["password"]
    users = open("../frontend/src/components/login/users.csv", "r")
    for line in users:
        credentials = line.split(",")
        if credentials[0] == str(username):
            return "Username already in use."

    if checkCriteria(str(password)) == "valid":
        hashedpw = bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())
        print(username)
        print(password)
        file = open("../frontend/src/components/login/users.csv", 'a')
        file.write(str(username) + "," + str(hashedpw.decode('utf-8')) + "\n")
        return "Successfully registered."
    else:
        return checkCriteria(str(password))
    # # this is where you should check if password meets criteria
    # # if it does hash the pw and store it in the database
    # if checkCriteria(password) == "valid":
    # 	hashedpw = saltAndHash(password)
    # 	sql_stmt = (
    # 		"INSERT INTO Users (username, password, bio, followers) "
    # 		"VALUES (%s, %s, %s, %s)"
    # 	)
    # 	val = (username, hashedpw, "This is the default bio.", "0")
    # 	mycursor.execute(sql_stmt, val)
    # 	mydb.commit()
    # else:
    # 	resp = checkCriteria(password)
    # 	return resp
    # redirect('/login')


@app.route("/comment")
def serveComment():
    wsock = request.environ.get('wsgi.websocket')
    while True:
        try:
            message = wsock.receive()

            print(message)

            # message is the comment in a string
            # send the comment
            # fomat:
            # <username>:<message>

            if not (message == None):

                messy = json.loads(message)

                if messy["type"] == 'comment':

                    # this is where you should update the database

                    msg = "eggie: " + messy["message"]

                    resp = {"type": "comment", "message": msg, "image": messy["image"]}

                    for client in server.clients.values():
                        client.ws.send(json.dumps(resp))



        except WebSocketError:
            break


@app.route("/post")
def servePost():
    wsock = request.environ.get('wsgi.websocket')
    while True:
        try:
            message = wsock.receive()

            if not (message == None):

                # write image to a file
                # we will need to have some method of renaming the image
                # then sending the name of that renamed image
                # allimages should be saved in testimages
                file = open("frontend/src/components/testimages/image0.png", 'w')
                file.write(message)

                # send a json witht the image and the user who posted it
                # format
                # imagename holds a string of the image just uploaded
                # username holds a string of who posted it
                retVal = {"type": "image", "imagename": "image0.png", "username": "eggie"}

                for client in server.clients.values():
                    client.ws.send(json.dumps(retVal))


        except WebSocketError:
            break


@app.route("/image/<image_name>")
def serveImage(image_name):
    print(image_name)
    return static_file(image_name, root="frontend/src/components/testimages/", mimetype="image/png")


@app.get("/App.css")
def serveAppCSS():
    return static_file("App.css", root="frontend/src/", mimetype="text/css")


@app.get("/app.js")
def serveAppCSS():
    return static_file("app.js", root="frontend/src/", mimetype="text/javascript")


@app.get('/login')
def serveLogin():
    return static_file("Login.html", root="../frontend/src/components/login", mimetype="text/html")


@app.get("/Login.css")
def serveLoginCSS():
    return static_file("Login.css", root="../frontend/src/components/login", mimetype="text/css")


@app.get("/register")
def serveRegister():
    return static_file("Regristration.html", root="../frontend/src/components/register", mimetype="text/html")


@app.get("/Regristration.css")
def serveRegisterCSS():
    return static_file("Regristration.css", root="../frontend/src/components/register", mimetype="text/css")


@app.get("/profile")
@view("profile/Profile.tpl", )
def serveProfile():
    """
    format is a dictionary with the keys user_name, user_bio and images
    user_name and user_bio hold strings that hold the user's username and bio respectively
    images holds a dicitonary where the name of each image is the key and the value is the number (integer) of likes recieve
    """
    retVal = {"user_name": '', "user_bio": '', "images": {}}

    retVal["user_name"] = "eggie"
    retVal["user_bio"] = "I like tofu and MS Paint"
    retVal["images"] = {"testimage.png": 7, "testimage2.png": 80, "eggie.png": 999}

    return retVal


@app.get("/Profile.css")
def serveProfileCSS():
    return static_file("Profile.css", root="frontend/src/components/profile", mimetype="text/css")


@app.get("/directmessages")
def serveDMS():
    return static_file("DirectMessages.html", root="frontend/src/components/dms", mimetype="text/html")


@app.get("/DirectMessages.css")
def serveDMSCSS():
    return static_file("DirectMessages.css", root="frontend/src/components/dms", mimetype="text/css")


@app.get("/newpost")
def serveNewPost():
    return static_file("NewPost.html", root="frontend/src/components", mimetype="text/html")


@app.get("/seemore/<post_id>")
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
    retVal = {"user_name": "", "post_image": "", "comments": [], "likes": 0}
    retVal["user_name"] = "eggie"
    retVal["post_image"] = "../image/" + post_id
    print(post_id)
    retVal["comments"] = [{"user": "eggie", "comment_body": "super cool!"},
                          {"user": "tofu", "comment_body": "i love it!!"}]
    return retVal


@app.get("/MSPaintRLogo.png")
def serveLogo():
    return static_file("MSPaintRLogo.png", root="frontend/src/components/profile/profileimages", mimetype="image/png")


def saltAndHash(password):
    hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedpw


def checkCriteria(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if password.islower():
        return "Password must contain an uppcase character."
    if not any(char.isdigit() for char in password):
        return "Password must contain a number."

    return "valid"


def generateToken():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O ',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    token = ""
    i = 0
    while (i < 16):
        token += chars[random.randint(0, 51)]
        i += 1
    return token


if __name__ == "__main__":
    server = WSGIServer(("0.0.0.0", 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()
