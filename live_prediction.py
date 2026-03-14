import serial
import pickle
import numpy as np
import smtplib

# Load ML model
model = pickle.load(open("model.pkl","rb"))
encoder = pickle.load(open("encoder.pkl","rb"))

# Serial port
ser = serial.Serial('COM8',9600)

print("System Started...\n")

# Email alert function
def send_email_alert(risk, water, distance, rise):

    sender = "drainmonitor.iot@gmail.com"
    receiver = "priyaangel49467@gmail.com"
    password = "kfexctobyxeisijt"

    message = f"""
Drain Blockage Alert

Water Level: {water}
Distance: {distance}
Rise Rate: {rise}

Predicted Blockage Risk: {risk:.2f} %

Immediate inspection required.
"""

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,message)
    server.quit()

    print("Email alert sent.\n")


while True:

    line = ser.readline().decode('utf-8', errors='ignore').strip()

    # Stop condition
    if line == "Completed readings.":
        print("All readings processed.")
        break

    if line == "":
        continue

    values = line.split(",")

    if len(values) != 3:
        continue

    try:
        water = float(values[0])
        distance = float(values[1])
        rise = float(values[2])
    except:
        continue

    sample = [[water,distance,rise]]

    prediction = model.predict(sample)
    result = encoder.inverse_transform(prediction)

    prob = model.predict_proba(sample)
    risk = max(prob[0]) * 100

    print("Water Level:", water)
    print("Distance:", distance)
    print("Rise Rate:", rise)

    print("Drain Status:", result[0])
    print("Blockage Risk:", round(risk,2), "%")

    # Alert condition
    if risk > 70:
        print("⚠ HIGH RISK ALERT")
        send_email_alert(risk, water, distance, rise)

    print("----------------------")

print("Prediction stopped.")