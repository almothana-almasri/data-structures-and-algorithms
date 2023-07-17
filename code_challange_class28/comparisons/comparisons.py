movies = [
    {'title': 'The Matrix', 'year': 1999},
    {'title': 'Taxi Driver', 'year': 1976},
    {'title': 'The Message', 'year': 1976},
    {'title': 'Amadeus', 'year': 1984},
    {'title': 'V for Vendetta', 'year': 2005},
    {'title': 'The Silence of the Lambs', 'year': 1991},
]

def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_by_title(movies):
    def ignore_leading_articles(title):
        articles = ['A ', 'An ', 'The ']
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    return sorted(movies, key=lambda movie: ignore_leading_articles(movie['title']))

sorted_by_year = sort_by_year(movies)
print("Sorted by year:")
for movie in sorted_by_year:
    print(f"{movie['year']} - {movie['title']}")

sorted_by_title = sort_by_title(movies)
print("\nSorted by title:")
print([movie['title'] for movie in sorted_by_title])

