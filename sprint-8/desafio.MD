# Desafio Parte 2 - Ingestão de dados do TMBD

Escolhi a categoria de filmes **Guerra**.

Pretendo trazer as informações de *renda*, *orçamento*, *popularidade*, *idioma original* e *nota média*.

A análise que pretendo trazer é referente renda e orçamento (lucro ou prejuízo), e a popularidade. Além disso
o idioma original para entender se países além dos que utilizam o idioma inglês, conseguem ter um resultado e popularidade maior, 
ou isso realmente está concentrado mais nos que são de idioma inglês.

## Endpoints que devo usar

* Gênero = 10752: https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&page={page} 
    Traz filmes com o gênero escolhido
* A partir dessas ids que eu receber dos filmes de Crime, usarei nesse endpoint para buscar as informações:
    https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR
    
    As informações serão: 

        revenue(renda);

        budget(orçamento);

        popularity(popularidade);

        original_language(idioma original);
        
        vote_average(nota média)