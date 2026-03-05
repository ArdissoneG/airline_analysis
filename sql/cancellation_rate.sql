SELECT
    a.AIRLINE,
    SUM(f.CANCELLED) * 1.0 / COUNT(*) AS cancellation_rate
FROM flights f
JOIN airlines a
ON f.AIRLINE = a.IATA_CODE
GROUP BY a.AIRLINE
ORDER BY cancellation_rate DESC;