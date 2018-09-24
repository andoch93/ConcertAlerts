import json
import urllib2

# takes in user input for artist search. This value is passed into the keyword
# parameter for ticketmaster's api call
artistSearch = raw_input('Search for an artist: ')
print('\n')

# api url from ticketmaster that extracts all events using user input as keyword
url = "https://app.ticketmaster.com/discovery/v2/events.json?keyword=" + artistSearch + "&countryCode=US&apikey=cEi2G5zNlAiLrkjwXHXusWpMfLTKsy8M"

# loading the json from api call into json object for parsing
urlJson = json.load(urllib2.urlopen(url))

# extract all items from the embedded object
eventsList = urlJson['_embedded']['events']

# prints all relevant event info from json object returned by ticketmaster's api
for event in eventsList:
    artist = event['name']
    date = event['dates']['start']['localDate']
    venue = event['_embedded']['venues'][0]['name']
    city = event['_embedded']['venues'][0]['city']['name']
    state = event['_embedded']['venues'][0]['state']['stateCode']
    print(date + ': ' + artist + ' at ' + venue + ' in ' + city + ', ' + state)

print('\n')
