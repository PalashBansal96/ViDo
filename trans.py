# pip install SpeechRecognition.
# pip install pyaudio
from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://translate.google.com")
import speech_recognition as sr

while(True):
	r = sr.Recognizer()
	with sr.Microphone() as source:                # use the default microphone as the audio source
		print("Wait")
		r.adjust_for_ambient_noise(source)
		print("Go")
		audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
	t = datetime.now()
	in_hindi = r.recognize_google(audio)
	try:
	    print("You said " + in_hindi)    # recognize speech using Google Speech Recognition
	except LookupError:                            # speech is unintelligible
	    print("Could not understand audio")

	driver.find_element_by_css_selector("#source").click()
	driver.find_element_by_css_selector("#source").send_keys(in_hindi)
	driver.find_element_by_css_selector("#gt-submit").click()
	result = ""
	while  result.strip() == "":
		result = driver.find_element_by_css_selector("#result_box").text
	driver.find_element_by_css_selector("#source").clear()
	print result
	r = requests.get("http://vido.herokuapp.com/q/"+result)
	print r.content
	print datetime.now() - t