-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT ge.name AS name
FROM 
    tv_genres ge INNER JOIN tv_show_genres sh_ge
ON 
    ge.id = sh_ge.genre_id INNER JOIN tv_shows sh
ON
    sh.id = sh_ge.show_id
WHERE
    sh.title = "Dexter"
ORDER BY
    ge.name ASC;
