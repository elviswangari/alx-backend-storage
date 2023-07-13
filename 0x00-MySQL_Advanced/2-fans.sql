-- script to read from tables
-- read group and orders by fanbase
-- well use SUM, AS , GROUP 
SELECT `origin`, SUM(fans) AS `nb_fans` 
	FROM `metal_bands` 
	GROUP BY `origin`
	ORDER BY `nb_fans` DESC;
