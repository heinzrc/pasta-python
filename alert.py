import http.client, urllib
def alert_phone():
  conn = http.client.HTTPSConnection("pushsafer.com:443")
  conn.request("POST", "/api",
    urllib.parse.urlencode({
      "k": "",                # Your Private or Alias Key
      "m": "Water has reached boiling point",                   # Message Text
      "t": "Alert",                     # Title of message
      "i": "62",                      # Icon number 1-98
      "s": "0",                     # Sound number 0-28
      "v": "1",                 # Vibration number 0-3
    }), { "Content-type": "application/x-www-form-urlencoded" })
  response = conn.getresponse()

#print(response.status, response.reason)
#data = response.read()
#print(data)