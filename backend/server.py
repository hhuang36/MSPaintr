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
import hashlib

app = Bottle()

mydb = mysql.connector.connect(host="mysqldb",
							   user="default",
							   passwd="changeme",
							   database="mspaintrdb"
							   )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Tokens(usern VARCHAR(255), token VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Users(username VARCHAR(20) NOT NULL, password VARCHAR(255), "
				 "bio VARCHAR(255), followers INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Posts (postid VARCHAR(255), image VARCHAR(255), upvotes INT, "
				 "Users_username VARCHAR (20))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Comments(commentid INT, comment VARCHAR(255), Posts_postid VARCHAR(255),"
				 "Users_username VARCHAR(20))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Upvotes(postid VARCHAR(255), Users_username VARCHAR (20))")

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
    """''
    checkToken = bottle.request.get_cookie('token')
    _username = getUsername(checkToken)
    if _username is None:
        redirect('/login')
    else:
        username = _username
        print(username)
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


@app.route('/home')
def getFeed():
    checkToken = bottle.request.get_cookie('token')
    if getUsername(checkToken) is None:
        redirect('/login')
    redirect('/')


@app.route("/updoot")
def serveUpdoot():
    checkToken = bottle.request.get_cookie('token')
    tokenuser = getUsername(checkToken)
    if tokenuser is None:
        redirect('/login')
    wsock = request.environ.get('wsgi.websocket')
    while True:
        try:
            message = wsock.receive()

            if not (message == None):

                messy = json.loads(message)

                if messy["type"] == 'updoot':
                    post_id = messy["message"]
                    # message is the name of the image
                    # update the image and reutrn a json object
                    # format:
                    # "imageName" : <imagename>
                    # "updoots" : <newupodots>

                    upvotes = getUpvotes(post_id, tokenuser)
                    query = "UPDATE Posts SET upvotes = %s WHERE postid = %s"
                    data = (upvotes, post_id)
                    mycursor.execute(query, data)
                    mydb.commit()

                    resp = {"type": "updoot", "imageName": post_id, "updoots": upvotes}

                    for client in server.clients.values():
                        client.ws.send(json.dumps(resp))

        except WebSocketError:
            break

@app.route("/logout")
def logout():
    bottle.response.set_cookie('token', "INVALID", path="/")
    redirect('/login')

@app.post("/login-confirm")
def confirmLogin():
    username = request.forms["user"]
    password = request.forms["passwd"]
    select = "SELECT * FROM Users WHERE username= %s"
    mycursor.execute(select, (username,))
    row = mycursor.fetchone()
    if row is not None:
        if bcrypt.checkpw(str(password).encode('utf-8'), str(row[1]).encode('utf-8')):
            token = generateToken()
            hashedToken = hashlib.sha256(token.encode('utf-8')).hexdigest()
            print(hashedToken)
            select_user = "SELECT * FROM Tokens WHERE usern= %s"
            mycursor.execute(select_user, (username,))
            row2 = mycursor.fetchone()
            if row2 is not None:
                sql_stmt = "UPDATE Tokens SET token = %s WHERE usern = %s"
                val = (str(hashedToken), username)
                mycursor.execute(sql_stmt, val)
            else:
                sql_stmt = ("INSERT INTO Tokens (usern, token) VALUES (%s, %s)")
                val = (username, str(hashedToken))
                mycursor.execute(sql_stmt, val)
            mydb.commit()
            bottle.response.set_cookie('token', token, path="/")
            redirect('/')
        else:
            return "Incorrect credentials."
    else:
        redirect('/register')

@app.post("/register-process")
def processRegister():
    username = request.forms["username"]
    password = request.forms["password"]
    # # this is where you should check if password meets criteria
    # # if it does hash the pw and store it in the database
    select = "SELECT * FROM Users WHERE username= %s"
    mycursor.execute(select, (username,))
    row = mycursor.fetchone()
    if row is not None:
        return "Username already in use."

    if checkCriteria(str(password)) == "valid":
        hashedpw = saltAndHash(password)
        hashedpw = str(hashedpw.decode('utf-8'))
        reg_stmt = (
    		"INSERT INTO Users (username, password, bio, followers) "
    		"VALUES (%s, %s, %s, %s)"
    	)
        reg_val = (username, hashedpw, "This is the default bio.", "0")
        mycursor.execute(reg_stmt, reg_val)
        mydb.commit()
        redirect('/login')
    else:
        return checkCriteria(str(password))


@app.route("/comment")
def serveComment():
    checkToken = bottle.request.get_cookie('token')
    username = getUsername(checkToken)
    if username is None:
        redirect('/login')
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
                    msg = username + ": " + messy["message"]
                    post_id = messy["image"]

                    select_comm = "SELECT * FROM Comments WHERE Posts_postid = %s"
                    comm_data = (post_id,)
                    mycursor.execute(select_comm, comm_data)
                    allComms = mycursor.fetchall()
                    id = 0
                    if allComms != None:
                        for com in allComms:
                            id += 1

                    comment_stmt = (
                        "INSERT INTO Comments (commentid, comment, Posts_postid, Users_username) "
                        "VALUES (%s, %s, %s, %s)"
                    )
                    print("id: ")
                    print(id)
                    comm_vals = (id, messy["message"], post_id, username)
                    mycursor.execute(comment_stmt, comm_vals)
                    mydb.commit()

                    resp = {"type": "comment", "message": msg, "image": post_id}

                    for client in server.clients.values():
                        client.ws.send(json.dumps(resp))
        except WebSocketError:
            break


@app.route("/post")
def servePost():
    checkToken = bottle.request.get_cookie('token')
    username = getUsername(checkToken)  # ADDED
    if username is None:  # CHANGED
        redirect('/login')
    else:  # ADDED
        wsock = request.environ.get('wsgi.websocket')
        while True:
            try:
                message = wsock.receive()

                if not (message == None):
                    getSize = "SELECT * FROM Posts"  # ADDED
                    mycursor.execute(getSize)  # ADDED
                    allPosts = mycursor.fetchall()
                    num = 0  # ADDED
                    if allPosts is not None:
                        for p in allPosts:
                            num += 1

                    print(num)  # ADDED
                    imgname = "image" + str(num) + ".png"  # ADDED
                    file = open("frontend/src/components/testimages/" + imgname, 'wb')  # CHANGED
                    file.write(message)
                    retVal = {"type": "image", "imagename": imgname, "username": username}  # CHANGED
                    insertPost = ("INSERT INTO Posts (postid, image, upvotes, Users_username) "  # ADDED
                                  "VALUES (%s, %s, %s, %s)")  # ADDED
                    values = (imgname, imgname, "0", username)  # ADDED
                    mycursor.execute(insertPost, values)  # ADDED
                    mydb.commit()  # ADDED
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
    return static_file("Login.html", root="frontend/src/components/login", mimetype="text/html")

@app.get("/Login.css")
def serveLoginCSS():
    return static_file("Login.css", root="frontend/src/components/login", mimetype="text/css")


@app.get("/register")
def serveRegister():
    return static_file("Regristration.html", root="frontend/src/components/register", mimetype="text/html")


@app.get("/Regristration.css")
def serveRegisterCSS():
    return static_file("Regristration.css", root="frontend/src/components/register", mimetype="text/css")


@app.get("/profile")
@view("profile/Profile.tpl", )
def serveProfile():
    checkToken = bottle.request.get_cookie('token')
    username = getUsername(checkToken)
    if username is None:
        redirect('/login')
    else:
        retVal = {"user_name": '', "user_bio": '', "images": {}}
        retVal["user_name"] = username
        selectUserInfo = "SELECT * FROM Users where username = %s"
        mycursor.execute(selectUserInfo, (username,))
        userInfo = mycursor.fetchone()
        if userInfo is not None:
            retVal["user_bio"] = userInfo[2]
            images = {}
            getImages = "SELECT * FROM Posts where Users_username = %s"
            mycursor.execute(getImages, (username,))
            getImageRow = mycursor.fetchone()
            while getImageRow is not None:
                upvotes = getImageRow[2]
                images.update({getImageRow[1]: upvotes})
                getImageRow = mycursor.fetchone()
            retVal["images"] = images
        else:                                           # WE CAN EDIT THIS LATER
            retVal["user_bio"] = "Random bio"
            retVal["images"] = {"testimage.png": 7, "testimage2.png": 80, "eggie.png": 999}

        return retVal



@app.get("/Profile.css")
def serveProfileCSS():
    return static_file("Profile.css", root="frontend/src/components/profile", mimetype="text/css")


@app.get("/directmessages")
def serveDMS():
    checkToken = bottle.request.get_cookie('token')
    if getUsername(checkToken) is None:
        redirect('/login')
    return static_file("DirectMessages.html", root="frontend/src/components/dms", mimetype="text/html")


@app.get("/DirectMessages.css")
def serveDMSCSS():
    return static_file("DirectMessages.css", root="frontend/src/components/dms", mimetype="text/css")


@app.get("/newpost")
def serveNewPost():
    checkToken = bottle.request.get_cookie('token')
    if getUsername(checkToken) is None:
        redirect('/login')
    return static_file("NewPost.html", root="frontend/src/components", mimetype="text/html")


@app.get("/seemore/<post_id>")
@view("SeeMore.tpl")
def serveMore(post_id):
    checkToken = bottle.request.get_cookie('token')
    if getUsername(checkToken) is None:
        redirect('/login')
    """
    format: a dictionary with 4 keys user_name, post_image, comments, and likes
    user_name is a stirng containing the user who posted the image
    post_image is the name of the image file to be displayed (string)
    comments is a list of dictionaries, with two keys user and comment_body
        user is the username of the commenter
        comment_body is their comment
    likes is an integer contianing the number of likes
    """
    select = "SELECT * FROM Posts WHERE postid = %s"
    mycursor.execute(select, (post_id,))
    post = mycursor.fetchone()
    username = post[3]
    retVal = {"user_name": "", "post_image": "", "comments": [], "likes": 0}
    retVal["user_name"] = username
    retVal["likes"] = post[2]
    retVal["post_image"] = "../image/" + post_id
    retVal["comments"] = getAllComments(post_id)
    return retVal


@app.get("/MSPaintRLogo.png")
def serveLogo():
    return static_file("MSPaintRLogo.png", root="frontend/src/components/profile/profileimages", mimetype="image/png")


def saltAndHash(password):
    hashedpw = bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())
    return hashedpw


def checkCriteria(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if password.islower():
        return "Password must contain an uppercase character."
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
    return str(token)

def getUsername(token):
    if token is not None:
        hashedToken = hashlib.sha256(token.encode('utf-8')).hexdigest()
        selectToken = "SELECT * FROM Tokens WHERE token = %s"
        mycursor.execute(selectToken, (hashedToken,))
        row = mycursor.fetchone()
        if row is not None:
            return row[0]
    return None

def getUpvotes(post_id, username):
    select = "SELECT * FROM Posts WHERE postid = %s"
    mycursor.execute(select, (post_id,))
    fetched = mycursor.fetchone()
    upvotes = fetched[2]

    selectUpvotes = "SELECT * FROM Upvotes WHERE postid = %s"
    mycursor.execute(selectUpvotes, (post_id,))
    fetchedUpvotes = mycursor.fetchall()

    upvoteExists = False

    if fetchedUpvotes is not None:
        for up in fetchedUpvotes:
            if up[1] == username:
                upvotes = upvotes - 1
                upvoteExists = True
                query = ("DELETE FROM Upvotes WHERE Users_username = %s")
                data = (username,)
                mycursor.execute(query, data)
                mydb.commit()

    if not upvoteExists:
        upvotes = upvotes + 1
        query = ("INSERT INTO Upvotes (postid, Users_username) VALUES (%s, %s)")
        data = (post_id, username)
        mycursor.execute(query, data)
        mydb.commit()

    return upvotes

def getAllComments(post_id):
    select_comm = "SELECT * FROM Comments WHERE Posts_postid = %s"
    comm_data = (post_id,)
    mycursor.execute(select_comm, comm_data)
    allComms = mycursor.fetchall()
    ret = []
    if allComms is not None:
        for comm in allComms:
            addendum = {"user": comm[3], "comment_body": comm[1]}
            ret.append(addendum)
    return ret

server = WSGIServer(("app", 8000), app, handler_class=WebSocketHandler)
server.serve_forever()
