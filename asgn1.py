'''
Resources:
Source 1: https://www.tutorialspoint.com/nodejs/nodejs_restful_api.htm
Source 2: https://www.youtube.com/watch?v=Q-BpqyOT3a8

To set up flask and solve any errors:
Source 3: https://www.youtube.com/watch?v=GHvj1ivQ7ms

Resolve Docker Error
Source 4: https://phoenixnap.com/kb/cannot-connect-to-the-docker-daemon-error

What is Dockerfile?
https://www.youtube.com/watch?v=LQjaJINkQXY&ab_channel=AutomationStepbyStep

ResfulAPI NodeJS:
https://www.tutorialspoint.com/nodejs/nodejs_restful_api.htm

Flask installation: 
https://pythonhosted.org/Flask-JSON/#installation

Running RESTAPI:
https://towardsdev.com/run-your-first-restful-api-service-using-docker-b6d8801af255



What I learned: 

API:
1. Think of like: a contract provided by one piece of software to another.
-> structured request and structured response

2. API IS A MESSENGER OR WAITER BETWEEN RUNNING SOFTWARE that sends some form of response/data to client
3. REST is a web architecture that uses HTTP protocol.
4. This server provides access to resources and client acn modify the resources using HTTP protocol.
5. Texts (resources) are often represented usinng JSON

6. 2 HTTP methods we will need to use are GET and PUT


Summary: 
1. API is the messenger and REST lets us use HTTP request to formmat those messages.
2. Endpoints are the URI where API can be accessed by a client application
3. curl tool - transfers data using multiple protocols

'''


#To run:
#flask run -p 8081
#library

#docker build instantiates container to run 
#docker build -t myimage .
#docker run -p 8081:8081 

import json
import flask
from flask import Flask, request, Response


#set up the application
app=Flask(__name__)

msg1="Hello, world!"

#create a route so that when we launch app we dont get 404 error
@app.route('/hello', methods=['GET', 'POST'])
def helloURI():
    if request.method=='POST':
        return Response('This method is unsupported.',status=405)
        
    if request.method=='GET' and request.args.get('name'):
        return Response("Hello, "+ request.args.get('name') + "!",status=200)
    
    if request.method=='GET':
        return Response('Hello, world!',status=200)
        
    return Response('This method is unsupported.', status=405)

@app.route('/check', methods=['GET', 'POST'])
def checkURI():
    
    if request.method=='GET':
        return Response('All is well!',status=200)
    
    if request.method=='POST':
        return Response('This method is unsupported.',status=405)
    

    
if __name__=="__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
    
    