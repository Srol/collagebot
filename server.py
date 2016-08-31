from __future__ import unicode_literals
from flask import Flask, request, redirect
from rq import Queue
from worker import conn
from utils import collage_it

app = Flask(__name__)
q = Queue(connection=conn)

@app.route("/request", methods = ['POST'])
def grab():
	#Insert outgoing request token here.
	if request.method == "POST" and request.form.get('token') == "Insert slack token here":
		files = request.form.get('text').split()
		del files[0]
		channel = request.form.get('channel_name')
		userName = request.form.get('user_name')
		if len(files) == 2:
			force = False
		elif len(files) == 3 and files[2] == "-f":
			files.pop()
			force = True
		# this sends the URLs of the files to collage as well as the other data sent in the request to the worker function
		result = q.enqueue(collage_it, files, channel, userName, force)
		print(files)
		print(channel)
		print(userName)
		return "Processing request."
	else:
		return "problem"