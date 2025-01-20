# Micropython A9G - Send GPS Data via SMS Every 1 Minute (No Altitude Condition)
# Source: Adapted from Pulkin's Micropython repository
# Author: [Your Name]

import gps
import cellular
import time

phone_number = "xxxxxxxx"  # Destination phone number

def get_gps_location():
    """Fetches GPS coordinates from the A9G module."""
    gps.on()
    time.sleep(5)  # Allow GPS to acquire a fix
    
    location = gps.get_location()

    # Ensure location is valid and has at least latitude & longitude
    if isinstance(location, tuple) and len(location) >= 2:
        latitude = location[0]
        longitude = location[1]
        altitude = location[2] if len(location) > 2 else "Unknown"  # Handle missing altitude

        gps.off()

        # Print GPS data for debugging
        print("GPS Data - Latitude: {}, Longitude: {}, Altitude: {}".format(latitude, longitude, altitude))

        # Send SMS with Google Maps URL
        return "Google Maps Location:\nhttps://www.google.com/maps?q={},{}\nAltitude: {} meters".format(latitude, longitude, altitude)
    else:
        gps.off()
        print("GPS Fix Not Available or Invalid Data:", location)
        return None

def send_sms(number, message):
    """Sends an SMS with the GPS location."""
    if message:
        sms = cellular.SMS(number, message)
        sms.send()
        print("SMS Sent to", number)
    else:
        print("No SMS sent due to GPS fix issues.")

# Main Loop: Check GPS and send SMS every 1 minute
while True:
    gps_data = get_gps_location()
    send_sms(phone_number, gps_data)
    
    print("Waiting for 1 minute before checking again...")
    time.sleep(60)  # Wait for 1 minute before checking GPS data again

