SELECT * FROM games JOIN games_details ON games_details.game_id = games.id JOIN release_details ON release_details.game_id = games.id;

"SELECT Plateforme, COUNT(Plateforme) FROM games GROUP BY Plateforme;"

SELECT platform, COUNt(platform) FROM release_details GROUP BY platform;

SELECT title, type, release_date, price, publisher, description, platform FROM games JOIN games_details ON games_details.game_id = games.id JOIN release_details ON release_details.game_id = games.id;

SELECT publisher, COUNT(publisher) FROM games_details GROUP BY publisher;

SELECT title , publisher, release_date FROM games JOIN games_details ON games_details.game_id = games.id ORDER BY release_date;

SELECT release_date, platform, COUNT(platform) FROM games JOIN release_details ON release_details.game_id = games.id GROUP BY platform, release_date ORDER BY release_date;

SELECT release_date, COUNT(release_date) FROM games GROUP by title ORDER BY release_date;