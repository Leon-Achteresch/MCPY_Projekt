import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('finanzen-d1c2c-firebase-adminsdk-5qaxo-b1f0e33497.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://finanzen-d1c2c-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference('MCPY/Aufgabe')

def check_and_reset_task():
    data = ref.get()
    for aufgabe, status in data.items():
        if status == True:
            print(f'Die Aufgabe "{aufgabe}" ist True.')
            try:  
                ref.child(aufgabe).set(False)
                
            finally:
                print(f'Die Aufgabe "{aufgabe}" ist nun auf False.')

while True:
    check_and_reset_task()
