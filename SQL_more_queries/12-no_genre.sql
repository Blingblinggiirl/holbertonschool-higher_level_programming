-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT sh.title, genres.genre_id
FROM tv_shows sh
LEFT JOIN tv_show_genres genres
ON sh.id = genres.show_id
WHERE
    genres.show_id IS NULL
ORDER BY sh.title, genres.genre_id ASC;
