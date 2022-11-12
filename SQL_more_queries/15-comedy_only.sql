-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT sh.title AS title
FROM
    tv_shows sh INNER JOIN tv_show_genres sh_ge
ON
    sh.id = sh_ge.show_id INNER JOIN tv_genres ge
ON
    ge.id = sh_ge.genre_id
WHERE
    ge.name = "Comedy"
ORDER BY
    sh.title ASC;
