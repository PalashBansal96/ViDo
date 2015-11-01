import requests
#curl 'http://translate.google.com/translate_tts?ie=UTF-8&q=Hello&tl=en&client=t' -H 'Referer: http://translate.google.com/' -H 'User-Agent: stagefright/1.2 (Linux;Android 5.0)' > google_tts.mp3

headers={}
headers["Referer"] = "http://translate.google.com/"
headers["User-Agent"] = "stagefright/1.2 (Linux;Android 5.0)"
r = requests.get("http://translate.google.com/translate_tts?ie=UTF-8&q=Hello&tl=hi&client=t",headers = headers)
print r.content