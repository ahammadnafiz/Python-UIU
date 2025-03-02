import time

import requests

url = "https://api.adviceslip.com/advice"
advice_set = set()

while len(advice_set) < 100:
    response = requests.get(url)

    if response.status_code == 200:
        advice = response.json().get("slip", {}).get("advice")

        if advice and advice not in advice_set:
            advice_set.add(advice)
            print(f"{len(advice_set)}: {advice}")

    time.sleep(1)

print("\nCollected 100 unique pieces of advice!")

with open("advice.txt", "w", encoding="utf-8") as file:
    for idx, advice in enumerate(advice_set, start=1):
        file.write(f"{idx}. {advice}\n")
