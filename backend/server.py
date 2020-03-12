#Source: Bottle


from bottle import get, post, request, run, response, view


def readFile(filename):
	result = ""
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			result += line + '\r\n'
	return result 


@get('/')
@view('template')
def serve_home():
	return dict(src="/index")

@get('/App')
def getFeed():
	response.content_type="text/javascript"
	return readFile("../frontend/src/App.js")

@get('/index')
def getIndex():
	response.content_type="text/javascript"
	return readFile("../frontend/src/index.js")

if __name__ == "__main__":
	run(host='localhost', port=8080)