Question:
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation.
The output should consist of four columns (Doctor, Professor, Singer, and Actor) in that specific order,
with their respective names listed alphabetically under each column.
Note: Print NULL when there are no more names corresponding to an occupation.
Input Format
The OCCUPATIONS table is described as follows:


Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation.
The output should consist of four columns (Doctor, Professor, Singer, and Actor) in that specific order, with their respective names listed alphabetically under each column.
Note: Print NULL when there are no more names corresponding to an occupation.


Input Format
The OCCUPATIONS table is described as follows:
Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.


ANSWEER:


SELECT
    MAX(CASE WHEN occupation = 'Doctor' THEN name END) AS Doctor,
    MAX(CASE WHEN occupation = 'Professor' THEN name END) AS Professor,
    MAX(CASE WHEN occupation = 'Singer' THEN name END) AS Singer,
    MAX(CASE WHEN occupation = 'Actor' THEN name END) AS Actor
FROM (
    SELECT
        name,
        occupation,
        ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS rn
    FROM occupations
) t
GROUP BY rn
ORDER BY rn;


-----------------------------------------------------------------------------------


Sample Output

Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria