# Desafio Parte 2 - Ingestão de dados do TMBD

Escolhi a categoria de filmes **Crime**.

Pretendo trazer as informações de *renda*, *popularidade*, *país de produção* e *nota média*.

A análise que pretendo trazer é referente renda e popularidade com o país de produção, para entender
se países menores conseguem ter uma renda e popularidade maior, ou isso realmente está concentrado mais
nos EUA.

## Endpoints que devo usar

* Gênero = 80: https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre} 
    Traz filmes com o gênero escolhido
* A partir dessas ids que eu receber dos filmes de Crime, usarei nesse endpoint para buscar as informações:
    https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR
    As informações serão: 

        revenue(renda);

        popularity(popularidade);

        production_country(país de produção);
        
        vote_average(nota média);