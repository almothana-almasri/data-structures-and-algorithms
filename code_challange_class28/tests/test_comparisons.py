from code_challange_class28.comparisons.comparisons import sort_by_year, sort_by_title

def test_sort_by_year():
    movies = [
        {'title': 'The Matrix', 'year': 1999, 'genres': ['Action', 'Sci-Fi']},
        {'title': 'Taxi Driver', 'year': 1976, 'genres': ['Crime', 'Drama']},
        {'title': 'The Message', 'year': 1976, 'genres': ['Biography', 'Drama', 'History']},
        {'title': 'Amadeus', 'year': 1984, 'genres': ['Biography', 'Drama', 'History', 'Music']},
        {'title': 'V for Vendetta', 'year': 2005, 'genres': ['Action', 'Drama', 'Sci-Fi', 'Thriller']},
        {'title': 'The Silence of the Lambs', 'year': 1991, 'genres': ['Crime', 'Drama', 'Thriller']},
    ]

    sorted_by_year = sort_by_year(movies)

    assert sorted_by_year[0]['year'] == 2005
    assert sorted_by_year[-1]['year'] == 1976
    assert [movie['year'] for movie in sorted_by_year] == [2005, 1999, 1991, 1984, 1976, 1976]

def test_sort_by_title():
    movies = [
        {'title': 'The Matrix', 'year': 1999, 'genres': ['Action', 'Sci-Fi']},
        {'title': 'Taxi Driver', 'year': 1976, 'genres': ['Crime', 'Drama']},
        {'title': 'The Message', 'year': 1976, 'genres': ['Biography', 'Drama', 'History']},
        {'title': 'Amadeus', 'year': 1984, 'genres': ['Biography', 'Drama', 'History', 'Music']},
        {'title': 'V for Vendetta', 'year': 2005, 'genres': ['Action', 'Drama', 'Sci-Fi', 'Thriller']},
        {'title': 'The Silence of the Lambs', 'year': 1991, 'genres': ['Crime', 'Drama', 'Thriller']},
    ]

    sorted_by_title = sort_by_title(movies)

    assert sorted_by_title[0]['title'] == 'Amadeus'
    assert sorted_by_title[-1]['title'] == 'V for Vendetta'
    assert [movie['title'] for movie in sorted_by_title] == ['Amadeus', 'The Matrix', 'The Message', 'The Silence of the Lambs', 'Taxi Driver', 'V for Vendetta']