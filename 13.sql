select name from people
join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
where movies.id in
(
    select movie_id from stars
    where person_id = (select id from people where name = 'Kevin Bacon' and birth = 1958)
) and
people.id != (select id from people where name = 'Kevin Bacon' and birth = 1958)
;
