from flask import Flask
from requests import get

app = Flask(__name__)

@app.route('/')
def hello_world():
    # business logic (call api, db , message queue)
    response = []
    apicalled = get('https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8').json()

    for i in apicalled:
        if i['city'] == 'London':
            response.append(i)

    return response

if __name__ == '__main__':
    app.run()