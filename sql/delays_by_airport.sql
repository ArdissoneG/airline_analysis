SELECT
    ap.AIRPORT,
    ap.CITY,
    ap.STATE,
    AVG(f.DEPARTURE_DELAY) AS avg_delay
FROM flights f
JOIN airports ap
ON f.ORIGIN_AIRPORT = ap.IATA_CODE
GROUP BY ap.AIRPORT, ap.CITY, ap.STATE
ORDER BY avg_delay DESC
LIMIT 10;