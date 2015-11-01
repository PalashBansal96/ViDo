from flask import Flask, render_template, request
import thread
import requests
import urllib
import threading
from requests import exceptions
app = Flask(__name__)


@app.route('/voice')
def about():
	sid = request.args.get('CallSid')	
	fro = request.args.get('From')
	url = request.args.get('RecordingUrl')
	url = urllib.unquote(url).decode('utf8')
	url = url.split(',')[-1]
	# threading.Thread(target=get_audio, args=(sid, url,)).start()
	second_server_ip="http://localhost"
	params = {'url':url, 'sid':sid}
	print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	print second_server_ip+":5002/trans?"+ urllib.urlencode(params)
	r = requests.get("http://127.0.0.1:5002/trans?"+ urllib.urlencode(params))
	print "ssssssssssssssssssssssssssssssssss"
	print r.status_code
	return "True"

def get_audio(sid, url):
	while True:
		try:
			r = requests.get(url)
			if r.status_code == 200:
				with open(sid + '.mp3', 'w') as f:
					f.write(r.content)
				thread.exit()
			else:
				time.sleep(30)
				continue
		except(exceptions.ConnectionError, exceptions.HTTPError, exceptions.Timeout) as err:
			break
	thread.exit()

if __name__ == '__main__':
	app.run(debug=True,port=5000)