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