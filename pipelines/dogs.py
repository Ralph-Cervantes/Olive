"""
A simple background worker designed to periodically fetch and store dog data.

"""
import re
import requests
import schedule
import time
from data.db import SessionLocal
from data.models.dogs import Dog
from data.schemas.dogs import ExternalDog

URL = 'https://interview-api-olive.vercel.app/api/dogs?page={}'


def cleaned(words):
    # Basic string validation to normalize the data 
    words = re.sub(r'[^\x00-\x7F]+', '', words)
    return ' '.join(words.strip().split())

def fetch_dogs(db):
    page = 1
    while True:
        try:
            # Fetch the data from the external service 
            response = requests.get(URL.format(page))
            data = response.json()

            # If the reponse does not contain data, break out of the loop 
            if not data:
                break
            
            # If the response is malformed, move onto the next page
            if not isinstance(data, list):
                page += 1
                continue
            
            # Validate the resposne body and save into dict with the breed as the key
            dogs = {cleaned(item['breed']): ExternalDog(**item) for item in data}
            breeds = set(dogs.keys())
            found = set(cleaned(dog.breed) for dog in db.query(Dog).where(Dog.breed.in_(breeds)).all())

            # Find the dogs that don't already exist in the databsae 
            new_dogs = breeds - found
            for new_dog in new_dogs:
                info = dogs.get(new_dog)

                breed = cleaned(info.breed)
                db.add(Dog(breed=breed, image=info.image))
                db.commit()

            # Go to the next page
            page += 1

        except Exception as e:
            print(f'Error: {e}')
            continue

def create_dog():
    try:
        db = SessionLocal()
        fetch_dogs(db)
    finally:
        db.close()


print("Starting pipeline scheduler...")
schedule.every(5).seconds.do(create_dog)
# schedule.every(1).hours.do(create_dog)
while True:
    schedule.run_pending()
    print("Scheduler is running...")
    time.sleep(5)



