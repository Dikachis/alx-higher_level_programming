-- This script lists all shows contained in hbtn_0d_tvshows without a genre linked.

-- Get the data using left join, where the right key is NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id is NULL
ORDER BY tv_shows.title;
