from flask import Flask, render_template, request
import thread
import requests
import urllib
import threading
from requests import exceptions
from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
import speech_recognition as sr
from pydub import AudioSegment
import os


app = Flask(__name__)


@app.route('/trans')
def trans():
	sid = request.args.get("sid")
	url = request.args.get("url")
	print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	print url
	threading.Thread(target=process_request, args=(sid, url)).start()
	return '1'

def process_request(sid, url):
	while (True):
		try:
			r = requests.get(url)
			if r.status_code == 200:
				with open(sid + '.mp3', 'w') as f:
					f.write(r.content)
					print f.name
				sound = AudioSegment.from_mp3(sid+".mp3")
				sound.export(sid+".wav","wav")
				# os.remove(sid+".mp3")
				break
			else:
				time.sleep(30)
				continue
		except(exceptions.ConnectionError, exceptions.HTTPError, exceptions.Timeout) as err:
			thread.exit()
	r = sr.Recognizer()
	# with sr.WavFile(open(os.path.realpath(sid+".wav"), "r")) as source:
	# 	audio = r.record(source)                   # listen for the first phrase and extract it into audio data
	# t = datetime.now()
	# try:
	# 	in_hindi = r.recognize_google(audio)
	# 	print("You said " + in_hindi)    # recognize speech using Google Speech Recognition
	# except LookupError:                            # speech is unintelligible
	# 	print("Could not understand audio")
	
	with sr.WavFile("/home/krngrvr09/Desktop/inout/pradhan.wav") as source:
		audio = r.record(source)                   # listen for the first phrase and extract it into audio data
	t = datetime.now()
	try:
		in_hindi = r.recognize_google(audio)
		print("You said " + str(in_hindi))    # recognize speech using Google Speech Recognition
	except LookupError:                            # speech is unintelligible
		print("Could not understand audio")
	


	global fp
	driver = webdriver.Firefox(firefox_profile=fp)
	driver.get("http://translate.google.com")
	driver.find_element_by_css_selector("#source").click()
	driver.find_element_by_css_selector("#source").send_keys(in_hindi)
	driver.find_element_by_css_selector("#gt-submit").click()
	result = ""
	while  result.strip() == "":
		result = driver.find_element_by_css_selector("#result_box").text
	driver.find_element_by_css_selector("#source").clear()
	print result
	r = get_result(result)
	print r.content
	print datetime.now() - t
	thread.exit()

def get_result(result):
	r = requests.get("http://vido.herokuapp.com/q/"+result)
	return r


if __name__ == '__main__':
	global fp
	fp = webdriver.FirefoxProfile()
	app.run(debug=True, use_reloader=False, port=5002)
