'''
Install requests with
pip install requests
'''

import requests
import os


'''
Before running this code, create an OMDB key
set the OMDB_KEY environment variable on your computer
You can do it temporarily with the appropriate command,
replacing abcd1234 with your key

(PC)

set OMDB_KEY=abcd1234

(Mac)

export OMDB_KEY=abcd1234

Or, you can set permanently. Google will tell you how.
'''

movie_base_url = 'http://www.omdbapi.com/'

class OMDB_Exception(Exception):
    pass


def omdb_call(movie_name):
    key = os.environ['OMDB_KEY']  # Read key from environment variable
    params = { 't' : movie_name, 'apikey' : key  }
    return requests.get(movie_base_url, params).json()


def movie_rating(movie_name):

    data = {}

    try:
        data = omdb_call(movie_name)

    except Exception as e:
        print(e)
        raise OMDB_Exception('Error connecting to OMDB')

    try:
        if data['Response'] == 'False' :
            error_message = data['Error']
            raise OMDB_Exception(error_message)
        else:
            return data['Ratings'][0]['Value']

    except (KeyError, TypeError, IndexError) as e:
        raise OMDB_Exception('Error processing response from OMDB')


    # Valid responses reporting errors from the query include response has a field 'Response' which is true or false, and an error message
    # {'Response': 'False', 'Error': 'Movie not found!'}

    # An example valid response - with no "Response" field
    # {'Plot': 'When the newly-crowned Queen Elsa...', 'imdbVotes': '475,585', 'Released': '27 Nov 2013', 'imdbRating': '7.5', 'Rated': 'PG', 'Awards': 'Won 2 Oscars. Another 77 wins & 57 nominations.', 'Production': 'Walt Disney Pictures', 'BoxOffice': '$400,736,600', 'Website': 'http://www.disney.com/frozen', 'Year': '2013', 'Metascore': '74', 'Director': 'Chris Buck, Jennifer Lee', 'Title': 'Frozen', 'Actors': 'Kristen Bell, Idina Menzel, Jonathan Groff, Josh Gad', 'Country': 'USA', 'Response': 'True', 'imdbID': 'tt2294629', 'Runtime': '102 min', 'Genre': 'Animation, Adventure, Comedy', 'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SX300.jpg', 'Ratings': [{'Value': '7.5/10', 'Source': 'Internet Movie Database'}, {'Value': '89%', 'Source': 'Rotten Tomatoes'}, {'Value': '74/100', 'Source': 'Metacritic'}], 'Language': 'English, Norwegian', 'Writer': 'Jennifer Lee (screenplay by), Hans Christian Andersen (story inspired by "The Snow Queen" by), Chris Buck (story by), Jennifer Lee (story by), Shane Morris (story by)', 'Type': 'movie', 'DVD': '18 Mar 2014'}


def main():
    movie_name = input('Please enter movie name: ')
    try:
        rating = movie_rating(movie_name)
        print('This movie\'s rating is ' + rating)
    except OMDB_Exception as e:
        print('Error getting rating, ' + str(e))


if __name__ == '__main__':
    main()
