import requests

def randomApi():
    name=str(input("Enter the name: "))
    url = f"https://api.genderize.io?name={name}"
    url = "https://official-joke-api.appspot.com/random_joke?"
    url=f'https://gps.sourcecodegh.com/v1/trial/{name}'
    # ghanapost gps api

    response=requests.get(url)

    if (response.status_code!=200):
        print(response.status_code)
    else:
        print("Correct")
        print(response.json())
    

# # get location using digital address
def digitalAddress():
    address=str(input("Enter the digital address: "))
    url = "https://ghanapostgps.sperixlabs.org/get-location"

    payload = f'address={address}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.json()['data']['Table']
    print(f'Area: {data[0]["Area"]}\n Region: {data[0]["Region"]}\n District: {data[0]["District"]}\n Street: {data[0]["Street"]}\n Latitude: {data[0]["CenterLatitude"]}\n Longitude: {data[0]["CenterLongitude"]}')





def geolocation():
  # Replace with your actual API key
  API_KEY = "AIzaSyA9K4-amuDYO2_GJpw55uWw6PpPzyqneh0"
  url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"
  
  # Optional payload: cell towers and/or Wi-Fi access points data
  data = {
      "wifiAccessPoints": [
          {
              "macAddress": "01:23:45:67:89:AB",
              "signalStrength": -65,
              "signalToNoiseRatio": 40
          }
      ]
  }
  
  response = requests.post(url, json=data)
  location = response.json()
  
  # Print latitude and longitude
  print("Location:", location.get("location"))
  print("Accuracy (meters):", location.get("accuracy"))
  return location.get("location")


# # get location using latitude and longitude

def latitudeLongitude():
    # lat=str(input("Enter the latitude: "))
    # long=str(input("Enter the longitude: "))
    url = "https://ghanapostgps.sperixlabs.org/get-address"
    geo=geolocation()


    payload={'lat': geo['lat'], 'long': geo['lng']}
    files=[]
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.json())

