import os
import requests
from datetime import datetime

NUTRITION_EXERCISE_ID = os.environ["NUTRITION_EXERCISE_ID"]
NUTRITION_EXERCISE_KEY = os.environ["NUTRITION_EXERCISE_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]


APP_ID = NUTRITION_EXERCISE_ID
API_KEY = NUTRITION_EXERCISE_KEY

GENDER = "male"
WEIGHT_KG = 74
HEIGHT_CM = 172
AGE = 47


NUTRITION_EXERCISE_ENDPOINT = "https://app.100daysofpython.dev"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY

}

GOOGLE_SHEET_NAME = 'workout'
def process_exercise_data():
    today = datetime.now()
    message = input("Tell me which exercises you did: ")
    exercise_params = {
        "query": message,
        "gender": GENDER,           # Optional: Weight in kg (1-500)
        "weight_kg": WEIGHT_KG,     # Optional: Height in cm (1-300)
        "height_cm": HEIGHT_CM,     # Optional: Age (1-150)
        "age": AGE,                 # Optional: "male" or "female"
        }

    response = requests.post(url=f"{NUTRITION_EXERCISE_ENDPOINT}/v1/nutrition/natural/exercise",json=exercise_params, headers=headers)
    response.raise_for_status()
    data = response.json()
    for exercise in data["exercises"]:
        exercise_data = {
            GOOGLE_SHEET_NAME : {
                'date': today.strftime("%d/%m/%Y"),
                'time': today.strftime("%H:%M:%S"),
                'exercise': exercise["name"].title(),  # .title() maakt er 'Running' van ipv 'running'
                'duration': exercise["duration_min"],
                'calories': exercise["nf_calories"]
            }
        }
        push_to_sheets(exercise_data)


sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

SHEETY_ENDPOINT = "https://api.sheety.co/0c8faf7a39e989229fbb39c46afde049/myWorkouts/workouts"

def push_to_sheets(data):
    response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=data)
    response.raise_for_status()
    print("Workout added to Google Sheets")

process_exercise_data()

