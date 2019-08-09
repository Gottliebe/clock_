import time

from flask import Flask, Response
import datetime

app = Flask(__name__)

@app.route("/")
def clock():
    return Response(f"Current date {str(datetime.date.today())}\n" + f"Current time {str(datetime.datetime.now().time())}")

@app.route('/time')
def get_time():
    def eventsStream():
        while True:
            yield str(get_time()) + " \r\n";

    return Response(eventsStream());


def get_time():
    time.sleep(1.0)
    return f"Current date {str(datetime.date.today())} " + f"Current time {str(datetime.datetime.now().time())}"

def bootapp():
    app.run(port='8080')

if __name__ == "__main__":
    bootapp()


