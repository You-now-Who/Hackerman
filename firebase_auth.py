import pyrebase

config = {
    "apiKey" : "AIzaSyBF5sdmUn1uC60xAGDgQXNDyDyv4DNayXg",
    "authDomain" : "minecare-2e2c7.firebaseapp.com",
    "databaseURL" : "https://minecare-2e2c7-default-rtdb.firebaseio.com",
    "projectId" : "minecare-2e2c7",
    "databaseURL": "https://minecare-2e2c7-default-rtdb.firebaseio.com/",
    "storageBucket" : "minecare-2e2c7.appspot.com",
    "messagingSenderId" : "355994474813",
    "appId" : "1:355994474813:web:12ed67ed555733b4fa4d54",
    "measurementId" : "G-QDGDL3WH6J"}

firebase = pyrebase.initialize_app(config)