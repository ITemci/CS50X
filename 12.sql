select title from movies
join stars on movies.id = stars.movie_id
where person_id in (select id from people where name = 'Bradley Cooper' or name = 'Jennifer Lawrence')
group by movies.title
having count(distinct stars.person_id) = 2;
