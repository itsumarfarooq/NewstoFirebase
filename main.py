from reuters import get_reuters_headlines
from foxnews import get_foxnews_headlines
from cnn import get_cnn_headlines
from firebase import Firebase

config =  {
        'apiKey': "AIzaSyA-gwShYTSeDiroeDewu7PV9piKVslDAAQ",
        'authDomain': "headlines-9ced6.firebaseapp.com",
        'databaseURL': "https://headlines-9ced6.firebaseio.com",
        'storageBucket': "headlines-9ced6.appspot.com",
        "serviceAccount": "credentials.json"
    }

firebase = Firebase(config)
db = firebase.database()
db.push(get_reuters_headlines())
db.push(get_foxnews_headlines())
db.push(get_cnn_headlines())