import imdb
import pandas as pd


# Load movies and initialize blank columns
movies = pd.read_csv('./movies.csv', header = 0)
movies['Year'] = [''  for mov in movies['Name']]
movies['Title'] = [''  for mov in movies['Name']]
movies['Cover URL'] = [''  for mov in movies['Name']]
# Iterate over and fetch data where available
ia = imdb.IMDb()
for i, mov in enumerate(movies['Name']):
    try:
        search_results = ia.search_movie(mov)
        movies['Year'].loc[i] = search_results[0]['year']
        movies['Title'].loc[i] = search_results[0]['title']
        cover_url = search_results[0]['cover url']
        cover_url = cover_url[:cover_url.rindex('._V1_')]
        movies['Cover URL'].loc[i] = cover_url
        print('Success for: ', mov)
    except:
        print('Failed for: ', mov)
# Print and save the data
print(movies)
movies.to_csv('moviesAndCovers.csv', index=False)
