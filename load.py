import csv
import os


def load(data):
    os.makedirs("output", exist_ok=True)

    with open("output/meteo_YYYY-MM-DD.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "date",
            "ville",
            "temperature",
            "humidity",
            "pression",
            "description"
        ])

        writer.writerow([
            data["date"],
            data["ville"],
            data["temperature"],
            data["humidity"],       
            data["pression"],
            data["description"]
        ])