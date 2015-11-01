
# {
#   "credentials": {
#     "url": "https://gateway.watsonplatform.net/question-and-answer-beta/api",
#     "username": "9d3f02a8-6067-429c-a313-8d32cf2f1b50",
#     "password": "ahnExOadRVuA"
#   }
# }



# from pywatson.watson import Watson
# import requests

# watson = Watson(url='https://gateway.watsonplatform.net/question-and-answer-beta/api', username='9d3f02a8-6067-429c-a313-8d32cf2f1b50', password='ahnExOadRVuA')


# print watson.ask_question(question_text="how are you" , category="healthcare")



import requests
import json
from pprint import pprint

def getHealth(q):

	url = "https://gateway.watsonplatform.net/question-and-answer-beta/api/v1/question/healthcare"
	r = requests.post(url,
	         data=json.dumps({"question": {"questionText": q}}),
	         headers={"Content-Type": "application/json", "X-SyncTimeout": '30'},
	         auth=("9d3f02a8-6067-429c-a313-8d32cf2f1b50", "ahnExOadRVuA"))
	return (json.loads(r.text)[0]['question']['evidencelist'][0]['text'])


def getTravel(q):

	url = "https://gateway.watsonplatform.net/question-and-answer-beta/api/v1/question/travel"
	r = requests.post(url,
	         data=json.dumps({"question": {"questionText": q}}),
	         headers={"Content-Type": "application/json", "X-SyncTimeout": '30'},
	         auth=("9d3f02a8-6067-429c-a313-8d32cf2f1b50", "ahnExOadRVuA"))
	# pprint(json.loads(r.text))
	return (json.loads(r.text)[0]['question']['evidencelist'][0]['text'])



import translate_sel

translate_sel.eng2hin(getHealth("wcdcis qqwwedd"))

