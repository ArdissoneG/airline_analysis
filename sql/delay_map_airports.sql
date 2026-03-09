SELECT
    ap.AIRPORT,
    ap.CITY,
    ap.STATE,
    ap.LATITUDE,
    ap.LONGITUDE,
    AVG(f.DEPARTURE_DELAY) AS avg_delay,
    COUNT(*) AS flight_count
FROM flights f
JOIN airports ap
ON f.ORIGIN_AIRPORT = ap.IATA_CODE
WHERE f.DEPARTURE_DELAY IS NOT NULL
GROUP BY
    ap.AIRPORT,
    ap.CITY,
    ap.STATE,
    ap.LATITUDE,
    ap.LONGITUDE
HAVING COUNT(*) > 500
ORDER BY avg_delay DESC;