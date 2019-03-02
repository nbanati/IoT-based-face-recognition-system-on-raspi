import pyrebase
config={
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
    }
firebase = pyrebase.initialize_app(config)

db=firebase.database()

db.child("names").push({"name":"pajji"})