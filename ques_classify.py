from alchemyapi_python.alchemyapi import AlchemyAPI
import json


alchemyapi = AlchemyAPI()


response = alchemyapi.taxonomy('text', 'to to prevent cancer')

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Categories ##')
    for category in response['taxonomy']:
        print(category['label'], ' : ', category['score'])
    print('')

else:
    print('Error in taxonomy call: ', response['statusInfo'])
