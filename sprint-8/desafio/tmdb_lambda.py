import requests
import boto3
import pandas as pd  
import datetime
import json

import requests
import boto3
import pandas as pd  
import datetime
import json
import os

def lambda_handler(event, context):
    
    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%m')
    day = datetime.datetime.now().strftime('%d')

    s3 = boto3.client('s3')

    api_key = os.environ['tmdb_key']
    genre = 10752
    page = 1
    ids = []

    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&page={page}")
    data = response.json()
    total_pages = data['total_pages']

    for page in range(1, total_pages+1):    
        response_genre = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&page={page}")
        data = response_genre.json() 
        if 'results' not in data:
            break
        for movie in data['results']:
            ids.append({'Id': movie['id']})    
    
    df_ids = pd.DataFrame(ids)
    movies = []
    
    for movie_id in df_ids['Id']:    
        response_movies = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR")
        data = response_movies.json()
        movie = {'ImdbId': data['imdb_id'],
              'Titulo': data['original_title'],
              'Popularidade': data['popularity'],
              'IdiomaOriginal': data['original_language'],
              'Orcamento': data['budget'],
              'Renda': data['revenue'],
              'NotaMedia:': data['vote_average'], 
              'DataLancamento': data['release_date']}
        movies.append(movie)
    
    movies_json = json.dumps(movies, indent=6)  
    s3.put_object(Bucket='data-lake-julio', Key=f'Raw/TMDB/JSON/Movies/{year}/{month}/{day}/movies{day}{month}.json', Body=movies_json)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }