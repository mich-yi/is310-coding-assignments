favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 2003,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]

# print(favorite_movies)

# total_favorite_movies = len(favorite_movies)
# print("How many total favorite movies do we have?", total_favorite_movies)

# print(type(favorite_movies), type(favorite_movies[0]))

# print('Enter your favorite movie of the last year:')
# recent_favorite_movie = input()
# print('Your favorite movie is of the last year:', recent_favorite_movie)

# favorite_movies[0]['long_description'] = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. The Waschowskis created a plot set in a dystopian future where humanity is unknowingly trapped inside a simulated reality, the Matrix, created by intelligent machines to distract humans while using their bodies as an energy source. In the movie, the main character, Neo, is a computer programmer who learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the Matrix."
# print(favorite_movies[0])

# split_description = favorite_movies[0]['long_description'].split(' ')
# print(split_description)

# print(len(split_description))

# favorite_movies[0]['short_description'] = ' '.join(split_description[:10])
# print(favorite_movies[0]['short_description'])

# print(' '.join(split_description))

# edited_description = favorite_movies[0]['long_description'].replace('the Wachowskis', 'Lana and Lilly Wachowski')
# print(edited_description)

# edited_description = favorite_movies[0]['long_description'].replace('the Wachowskis', 'Lana and Lilly Wachowski', 1)
# print(edited_description)

# print(favorite_movies[0]['long_description'].lower())
# print(favorite_movies[0]['long_description'].upper())
# print(favorite_movies[0]['long_description'].title())
# print(favorite_movies[0]['long_description'].strip())

def movie_before_2000(name):
    if name['release_year'] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return name
    
recent_movies = []

for movie in favorite_movies:
    before_2000 = movie_before_2000(movie)
    if before_2000 is None:
        pass
    else:
        recent_movies.append(before_2000)

print(recent_movies)
