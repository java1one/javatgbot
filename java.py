import pyowm

owm = pyowm.OWM('adbe024e3c511fca6f5596d95d2e9275', language = "ru")

place = input ("В каком городе/стране? ")
observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w)

