CREATE TABLE employee(
	employee_id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	position VARCHAR(50),
	department VARCHAR(50),
	hire_date DATE,
	salary NUMERIC(10,2)
);
INSERT INTO employee(employee_id,name,position,department,hire_date,salary)
VALUES 	 (001,'Deep','Data Analyst','Data Scientist','2022-12-25',53000.00),
		 (002,'Sonu','Data Engineer','Data Head','2022-01-01',55000.00),
		 (003,'Deepak','Data st','Data Scientist','2022-05-25',6200.00),
		 (004,'mahesh','Data em','Data Scientist','2022-09-02',65000.00),
		 (005,'Ganesh','Data En','Data Base Adm','2022-09-05',70000.00),
		 (006,'Puja','Data lea','Data Center Ch.','2025-12-25',500000.00),
		 (007,'Feary','Data pm','Data Scientist','2024-10-05',75000.00);
------------------------------------------------------------------------------------
DELETE FROM employee       -- Only use for specific row delete
WHERE employee_id='001';		
------------------------------------------------------------------------------------
SELECT * FROM employee		-- Here we can see ordinal position of salary data
ORDER BY salary DESC;
------------------------------------------------------------------------------------
TRUNCATE TABLE employee;	-- Remove only all data not a column names
------------------------------------------------------------------------------------
SELECT * FROM employee		-- Which name start letter with j if we can cnage 
WHERE name LIKE '%j';		--j% then last letter find in the name,%abc% between.
------------------------------------------------------------------------------------
SELECT * FROM employee				-- It's shows data where position in Data Analyst 
WHERE position in ('Data Analyst');
------------------------------------------------------------------------------------
SELECT * FROM employee			-- WE can see hire_date in ordinal position.
ORDER BY hire_date;
------------------------------------------------------------------------------------
SELECT name, salary				--WE can see only those data that in order position is 
FROM employee					-- highest and limit 1 means only show one data.
ORDER BY salary
LIMIT 1;
-----------------------------------------------------------------------------------
ALTER TABLE employee			-- I wnat to chnage column name to full name 
RENAME COLUMN name TO full_name;
-----------------------------------------------------------------------------------
ALTER TABLE employee		-- Remove salary column 
DROP COLUMN salary;
----------------------------------------------------------------------------------
DROP TABLE IF EXISTS employee; -- Remove Table
----------------------------------------------------------------------------------

DROP DATABASE IF EXISTS employee; -- Remove DataBase
----------------------------------------------------------------------------------
















