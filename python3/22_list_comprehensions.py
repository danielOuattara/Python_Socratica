# !bin/bash
# Daniel OUATTARA
# 24 06 2024
#


"""

List: [ 1, 2, "a",.14]

ListComprehensions:
    [ expr for val in collection ]
    [ expr for val in collection if <test> ]
    [ expr for val in collection if <test_1> and <test_2> ]
    [ expr for val_1 in collection_1 if and  val_2 in collection_2 ]

"""

# Example: List of squares

squares_1 = []
for i in range(1, 101):
    squares_1.append(i**2)
print(f'\nsquares_1 = {squares_1}')

print('-' * 30)

squares_2 = [i**2 for i in range(1, 101)]
print(f'\nsquares_2 = {squares_2}')

# Example: List of reminder

remainders_5 = [i**2 % 5 for i in range(1, 101)]
print(f'\nremainders_5 = {remainders_5}')

#

remainders_11 = [i**2 % 11 for i in range(1, 101)]
print(f'\nremainders_11 = {remainders_5}')


# Example: Movies list

movies_list = [
    "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Return of the King", "Forrest Gump", "Inception", "The Matrix", "The Lord of the Rings: The Fellowship of the Ring", "Fight Club", "Star Wars: Episode V - The Empire Strikes Back", "The Godfather: Part II", "The Lord of the Rings: The Two Towers", "Interstellar", "Parasite", "Gladiator", "Jurassic Park", "The Lion King", "Back to the Future", "Titanic", "The Avengers", "Star Wars: Episode IV - A New Hope", "The Silence of the Lambs", "Schindler's List", "Saving Private Ryan", "The Green Mile", "Se7en", "Braveheart", "The Departed", "The Prestige", "Whiplash", "Mad Max: Fury Road", "Guardians of the Galaxy", "The Social Network", "Inglourious Basterds", "Django Unchained", "Spider-Man: Into the Spider-Verse", "The Dark Knight Rises", "Avengers: Endgame", "Avengers: Infinity War", "Toy Story", "Toy Story 3", "Finding Nemo", "WALL-E", "Up", "Coco", "Inside Out", "Shrek", "Ratatouille", "The Incredibles", "Monsters, Inc.", "Zootopia", "Frozen", "Moana", "Beauty and the Beast", "Aladdin", "Mulan", "The Little Mermaid", "Cinderella", "Snow White and the Seven Dwarfs", "Fantasia", "The Wizard of Oz", "E.T. the Extra-Terrestrial", "Jaws", "Raiders of the Lost Ark", "Indiana Jones and the Last Crusade", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Prisoner of Azkaban", "The Hunger Games", "The Maze Runner", "Divergent", "Twilight", "The Fault in Our Stars", "A Beautiful Mind", "Good Will Hunting", "The Pursuit of Happyness", "Slumdog Millionaire", "The Great Gatsby", "The Curious Case of Benjamin Button", "A Star Is Born", "La La Land", "Les Misérables", "The Sound of Music", "West Side Story", "Singin' in the Rain", "My Fair Lady", "Grease", "Mamma Mia!", "Chicago", "The Phantom of the Opera", "The Greatest Showman", "Bohemian Rhapsody", "Rocketman", "Amadeus", "Moulin Rouge!", "Breakfast at Tiffany's", "Gone with the Wind", "Casablanca", "Citizen Kane", "It's a Wonderful Life", "One Flew Over the Cuckoo's Nest", "A Clockwork Orange"
]

title_movies = []
for movie in movies_list:
    if movie.startswith("G"):
        title_movies.append(movie)

print(f'title_movies = {title_movies}')

#

title_movies_2 = [movie for movie in movies_list if movie.startswith("G")]
print(f'title_movies_2 = {title_movies_2}')

#

movies_list_2 = [
    ("The Shawshank Redemption", 1994), ("The Godfather", 1972), ("The Dark Knight", 2008), ("Pulp Fiction", 1994), ("The Lord of the Rings: The Return of the King", 2003), ("Forrest Gump", 1994), ("Inception", 2010), ("The Matrix", 1999), ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Fight Club", 1999), ("Star Wars: Episode V - The Empire Strikes Back", 1980), ("The Godfather: Part II", 1974), ("The Lord of the Rings: The Two Towers", 2002), ("Interstellar", 2014), ("Parasite", 2019), ("Gladiator", 2000), ("Jurassic Park", 1993), ("The Lion King", 1994), ("Back to the Future", 1985), ("Titanic", 1997), ("The Avengers", 2012), ("Star Wars: Episode IV - A New Hope", 1977), ("The Silence of the Lambs", 1991), ("Schindler's List", 1993), ("Saving Private Ryan", 1998), ("The Green Mile", 1999), ("Se7en", 1995), ("Braveheart", 1995), ("The Departed", 2006), ("The Prestige", 2006), ("Whiplash", 2014), ("Mad Max: Fury Road", 2015), ("Guardians of the Galaxy", 2014), ("The Social Network", 2010), ("Inglourious Basterds", 2009), ("Django Unchained", 2012), ("Spider-Man: Into the Spider-Verse", 2018), ("The Dark Knight Rises", 2012), ("Avengers: Endgame", 2019), ("Avengers: Infinity War", 2018), ("Toy Story", 1995), ("Toy Story 3", 2010), ("Finding Nemo", 2003), ("WALL-E", 2008), ("Up", 2009), ("Coco", 2017), ("Inside Out", 2015), ("Shrek", 2001), ("Ratatouille", 2007), ("The Incredibles", 2004), ("Monsters, Inc.",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    2001), ("Zootopia", 2016), ("Frozen", 2013), ("Moana", 2016), ("Beauty and the Beast", 1991), ("Aladdin", 1992), ("Mulan", 1998), ("The Little Mermaid", 1989), ("Cinderella", 1950), ("Snow White and the Seven Dwarfs", 1937), ("Fantasia", 1940), ("The Wizard of Oz", 1939), ("E.T. the Extra-Terrestrial", 1982), ("Jaws", 1975), ("Raiders of the Lost Ark", 1981), ("Indiana Jones and the Last Crusade", 1989), ("Harry Potter and the Sorcerer's Stone", 2001), ("Harry Potter and the Prisoner of Azkaban", 2004), ("The Hunger Games", 2012), ("The Maze Runner", 2014), ("Divergent", 2014), ("Twilight", 2008), ("The Fault in Our Stars", 2014), ("A Beautiful Mind", 2001), ("Good Will Hunting", 1997), ("The Pursuit of Happyness", 2006), ("Slumdog Millionaire", 2008), ("The Great Gatsby", 2013), ("The Curious Case of Benjamin Button", 2008), ("A Star Is Born", 2018), ("La La Land", 2016), ("Les Misérables", 2012), ("The Sound of Music", 1965), ("West Side Story", 1961), ("Singin' in the Rain", 1952), ("My Fair Lady", 1964), ("Grease", 1978), ("Mamma Mia!", 2008), ("Chicago", 2002), ("The Phantom of the Opera", 2004), ("The Greatest Showman", 2017), ("Bohemian Rhapsody", 2018), ("Rocketman", 2019), ("Amadeus", 1984), ("Moulin Rouge!", 2001), ("Breakfast at Tiffany's", 1961), ("Gone with the Wind", 1939), ("Casablanca", 1942), ("Citizen Kane", 1941), ("It's a Wonderful Life", 1946), ("One Flew Over the Cuckoo's Nest", 1975), ("A Clockwork Orange", 1971)
]
released_by_year_movies = []
for movie in movies_list_2:
    if movie[1] < 2000:
        released_by_year_movies.append(movie)

print(f'title_movies = {title_movies}')

released_by_year_movies = [title for (
    title, year) in movies_list_2 if year < 2000]
print(f'released_by_year_movies {released_by_year_movies}')


# Example: vector scalar

v = [2, -3, 1]
print(f'v=  {v}')

v_3 = [x * 4 for x in v]
print(f'v_3 = {v_3}')


# Example Cartesian Product

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

A_scalar_B = [(x, y) for x in A for y in B]

print(A_scalar_B)
