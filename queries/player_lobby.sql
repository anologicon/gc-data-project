DROP TABLE IF EXISTS tb_player_lobby;
CREATE TABLE tb_player_lobby AS 

	SELECT 
		tlsp.*,
		CASE WHEN qtKill > qtDeath THEN 1 ELSE 0 END AS  isKdPositive,
		qtKill / qtDeath AS kdRatio,
		qtShots / qtHits AS shotsHitsRatio,
		(qtHits / qtShots * 100) AS shotsHitsPercentage,
		qtShots - qtHits AS missingShots,
		(qtHitHeadshot / qtHits) * 100 AS qtHitHeadshotPercentage,
		(qtHitChest / qtHits) * 100 AS qtHitChestPercentage, 
		(qtHitStomach / qtHits) * 100 AS qtHitStomachPercentage, 
		(qtHitLeftAtm / qtHits) * 100 AS qtHitLeftAtmPercentage, 
		(qtHitRightArm / qtHits) * 100 AS qtHitRightArmPercentage, 
		(qtHitLeftLeg / qtHits) * 100 AS qtHitLeftLegPercentage,
		(qtAssist / qtDeath) * 100 AS assistDeathRatio,
		CASE WHEN qtRoundsPlayed < 16 THEN 1 ELSE 0 END AS abandonedLobby,
		CASE WHEN descMapName = 'de_mirage' THEN  1 ELSE 0 END AS de_mirage_map,      
		CASE WHEN descMapName = 'de_inferno' THEN  1 ELSE 0 END AS de_inferno_map,     
		CASE WHEN descMapName = 'de_dust2' THEN  1 ELSE 0 END AS de_dust2_map,       
		CASE WHEN descMapName = 'de_vertigo' THEN  1 ELSE 0 END AS de_vertigo_map,     
		CASE WHEN descMapName = 'de_overpass' THEN  1 ELSE 0 END AS de_overpass_map,    
		CASE WHEN descMapName = 'de_nuke' THEN  1 ELSE 0 END AS de_nuke_map,        
		CASE WHEN descMapName = 'de_train' THEN  1 ELSE 0 END AS de_train_map,         
		CASE WHEN descMapName = 'de_ancient' THEN  1 ELSE 0 END AS de_ancient_map
	FROM tb_lobby_stats_player tlsp
;


