SELECT COUNTRY.CONTINENT, TRUNCATE(AVG(CITY.POPULATION), 0)
FROM COUNTRY
INNER JOIN CITY
ON COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY COUNTRY.CONTINENT;
