import http.server
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

PORT = 3000


class Server(BaseHTTPRequestHandler):

    ## TODO put this data in separate file
    movies = [
    {
        "Title": "Frozen", "Year": "2013",
        "Ratings": [{"Source": "Internet Movie Database", "Value": "7.5/10"}, {"Source": "Rotten Tomatoes", "Value": "89%"}, {"Source": "Metacritic", "Value": "74/100"}],
        "Response": "True"
    },
    {
        "Title": "Spiderman", "Year": "1990",
        "Ratings": [{"Source": "Internet Movie Database", "Value": "5.7/10"}], "Metascore": "N/A", "imdbRating": "5.7", "imdbVotes": "90",
        "Response": "True"
    }
    ]


    no_key = {
        "Response": "False",
        "Error": "No API key provided."
    }

    not_found =  {
        "Response":"False",
        "Error": "Movie not found!"
    }

    def _set_headers(self):
        self.send_header('Content-type', 'application/json')


    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        print(query)
        print(parsed.path)

        if 'apikey' not in query:
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(self.no_key), 'utf-8'))


        elif 't' in query:
            movies = [m for m in self.movies if m["Title"] == query['t'][0]]

            if movies:
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(movies[0]), 'utf-8'))

            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(self.not_found), 'utf-8'))


        # Otherwise, send 404 not found
        else:
            self.send_error(404, 'Not Found')
            self.send_header('Content-type', 'text/plain')
            self.end_headers()



def run(server_class=HTTPServer, handler_class=Server, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()




## Help https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET
## https://gist.github.com/bradmontgomery/2219997
