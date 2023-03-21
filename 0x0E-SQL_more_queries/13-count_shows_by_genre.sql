-- List all genres from hbtn_0d_tvshows and display the number of shows linked to each
-- Using COUNT and GROUP BY

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) as number_of_shows
  FROM tv_genres
  JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY tv_genres.name
  ORDER BY COUNT(tv_show_genres.genre_id) DESC;
