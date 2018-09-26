import json
import urllib2

# creation of event class constructor
class Event():
    def __init__(self, artist, date, venue, city, state):
        self.artist = artist
        self.date = date
        self.venue = venue
        self.city = city
        self.state = state

    def __str__(self):
        return self.date + ': ' + self.artist + ' at ' + self.venue + ' in ' + self.city + ', ' + self.state

    def set_artist(self, artist):
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_venue(self, venue):
        self.venue = venue

    def get_venue(self):
        return self.venue

    def set_city(self, city):
        self.artist = city

    def get_city(self):
        return self.city

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


# takes in user input for artist search. This value is passed into the keyword
# parameter for ticketmaster's api call
artist_search = raw_input('Search for an artist: ')
print('\n')

# api url from ticketmaster that extracts all events using user input as keyword
url = "https://app.ticketmaster.com/discovery/v2/events.json?keyword=" + artist_search + "&countryCode=US&apikey=cEi2G5zNlAiLrkjwXHXusWpMfLTKsy8M"

# loading the json from api call into json object for parsing
url_json = json.load(urllib2.urlopen(url))

# extract all items from the embedded object
events_info = url_json['_embedded']['events']

# creation of list of events
list_of_events = []

# collects all relevant event info and appends it to a list of events from json object returned by ticketmaster's api
for event in events_info:
    artist = event['name']
    date = event['dates']['start']['localDate']
    venue = event['_embedded']['venues'][0]['name']
    city = event['_embedded']['venues'][0]['city']['name']
    state = event['_embedded']['venues'][0]['state']['stateCode']
    list_of_events.append(Event(artist, date, venue, city, state))

# prints list of events
index = 0   
for event in list_of_events:
    print(list_of_events[index])
    index += 1
print('\n')
