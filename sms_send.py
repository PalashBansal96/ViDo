#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pprint import pprint
import requests

# from settings import sid, token


def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body

        })


if __name__ == '__main__':
    # 'From' doesn't matter; For transactional, this will be replaced with your SenderId;
    # For promotional, this will be ignored by the SMS gateway
    # Incase you are wondering who Dr. Rajasekhar is http://en.wikipedia.org/wiki/Dr._Rajasekhar_(actor)

    v = "हिंदी में".decode('UTF-8').encode('UTF-16')

    r = send_message('byld5', '7b462e15311bf7d65ba15ffdebf5fd885ac4b4a5',
        sms_from='',  # sms_from='8808891988',
        sms_to='9818148131', # sms_to='9052161119',
        sms_body="एड्स मुख्य रूप से मानव इम्यूनो वायरस (एचआईवी) की वजह से एक प्रतिरक्षा प्रणाली विकार है, लेकिन यह भी तंत्रिका तंत्र को प्रभावित कर सकते हैं। इस तरह के भ्रम, विस्मृति, व्यवहार में बदलाव, सिर दर्द, प्रगतिशील कमजोरी और हाथ और पैर में सनसनी के नुकसान, संज्ञानात्मक मोटर हानि, या क्षति के रूप में लक्षण है, जिससे एचआईवी सीधे तंत्रिका कोशिकाओं पर आक्रमण करने के लिए प्रकट नहीं होता है, लेकिन यह उनके स्वास्थ्य और समारोह jeopardizes परिधीय तंत्रिकाएं।")
    print r.status_code
    pprint(r.json())