-- ============ SUPER STORE PARCTICES =================

############### HAVING CLAUSE  EXAMPLES ###############


-- Sales by City > 15000
SELECT 
	s.City,
	s.Customer_Segment, SUM(s.Sales) AS sales
FROM retails.sales_2015 s
GROUP BY s.City, s.Customer_Segment
HAVING SUM(s.Sales) > 15000
ORDER BY sales DESC;

-- Count the ORDERS top 5 by customer > 5, add sales and profit
SELECT 
	s.Customer_Name, COUNT(s.Order_ID) AS orders_by_customers, SUM(s.Sales) AS sales_orders, SUM(s.Profit) AS profit
FROM retails.sales_2015 s
GROUP BY s.Customer_Name
HAVING COUNT(s.Order_ID) > 5
ORDER BY orders_by_customers DESC
LIMIT 5;

-- Select the 50 customers with most profit > 2000, sales and disccount
SELECT 
	s.Customer_Name, SUM(s.Profit) AS profit_cust, COUNT(s.Order_ID) AS orders_cust, SUM(s.Sales) AS sales_cust, SUM(s.Discount) AS disccount_cust
FROM 	retails.sales_2015 s
GROUP BY s.Customer_Name
HAVING SUM(s.Profit) > 2000
ORDER BY profit_cust DESC
LIMIT 50;

-- Identify the 10 customers with poor profit, show the sales > 5000, orders and disccount
SELECT 
	s.Customer_Name, SUM(s.Profit) AS profit_cust, COUNT(s.Order_ID) AS orders_cust, SUM(s.Sales) AS sales_cust, SUM(s.Discount) AS disccount_cust
FROM retails.sales_2015 s
GROUP BY s.Customer_Name
HAVING SUM(s.Sales) > 5000
ORDER BY profit_cust ASC
LIMIT 10;


-- identify the products with order quantity > 5 and sales > 5000
SELECT DISTINCT 
	s.Product_Name, SUM(s.Sales) AS sales_product, COUNT(s.Order_Quantity) AS order_quantity
FROM retails.sales_2015 s
GROUP BY s.Product_Name
HAVING order_quantity > 5 AND sales_product > 5000
ORDER BY order_quantity DESC;

-- identify the sales with  avg shipping cost between 35 and 50 usd
SELECT 
	s.Product_Name, SUM(s.Sales) AS sales_prod, AVG(s.Shipping_Cost) AS avg_prod
FROM retails.sales_2015 s
GROUP BY s.Product_Name
HAVING avg_prod BETWEEN 35 AND 50
ORDER BY avg_prod DESC;

-- identify the products that the shipmode is major that the avg sale
SELECT 
	s.Product_Name, AVG(s.Sales) AS sales_prod, SUM(s.Shipping_Cost) AS avg_shipmode
FROM retails.sales_2015 s
GROUP BY s.Product_Name
HAVING sales_prod < avg_shipmode;


############### SCALAR SUBQUERY  EXAMPLES ###############

-- Scalar subqueries return a single value, or exactly one row and exactly one column.

-- write a query where the avg of sales be greather than sales for:  Office Machines
-- by region an state
SELECT 
	s.Region,
	s.State,
	s.Product_SubCategory,
	s.Sales AS sales_prod
FROM retails.sales_2015 s
WHERE s.Sales > (
SELECT AVG(s1.Sales)
FROM retails.sales_2015 s1) AND s.Product_SubCategory = 'Office Machines'
ORDER BY s.Sales DESC ;

-- query the max sale by state
SELECT 
	s.State,
	s.Sales
FROM retails.sales_2015 s
WHERE s.Sales = (
SELECT MAX(s1.Sales)
FROM retails.sales_2015 s1);

-- a person in Paris wants to go to the #1 place in the world for
-- snorkeling. What type of transportation goes from Paris to this place?
SELECT 
	o.City_Destination,
	o.Transportation,
	o.Travel_Time,
	o.Ticket_Price
FROM retails.one_way_ticket o
WHERE o.City_Destination = (
SELECT 
		b.Closest_City
FROM retails.best_10_places b
WHERE b.Activity = 'snorkeling' AND b.Ranking_Position = 1
) AND o.City_Origin = 'Paris';

-- a customer who wants to go from Paris to Bariloche. Before buying the 
-- ticket, the customer wants to see if there are any places with a cheaper ticket.
SELECT 
	o.City_Destination,
	o.Transportation,
	o.Ticket_Price
FROM retails.one_way_ticket o
WHERE o.Ticket_Price < (
SELECT 
		w.Ticket_Price
FROM retails.one_way_ticket w
WHERE w.City_Destination = 'Bariloche' AND w.City_Origin = 'Paris';
)

-- Our next example uses the IN operator. Let’s suppose the person who asked 
-- about the best place for snorkeling wants to explore other destinations; 
-- in fact, they’d like to see the top three snorkeling places
SELECT 
	o.City_Destination,
	o.Transportation,
	o.Ticket_Price,
	o.Travel_Time
FROM retails.one_way_ticket o
WHERE o.City_Destination IN (
SELECT 
		b.Closest_City
FROM retails.best_10_places b
WHERE b.Ranking_Position <= 3 AND b.Activity = 'snorkeling'
) AND o.City_Origin = 'Paris';

-- Suppose the travel agency’s owner wants to show every city along with the ticket 
-- cost and the number of “best places” near this city.
SELECT 
	o.City_Destination,
	o.Ticket_Price,
	tbl.quantity
FROM retails.one_way_ticket o
JOIN (
SELECT 
		b.Closest_City AS city, COUNT(*) AS quantity
FROM retails.best_10_places b
GROUP BY 1) tbl ON o.City_Destination = tbl.city;

-- let’s suppose our customer from Paris wants to travel to a place where they
-- can do both trekking and snorkeling
SELECT 
	o.City_Destination,
	o.Transportation,
	o.Ticket_Price,
	o.Travel_Time
FROM retails.one_way_ticket o
WHERE EXISTS (
SELECT b.Closest_City
FROM retails.best_10_places b
WHERE b.Activity = 'snorkeling' AND b.Closest_City = o.City_Destination
) AND EXISTS (
SELECT b1.Closest_City
FROM retails.best_10_places b1
WHERE b1.Activity = 'trekking' AND b1.Closest_City = o.City_Destination
) AND o.City_Origin = 'Paris';

-- Suppose we want to promote all the “world’s best places” you 
-- can visit with a ticket under $1,000
SELECT 
	b.Place_Name,
	b.Activity,
	b.Ranking_Position
FROM retails.best_10_places b
WHERE 1000 > ANY (
SELECT o.Ticket_Price
FROM retails.one_way_ticket o
WHERE o.City_Destination = b.Closest_City
);

-- query the employees of sales with salary > 5000 in the year 2000
SELECT 
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
FROM employee.employees e
INNER JOIN employee.dept_emp de ON de.emp_no = e.emp_no
INNER JOIN employee.departments d ON d.dept_no = de.dept_no
WHERE e.emp_no IN (
SELECT s.emp_no
FROM employee.salaries s
WHERE s.salary > 50000 AND SUBSTRING(s.from_date,1,4) = '2000'
) AND d.dept_name = 'Sales';

-- Extract the max salary of employee
SELECT 
	s.emp_no,
	e.first_name,
	e.last_name,
	s.salary
FROM employee.salaries s
INNER JOIN employee.employees e ON e.emp_no = s.emp_no
WHERE s.salary = (
SELECT MAX(s1.salary)
FROM employee.salaries s1
);

-- extract the employees with max salary > avg salary
SELECT 
	e.first_name,
	e.last_name, MAX(s.salary) AS salary
FROM employee.salaries s
INNER JOIN employee.employees e ON e.emp_no = s.emp_no
WHERE s.salary > (
SELECT AVG(s1.salary) AS salary
FROM employee.salaries s1
)
GROUP BY e.first_name, e.last_name;


-- query the employees of research Female that have salary > avg from 1998
SELECT 
	e.first_name,
	e.last_name,
	s.from_date,
	s.salary
FROM employee.employees e
INNER JOIN employee.salaries s ON s.emp_no = e.emp_no
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
INNER JOIN employee.departments d ON d.dept_no = de.dept_no
WHERE s.salary > (
SELECT AVG(s1.salary) AS salary
FROM employee.salaries s1
) AND d.dept_name = 'Research' AND
LEFT(s.from_date,4) > '1997' AND e.gender = 'F';

-- count the number of employees by deparment
SELECT 
	d.dept_name,
	emp.quantity_emp
FROM employee.departments d
JOIN (
SELECT 
		de.dept_no AS dept_no, COUNT(*) AS quantity_emp
FROM employee.dept_emp de
GROUP BY 1
) emp ON d.dept_no = emp.dept_no
ORDER BY d.dept_name ASC;

-- select the departments with employees > 25000
SELECT 
	d.dept_name
FROM employee.departments d
WHERE 25000 > (
SELECT COUNT(*) AS quantity_emp
FROM employee.dept_emp de
WHERE de.dept_no = d.dept_no
);

############### MULTIROW SUBQUERY  EXAMPLES ###############
-- Multirow subqueries return either:
--  * One column with multiple rows (i.e. a list of values), or
--  * Multiple columns with multiple rows (i.e. tables).

-- Query the employees with deparment from 1998
SELECT 
	e.first_name,
	e.last_name
FROM employee.employees e
WHERE e.emp_no IN (
SELECT 
		de.emp_no
FROM employee.dept_emp de
WHERE
LEFT(de.from_date,4) > '2000'
); 

-- query all employees with salary < 50000 in the year 2000
SELECT 
	*
FROM employee.employees e
WHERE e.emp_no IN (
SELECT 
		s.emp_no
FROM employee.salaries s
WHERE s.salary > 5000 AND
LEFT(s.from_date,4) = '2000'
);

-- query all employees and salaries with salary < 50000 in the year 2000
SELECT 
	e.first_name,
	e.last_name,
	e.gender,
	sal.salary,
	sal.emp_no
FROM employee.employees e
JOIN (
SELECT 
		s.emp_no AS emp_no, MAX(s.salary) AS salary
FROM employee.salaries s
WHERE s.salary < 50000 AND
LEFT(s.from_date,4) = '2000'
GROUP BY 1
) sal ON e.emp_no = sal.emp_no
ORDER BY sal.salary DESC;

############### CORRELETED SUBQUERY  EXAMPLES ###############

-- Correlated subqueries, where the inner query relies on information obtained 
-- from the outer query.

-- query the total of employees by deparment
SELECT DISTINCT 
	d.dept_name,
	(
SELECT COUNT(*) AS emp
FROM employee.dept_emp de1
WHERE de1.dept_no = d.dept_no
	) AS emp
FROM employee.dept_emp de
JOIN employee.departments d ON d.dept_no = de.dept_no
ORDER BY emp DESC;

-- query the avg salary by deparment
SELECT 
	avg_dep.dept_no,
	d.dept_name,
	avg_dep.avg_sal
FROM employee.departments d
JOIN (
SELECT de.dept_no AS dept_no, AVG(s.salary) AS avg_sal
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no
) avg_dep ON avg_dep.dept_no = d.dept_no
ORDER BY avg_dep.avg_sal DESC;


############### CTE COMMON TABLE EXPRESSIONS EXAMPLES ###############

-- A Common Table Expression (CTE), also referred to as a WITH clause, is a 
-- temporary named result set that you can reference anywhere in your query.

-- Query Correlated, calculated the avg salary by deparment
SELECT 
	avg_dep.dept_no,
	d.dept_name,
	avg_dep.avg_sal
FROM employee.departments d
JOIN (
SELECT de.dept_no AS dept_no, AVG(s.salary) AS avg_sal
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no
) avg_dep ON avg_dep.dept_no = d.dept_no
ORDER BY avg_dep.avg_sal DESC;

-- now with cte
WITH avg_department AS 
	(
SELECT de.dept_no AS dept_no, AVG(s.salary) AS avg_sal
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no 
	)
SELECT
	d.dept_name,
	a.avg_sal
FROM employee.departments d
INNER JOIN avg_department a ON a.dept_no = d.dept_no
ORDER BY a.avg_sal DESC;

-- obtain the average, the min and max salary by department
WITH avg_salary_department AS 
	(
SELECT de.dept_no AS dept_no, AVG(s.salary) AS avg_sal
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no 
	),
	 min_salary_department AS (
SELECT de.dept_no AS dept_no, MIN(s.salary) AS min_sal
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no 
	),
	 max_salary_department AS (
SELECT de.dept_no AS dept_no, MAX(s.salary) AS max_sal
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no 
	)
SELECT
	a.dept_no,
	a.avg_sal,
	m.min_sal,
	mx.max_sal
FROM avg_salary_department a
JOIN min_salary_department m ON m.dept_no = a.dept_no
JOIN max_salary_department mx ON mx.dept_no = a.dept_no
ORDER BY a.avg_sal DESC;

-- Query the employees that have > 10 years as senior and < 10 years as junior by department
-- until year 2000
WITH senior_employees AS 
	(
SELECT 
			de.dept_no, COUNT(de.emp_no) AS total_emp_sen
FROM employee.employees e
JOIN employee.dept_emp de ON de.emp_no = e.emp_no
WHERE 2001-
LEFT(e.hire_date, 4) > 9
GROUP BY de.dept_no
	),

 junior_employees AS 
	(
SELECT 
			de.dept_no, COUNT(de.emp_no) AS total_emp_jun
FROM employee.employees e
JOIN employee.dept_emp de ON de.emp_no = e.emp_no
WHERE 2001-
LEFT(e.hire_date, 4) < 9
GROUP BY de.dept_no
)
SELECT 
	s.dept_no,
	s.total_emp_sen,
	j.total_emp_jun
FROM senior_employees s
JOIN junior_employees j ON s.dept_no = j.dept_no


-- query the employees by department avg salary above and below
WITH avg_department_salary AS 
	(
SELECT de.dept_no, AVG(s.salary) AS avg_salary
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no
	),
	
	above_avg_department AS 
	(
SELECT de.dept_no, COUNT(*) AS employees_above_avg
FROM employee.employees e
INNER JOIN employee.dept_emp de ON de.emp_no = e.emp_no
JOIN employee.salaries s ON s.emp_no = de.emp_no
JOIN avg_department_salary a ON a.dept_no = de.dept_no
WHERE s.salary > a.avg_salary
GROUP BY de.dept_no		
	),
	
	below_avg_department AS 
	(
SELECT de.dept_no, COUNT(*) AS employees_below_avg
FROM employee.employees e
INNER JOIN employee.dept_emp de ON de.emp_no = e.emp_no
JOIN employee.salaries s ON s.emp_no = de.emp_no
JOIN avg_department_salary a ON a.dept_no = de.dept_no
WHERE s.salary < a.avg_salary
GROUP BY de.dept_no		
	)
SELECT 
	a.dept_no,
	a.avg_salary,
	ab.employees_above_avg,
	bl.employees_below_avg
FROM avg_department_salary a
JOIN above_avg_department ab ON ab.dept_no = a.dept_no
JOIN below_avg_department bl ON bl.dept_no = a.dept_no

-- query the salaries and the avg by departement and avg by employee and find the difference
WITH total_avg AS 
	(
SELECT 
			de.dept_no, AVG(s.salary) AS avg_salaries_department
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no
	),
	avg_by_employee AS (
SELECT 
			s.emp_no, AVG(s.salary) AS avg_salary_employee
FROM employee.salaries s
GROUP BY s.emp_no
	)
SELECT 
	de.emp_no,
	av.avg_salary_employee,
	ta.avg_salaries_department,
	(av.avg_salary_employee- ta.avg_salaries_department) AS diff
FROM avg_by_employee av
JOIN employee.dept_emp de ON de.emp_no = av.emp_no
JOIN total_avg ta ON ta.dept_no = de.dept_no
WHERE (av.avg_salary_employee- ta.avg_salaries_department) > 1;


-- query the salary hihgest by department
WITH avg_salaries_deparment AS 
	(
SELECT 
			de.dept_no, AVG(s.salary) AS avg_salaries_department
FROM employee.salaries s
INNER JOIN employee.dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no
	)
SELECT DISTINCT
	a.dept_no, MAX(a.avg_salaries_department) AS max_salary
FROM avg_salaries_deparment a
GROUP BY a.dept_no
ORDER BY max_salary DESC
LIMIT 1
;

############### WINDOW FUNCTIONS EXAMPLES ###############
-- WINDOW FUNCTIONS
-- Compute their result based on a sliding window frame, a set of rows 
-- that are somehow related to the current row.

-- query and ranked the salary by department
SELECT
		d.dept_no,
		d.dept_name,
		de.emp_no,
		s.salary, RANK() OVER(PARTITION BY d.dept_name
ORDER BY s.salary DESC) AS dep_sal_rank
FROM employee.salaries s
JOIN employee.dept_emp de ON de.emp_no = s.emp_no
JOIN employee.departments d ON d.dept_no = de.dept_no
LIMIT 20


-- query the sales by region and ranked
SELECT 
	s.State,
	s.Region,
	s.Sales, RANK() OVER (PARTITION BY s.State
ORDER BY s.Sales DESC) AS sales_rank
FROM retails.sales_2015 s;

-- find out where each States  ranks in relation to the top sales
SELECT 
	s.State,
	s.Region,
	s.Sales,
	s.Sales / MAX(s.Sales) OVER (PARTITION BY s.State
ORDER BY s.Sales DESC) AS sales_metric
FROM retails.sales_2015 s
LIMIT 10;

-- calculate the variation of shipping cost of order 59781
SELECT 
	s.Customer_Name,
	s.Sales,
	s.Discount,
	s.Shipping_Cost,
	LEAD(s.Shipping_Cost) OVER (PARTITION BY s.Customer_Name
	ORDER BY s.Shipping_Cost) - s.Shipping_Cost 						AS var_dis
FROM retails.sales_2015 s
WHERE s.Order_ID = 59781
ORDER BY s.Order_ID DESC;

-- calculate the variation of product margin of order 52068
SELECT 
	s.Order_ID,
	s.Customer_Name,
	s.Sales,
	s.Product_Base_Margin,
	LEAD(s.Product_Base_Margin) OVER (PARTITION BY s.Customer_Name ORDER BY s.Product_Base_Margin)
	- s.Product_Base_Margin AS var_product_margin 
FROM retails.sales_2015 s
WHERE s.Order_ID = 52068
ORDER BY s.Order_ID DESC;

-- calculate the avg in a column by each row and calculate the percent

SELECT 
	s.Region,
	s.State,
	s.Sales,
	AVG(s.Sales) OVER() AS avg_sales,
	s.Sales / AVG(s.Sales) OVER() * 100 - 100 sales_over_avg
FROM retails.sales_2015 s
ORDER BY s.Sales DESC;

-- order by the sales by product in top 10
SELECT 
	s.Product_Category,
	s.Product_Name,
	s.Sales,
	RANK() OVER (ORDER BY s.Sales DESC ) AS sales_rank
FROM retails.sales_2015 s
LIMIT 10;

-- query the top 10 of customers with sales desc

SELECT 
	s.Customer_Segment,
	s.Customer_Name,
	s.Sales,
	RANK() OVER(ORDER BY s.Sales DESC ) AS sales_rank
FROM retails.sales_2015 s
LIMIT 10;

-- query the top 10 of customers with low sales

SELECT
	s.Customer_Segment,
	s.Customer_Name,
	s.Sales,
	RANK() OVER(ORDER BY s.Sales ASC ) AS sales_rank
FROM retails.sales_2015 s
LIMIT 10;

-- query the total sales by city and rank by product
SELECT 
	s.City,
	s.Product_Name,
	s.Sales,
	SUM(s.Sales) OVER(PARTITION BY s.City) AS total_sales
FROM retails.sales_2015 s
ORDER BY s.Sales DESC;

-- query the total sales by state and rank the customer segment
SELECT 
	s.Region,
	s.Customer_Segment,
	s.Sales,
	SUM(s.Sales) OVER(PARTITION BY s.Customer_Segment) AS total_sales_seg
FROM retails.sales_2015 s
ORDER BY s.Sales DESC;

-- query the total sales by customer and product subcategory
SELECT 
	s.Customer_Name,
	s.Product_SubCategory,
	s.Sales,
	SUM(s.Sales) OVER (PARTITION BY s.Product_SubCategory) AS total_sales_psub
FROM retails.sales_2015 s
ORDER BY s.Sales DESC;

-- query the total sales and partition by customer and product subcategory
SELECT 
	s.City,
	s.Product_Name,
	s.Product_SubCategory,
	s.Sales,
	SUM(s.Sales) OVER (PARTITION BY s.Product_SubCategory, s.Product_Name ORDER BY s.City) AS cumm
FROM retails.sales_2015 s
ORDER BY s.Sales DESC;

-- query the total sales by month and customer order by state

SELECT 
	MONTH(s.Order_Date) AS month_order,
	s.Customer_Name,
	s.State,
	s.Sales,
	SUM(s.Sales) OVER (PARTITION BY MONTH(s.Order_Date), s.Customer_Name ORDER BY s.State) AS cumm
FROM retails.sales_2015 s 
ORDER BY s.Sales DESC;

-- other examples



-- ORDER BY SUM(s.Sales) DESC;24701