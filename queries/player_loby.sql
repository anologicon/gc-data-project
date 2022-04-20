drop table if exists df_raw_player_loby;
create table df_raw_player_loby as

	select 
		tlsp.*,
		CASE WHEN qtKill > qtDeath THEN 1 ELSE 0 END as  isKdPositive,
		qtKill / qtDeath as kdRatio,
		qtShots / qtHits as shotsHitsRatio,
		(qtHits / qtShots * 100) as shotsHitsPercentage,
		qtShots - qtHits as missingShots,
		(qtHitHeadshot / qtHits) * 100 as qtHitHeadshotPercentage,
		(qtHitChest / qtHits) * 100 as qtHitChestPercentage, 
		(qtHitStomach / qtHits) * 100 as qtHitStomachPercentage, 
		(qtHitLeftAtm / qtHits) * 100 as qtHitLeftAtmPercentage, 
		(qtHitRightArm / qtHits) * 100 as qtHitRightArmPercentage, 
		(qtHitLeftLeg / qtHits) * 100 as qtHitLeftLegPercentage,
		CASE WHEN descMapName = 'de_mirage' THEN  1 ELSE 0 END AS de_mirage_map,      
		CASE WHEN descMapName = 'de_inferno' THEN  1 ELSE 0 END AS de_inferno_map,     
		CASE WHEN descMapName = 'de_dust2' THEN  1 ELSE 0 END AS de_dust2_map,       
		CASE WHEN descMapName = 'de_vertigo' THEN  1 ELSE 0 END AS de_vertigo_map,     
		CASE WHEN descMapName = 'de_overpass' THEN  1 ELSE 0 END AS de_overpass_map,    
		CASE WHEN descMapName = 'de_nuke' THEN  1 ELSE 0 END AS de_nuke_map,        
		CASE WHEN descMapName = 'de_train' THEN  1 ELSE 0 END AS de_train_map,         
		CASE WHEN descMapName = 'de_ancient' THEN  1 ELSE 0 END AS de_ancient_map 
	from tb_lobby_stats_player tlsp;
;
