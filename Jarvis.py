from datetime import date, datetime
import geocoder
from geopy.geocoders import Nominatim


def get_currentTime():
   now = datetime.now()
   current_time = now.strftime("%I:%M %p")
   print("Sir, it's " + current_time)

def get_currentDate():
   this_day = date.today()
   day = int(this_day.strftime("%d"))
   if day == 1 or day == 21 or day == 31:
      print(this_day.strftime("It's %A, {}st of %b %Y ").format(day))
   elif day == 2 or day == 22:
      print(this_day.strftime("It's %A, {}nd of %b %Y ").format(day))
   elif day == 3 or day == 23:
      print(this_day.strftime("It's %A, {}rd of %b %Y ").format(day))
   elif day > 3:
      print(this_day.strftime("It's %A, {}th of %b %Y ").format(day))

def get_location():
   geoLoc = Nominatim(user_agent="GetLoc")
   g = geocoder.ip('me')
   locname = geoLoc.reverse(g.latlng)
   location = locname.address
   print(location)

