from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
api_key = "pk.eyJ1IjoibmRhbHRvbjEiLCJhIjoiY2tsNWlkMHBwMTlncDJwbGNuNzJ6OGo2ciJ9.QbcnC4OnBjZU6P6JN6m3Pw"
mapURL = "https://api.mapbox.com/geocoding/v5/mapbox.places/3001%20S%20Congress%20Ave,%20Austin,%20TX%2078704.json?types=address&access_token="+api_key
response = requests.get(mapURL)
geocodeData = json.dumps(response.text)
# Mapbox Reservse Geocoding API Call
reverseGeocodingURL = "https://api.mapbox.com/geocoding/v5/mapbox.places/-97.757134,30.2321.json?access_token="+api_key
responseReverseGeocode = requests.get(reverseGeocodingURL)
reverseGeoCodeData = json.dumps(responseReverseGeocode.text)
# Mapbox Directions API Call
directionsURL = "https://api.mapbox.com/directions/v5/mapbox/driving/-97.752987,30.229009;-97.741089,30.272759?annotations=speed,distance,duration&overview=full&steps=true&access_token="+api_key+"&depart_at=2021-03-14T15:00"
responseDirections = requests.get(directionsURL)
directionsData = json.dumps(responseDirections.text)


class MapBoxAPIExample(BaseHTTPRequestHandler):
    # Respond to GET requests from the client
    def do_GET(self):
        path = self.path

        # This is the URI or block of code which will execute when the client requests the address: 'http://localhost:8082'
        if path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            encodedString = geocodeData.encode('utf-8')
            # Write the encoded string (the write function in this package only accepts bytes data) back to the client's browser
            self.wfile.write(encodedString)
        if path == '/getreversegeocode':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            encodedString = reverseGeoCodeData.encode('utf-8')
            # Write the encoded string (the write function in this package only accepts bytes data) back to the client's browser
            self.wfile.write(encodedString)

        if path == '/getdirections':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            encodedString = directionsData.encode('utf-8')
            # Write the encoded string (the write function in this package only accepts bytes data) back to the client's browser
            self.wfile.write(encodedString)


# Turn the app server on at port 8082 and fork it
if __name__ == "__main__":
    serverPort = 8082
    hostName = "localhost"
    appServer = HTTPServer((hostName, serverPort), MapBoxAPIExample)
    print("Server started http://%s:%s $ (hostName, serverPort)")

    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    print("Server stopped")