-- my solution
SELECT IFNULL(
               (SELECT num
                FROM MyNumbers
                GROUP BY num
                HAVING COUNT(num) = 1
                ORDER BY num DESC
                   LIMIT 1),
  NULL
) AS num;

-- recommended solution
SELECT
    MAX(num) AS num
FROM
    (SELECT
        num
    FROM
        my_numbers
    GROUP BY num
    HAVING COUNT(num) = 1) AS t;