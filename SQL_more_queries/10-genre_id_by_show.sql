-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT sh.title, genres.genre_id
FROM tv_shows sh
-- return when the valueas are the same
INNER JOIN tv_show_genres genres
ON sh.id = genres.show_id
ORDER BY sh.title, genres.genre_id ASC;
