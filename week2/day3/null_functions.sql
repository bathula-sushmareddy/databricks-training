--1. Show all employees whose salary is NULL
SELECT *
FROM Employee
WHERE salary IS NULL;

--2. Show all orders where discount is NOT NULL
SELECT *
FROM Orders
WHERE discount IS NOT NULL;

--3. Get products where category is NULL
SELECT *
FROM Products
WHERE category IS NULL;

--4. Count number of employees with NULL manager_id
SELECT COUNT(*) AS total_employees
FROM Employees
WHERE manager_id IS NULL;

--5. Replace NULL salary with 0
SELECT name,
       ISNULL(salary, 0) AS salary
FROM Employees;

--6. Replace NULL bonus with 1000
SELECT name,
       ISNULL(bonus, 1000) AS bonus
FROM Employees;

--7. Show order amount, if NULL replace with 500
SELECT order_id,
       ISNULL(amount, 500) AS amount
FROM Orders;

--8. Replace NULL stock with 0
SELECT product_name,
       ISNULL(stock, 0) AS stock
FROM Products;

--9. Show employee earnings using salary, if NULL use bonus
SELECT name,
       COALESCE(salary, bonus) AS earnings
FROM Employees;

--10. Show first available value: salary → bonus → 0
SELECT name,
       COALESCE(salary, bonus, 0) AS income
FROM Employees;

--11. Show product price, if NULL use 1000
SELECT product_name,
       COALESCE(price, 1000) AS price
FROM Products;

--12. Get customer payment using amount → discount → 0
SELECT customer_name,
       COALESCE(amount, discount, 0) AS payment
FROM Orders;

--13. Convert salary to NULL if salary = 0
SELECT name,
       NULLIF(salary, 0) AS salary
FROM Employees;

--14. Convert discount to NULL if discount = 0
SELECT order_id,
       NULLIF(discount, 0) AS discount
FROM Orders;

--15. Use NULLIF to avoid divide by zero
SELECT amount / NULLIF(discount, 0) AS result
FROM Orders;

--16. Replace coupon_code with NULL if it is 'DISC10'
SELECT order_id,
       NULLIF(coupon_code, 'DISC10') AS coupon_code
FROM Orders;

--17. Calculate total earnings (salary + bonus)
SELECT name,
       ISNULL(salary, 0) + ISNULL(bonus, 0) AS total_earnings
FROM Employees;

--18. Show employees where both salary and bonus are NULL
SELECT *
FROM Employees
WHERE salary IS NULL
AND bonus IS NULL;

--19. Show products where price is NULL but category is NOT NULL
SELECT *
FROM Products
WHERE price IS NULL
AND category IS NOT NULL;

--20. Show orders where both amount and discount are NULL
SELECT *
FROM Orders
WHERE amount IS NULL
AND discount IS NULL;

--21. Show employee income using COALESCE
SELECT name,
       COALESCE(salary, bonus, 1000) AS income
FROM Employees;

--22. Replace empty discount with NULL using NULLIF
SELECT order_id,
       NULLIF(discount, 0) AS discount
FROM Orders;

--23. Show final payable amount
SELECT order_id,
       ISNULL(amount, 0) - ISNULL(discount, 0) AS final_amount
FROM Orders;

--24. Find employees where salary is NULL but manager exists
SELECT *
FROM Employees
WHERE salary IS NULL
AND manager_id IS NOT NULL;
