select name from people join stars on people.id = stars.person_id where movie_id = (select id from movies where title = 'Toy Story');
