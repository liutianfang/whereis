import requests

url = 'http://127.0.0.1:8000/jdAlpha/whereis/'
httpsUrl="https://www.whereis.top/jdAlpha/whereis/"
headers = {
        'Content-Type': 'application/json',
    }


def post(fname='IntentRequest-cancel.json', url='http://127.0.0.1:8000/jdAlpha/whereis/'):
    file =  open(fname, 'rb')
    str= file.read()
    file.close()
    r = requests.post(url,headers=headers, data=str)
    print(r.text)

if __name__ == '__main__':
    post()
    post('IntentRequest-cancel.json',httpsUrl)
