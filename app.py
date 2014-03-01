from flask import Flask
import json

app = Flask("test_app")

@app.route("/login/", methods=['POST', 'GET'])
def login():
	return "Login here"


@app.route("/docs/", methods=['GET'])
def docs():
	app.logger.info("hello")
	return "a collection of docs"

@app.route("/doc/<int:docid>/", methods=['GET', 'POST'])
def doc(docid):
	#app.logger.info("doc hello")
	dict_ = {'id':docid,
			'text':"Some made up text for classification"}
	doc = json.dumps(dict_)
	return doc
	#return "a test doc with id: {0}".format(docid)

	
if __name__ == "__main__":
	app.run(debug=True)