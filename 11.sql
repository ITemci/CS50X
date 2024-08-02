select title from movies
join ratings on movies.id = ratings.movie_id
join stars on movies.id = stars.movie_id
where person_id = (select id from people where name = 'Chadwick Boseman')
order by rating desc
limit 5;
