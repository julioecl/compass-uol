# Leia o arquivo actors.csv e codifique os cálculos solicitados sobre o conjunto de dados utilizando a biblioteca Pandas. Adicione apenas a resposta da questões nos espaços indicados. Seu código-fonte deverá estar no Github.

# Perguntas dessa tarefa
# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')
max_movies = max(df['Number of Movies'])
max_movies_df = df.loc[df['Number of Movies'] == max_movies, ['Actor', 'Number of Movies']]
max_actor = max_movies_df['Actor'].values[0]

print(f'O ator/atriz com mais filmes é {max_actor}, com {max_movies} filmes.')

# Apresente a média da coluna contendo o número de filmes.

movies_df = pd.DataFrame(df['Number of Movies'])
mean_movies = movies_df.mean().values[0]

print(f'A média da coluna de número de filmes é {mean_movies}.')

# Apresente o nome do ator/atriz com a maior média por filme.

df = pd.read_csv('actors.csv')
max_avg_movies = max(df['Average per Movie'])
max_avg_movies_df = df.loc[df['Average per Movie'] == max_avg_movies, ['Actor', 'Average per Movie']]
max_avg_actor = max_avg_movies_df['Actor'].values[0]

print(f'O ator/atriz com a maior média por filme é {max_avg_actor}, com {max_avg_movies}.')

# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

most_freq_movies_df = df['#1 Movie'].value_counts().rename_axis('Movie').reset_index(name='Frequency')
for index, row in most_freq_movies_df.iterrows():
    print(f"O filme {row['Movie']} aparece {row['Frequency']} vez(es) no dataset.")