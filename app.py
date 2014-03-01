from flask import Flask, make_response
import json

app = Flask("test_app")


def _send(data, err=None):
	"""Merge output with default data."""
	
	dict_ = {"version":"0.1",
			"err":err,
			"data":data}
	resp = make_response(json.dumps(dict_))
	resp.headers['Content-Type'] ='application/json'
	return resp
	
@app.errorhandler(404)
def error(msg):
	err = "Error. {0}".format(msg)
	return _send([], err=err)

@app.route("/login/", methods=['POST', 'GET'])
def login():
	return "Login here"


@app.route("/docs/", methods=['GET'])
def docs():
	app.logger.info("hello")
	return _send([])

@app.route("/doc/<int:docid>/", methods=['GET', 'POST'])
def doc(docid):
	"""Return a doc for classification."""
	
	data = {'id':docid,
			'text':"Some made up text for classification"}
	return _send(data)
	
	
if __name__ == "__main__":
	app.run(debug=True)