SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) LIKE 2021 AND CATEGORY LIKE '인문'
ORDER BY PUBLISHED_DATE 