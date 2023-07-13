-- listing all bands that use glam rock
-- calculating how long theyve been together
SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
	FROM metal_bands
	WHERE style LIKE '%Glam rock%'
	ORDER BY lifespan DESC;
