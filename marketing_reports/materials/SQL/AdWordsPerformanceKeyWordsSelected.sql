SELECT
	CASE Device
		WHEN 'Computer' THEN 'Desktop'
		WHEN 'Mobile' THEN 'Mobile'
		WHEN 'Tablet' THEN 'Tablet'
	END AS Device,
	TrafficDate,
	KeywordID,
	Keyword,
	MatchType,    
	SUM(Impressions) AS Impressions,
	SUM(Clicks) AS Clicks,
	SUM(Cost) AS Cost,
	CONVERT(FLOAT,SUM(Clicks))/(0.0000001 + CONVERT(FLOAT,SUM(Impressions))) AS CTR,
	SUM(AvgPosition*Impressions)/(0.0000001 + CONVERT(FLOAT,SUM(Impressions))) AS AvgPosition,
	SUM(Cost)/(0.0000001 + CONVERT(FLOAT,SUM(Clicks))) AS AvgCPC,
	SUM(QualityScore*Impressions)/(0.0000001 + CONVERT(FLOAT,SUM(Impressions))) AS AvgQualityScore,
	AVG(MaxCPC) AS AvgMaxCPC,
	AVG(SearchImpressionShare) AS AvgSearchImpressionShare
From tblA
WHERE TrafficDate BETWEEN @dateStart AND @DateEnd
AND OTBAccount = 'UK'
-- 'Sunshine UK'
AND CampaignState IS NOT NULL
AND Keyword IN ('@KeyWordList')
GROUP BY
	CASE Device
		WHEN 'Computer' THEN 'Desktop'
		WHEN 'Mobile' THEN 'Mobile'
		WHEN 'Tablet' THEN 'Tablet'
	END,
	TrafficDate,
	KeywordID,
	Keyword,
	MatchType