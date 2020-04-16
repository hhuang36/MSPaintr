# Source: Bottle
from bottle import get, route, redirect, run, static_file
import bottle
import bottle_mysql

app = bottle.Bottle()
plugin = bottle_mysql.MySQLPlugin(dbname='mspaintrdb')
app.install(plugin)

''' Makes a fake user account with username as 'default' '''
@app.route('insert/<username>/<password>/<bio>')
def insertUserInfo(username, password, bio, db):
    db.execute('INSERT INTO Users(username, password, bio, followers) VALUES ({}, {}, {}, {})'
            .format(username, password, bio, 0))

@app.route('insert/post/<username>/<image>')
def insertPost(username, image, db):
    numPosts = db.execute('SELECT COUNT (postid) FROM Posts')
    postid = numPosts+1
    db.execute(
        'INSERT INTO Posts(postid, image, upvotes, Users_username) VALUES({}, {}, {}, {}, {})'
            .format(username, postid, image, 0))

@app.route('insert/comment/<username>/<postid>/<comment>')
def insertComment(username, postid, comment, db):
    commentid = db.execute('SELECT COUNT (postid) FROM Comments where postid= + postid') + 1
    db.execute(
        'INSERT INTO Comments(commentid, comment, Posts_postid, Users_username) VALUES({}, {}, {}, {})'
            .format(commentid, comment, postid, username))

@app.route('insert/upvote/<postid>')
def insertUpvote(postid, db):
    db.execute('SELECT * FROM Posts where postid=' + postid)
    row = db.fetchone()
    currUpvotes = row['upvotes'] + 1
    db.execute('UPDATE Posts SET upvotes=' + currUpvotes + ' where postid=' + postid)

@app.route('retrieve/comments/<postid>')
def retrieveCommentThread(postid, db):
    db.execute('SELECT * FROM Comments where postid=' + postid)
    row = db.fetchone()
    commentThread = []
    while row is not None:
        commentThread.append(row['comment'])
    return commentThread

@app.route('retrieve/newsfeed')
def retrieveNewsFeed(db):
    db.execute('SELECT * FROM Posts')
    row = db.fetchone()
    posts = []
    while row is not None:
        posts.append(retrievePostDetails(row['postid']), db)
    return posts

@app.route('/retrieve/profile/<username>')
def retrieveUserInfo(username, db):
    db.execute('SELECT * FROM Users where username=' + username)
    row = db.fetchone()
    db.execute('SELECT * FROM Posts where Users_username=' + username)
    images = []
    getImageRow = db.fetchone
    while getImageRow is not None:
        images.append(getImageRow['image'])
    if row:
        return {"username": username, "user_bio": row['bio'], "images": images}
    return bottle.HTTPError(404, "User not found")

@app.route('retrieve/posts/<postid>')
def retrievePostDetails(postid, db):
    db.execute('SELECT * FROM Posts WHERE postid=' + postid)
    row = db.fetchone()
    postid = 1
    while row is not None:
        postid+=1
    if row:
        return [{"user_name": row['Users_username'], "post_image": row['image'], "post_id": postid,
                 "likes": row['upvotes']}]
    return bottle.HTTPError(404, "No posts found for user")


@app.route('')
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
