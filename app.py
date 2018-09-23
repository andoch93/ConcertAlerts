import json
import urllib2

artistSearch = raw_input('Search for an artist: ')

# api url from ticketmaster that extracts all events with Haken as a keyword
url = "https://app.ticketmaster.com/discovery/v2/events.json?keyword=" + artistSearch + "&countryCode=US&apikey=cEi2G5zNlAiLrkjwXHXusWpMfLTKsy8M"

# loading the json from api call into json object for parsing
urlJson = json.load(urllib2.urlopen(url))

# extract all items from the embedded object
eventsList = urlJson['_embedded']['events']

for event in eventsList:
    artist = event['name']
    date = event['dates']['start']['localDate']
    venue = event['_embedded']['venues'][0]['name']
    print(date + ': ' + artist + ' at ' + venue)
