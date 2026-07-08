from datetime import datetime
def transform(data):

    transformed_data = {
        "date": datetime.now(),
        "ville":data["name"],
        "temperature":data["main"]["temp"],
        "humidity":data["main"]["humidity"],
        "pression":data["main"]["pressure"],
        "description":data["weather"][0]["description"],
    }

    return transformed_data