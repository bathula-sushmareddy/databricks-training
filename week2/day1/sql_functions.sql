--1 – Employee Compensation Classification
SELECT
    emp_id,
    INITCAP(emp_name) AS emp_name,
    department,
    ROUND(base_salary + COALESCE(bonus,0)) AS total_income,
    EXTRACT(YEAR FROM joining_date) AS joining_year,
    CASE
        WHEN DATE_PART('year', AGE(CURRENT_DATE, joining_date)) > 7 THEN 'Senior'
        WHEN DATE_PART('year', AGE(CURRENT_DATE, joining_date)) BETWEEN 4 AND 7 THEN 'Mid'
        ELSE 'Junior'
    END AS employee_level
FROM employee_payments;

--2 Order Delivery Delay Analysis
SELECT
    order_id,
    UPPER(customer_name) AS customer_name,
    order_date,
    COALESCE(delivery_date, CURRENT_DATE) AS delivery_date,
    COALESCE(delivery_date, CURRENT_DATE) - order_date AS delivery_days,
    TRUNC(order_amount,1) AS truncated_amount,
    CASE
        WHEN delivery_date IS NULL THEN 'Pending'
        WHEN delivery_date = order_date THEN 'Same-day'
        WHEN delivery_date - order_date > 3 THEN 'Delayed'
        ELSE 'On Time'
    END AS delivery_status
FROM orders_delivery;

--3 – Customer Spending Pattern
SELECT
    INITCAP(cust_name) AS customer_name,
    TO_CHAR(purchase_date,'Month') AS purchase_month,
    ROUND(purchase_amount) AS rounded_amount,
    ABS(purchase_amount) AS absolute_amount,
    CASE
        WHEN purchase_amount > 15000 THEN 'High Spender'
        WHEN purchase_amount BETWEEN 8000 AND 15000 THEN 'Medium Spender'
        ELSE 'Low Spender'
    END AS spender_category
FROM customer_spending;

--4 – Subscription Validity Check
SELECT
    user_id,
    SPLIT_PART(user_email,'@',2) AS email_domain,
    AGE(end_date,start_date) AS subscription_duration,
    TO_CHAR(subscription_fee,'99,99,999.99') AS formatted_fee,
    end_date - CURRENT_DATE AS remaining_days,
    CASE
        WHEN end_date < CURRENT_DATE THEN 'Expired'
        WHEN end_date - CURRENT_DATE <= 30 THEN 'Expiring Soon'
        ELSE 'Active'
    END AS subscription_status
FROM subscriptions;

--5 – Loan EMI Risk Categorization
SELECT
    loan_id,
    UPPER(customer_name) AS customer_name,
    POWER((1 + interest_rate/100),1.0/12) AS monthly_interest,
    DATE_PART('year', AGE(CURRENT_DATE, loan_start)) AS years_since_loan,
    ROUND(loan_amount * (interest_rate/100)/12) AS emi,
    CASE
        WHEN interest_rate > 9 THEN 'High Risk'
        WHEN interest_rate BETWEEN 8 AND 9 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_category
FROM loan_details;

--6 – Employee Attendance Evaluation
SELECT
    LOWER(emp_name) AS employee_name,
    ROUND((present_days * 100.0)/total_days,2) AS attendance_percentage,
    TO_CHAR(record_date,'Month') AS month_name,
    total_days - present_days AS absent_days,
    CASE
        WHEN (present_days * 100.0)/total_days >= 90 THEN 'Excellent'
        WHEN (present_days * 100.0)/total_days BETWEEN 75 AND 89 THEN 'Average'
        ELSE 'Poor'
    END AS attendance_status
FROM attendance;

--7 – Product Discount Validation
SELECT
    product_id,
    INITCAP(product_name) AS product_name,
    ABS(mrp - selling_price) AS discount_amount,
    ROUND(((mrp - selling_price)/mrp) * 100,2) AS discount_percentage,
    TO_CHAR(sale_date,'Day') AS sale_day,
    CASE
        WHEN selling_price < mrp THEN 'Valid Discount'
        WHEN selling_price > mrp THEN 'Overpriced'
        ELSE 'No Discount'
    END AS discount_status
FROM product_sales;

--8 – Insurance Policy Aging
SELECT
    policy_id,
    UPPER(holder_name) AS holder_name,
    DATE_PART('year', AGE(policy_end, policy_start)) AS policy_duration,
    policy_end - CURRENT_DATE AS remaining_days,
    ROUND(premium_amount) AS rounded_premium,
    CASE
        WHEN policy_end < CURRENT_DATE THEN 'Expired'
        WHEN DATE_PART('year', AGE(policy_end, policy_start)) >= 3 THEN 'Long Term'
        ELSE 'Mid Term'
    END AS policy_status
FROM insurance_policies;

--9 – Salary Increment Simulation
SELECT
    emp_id,
    LOWER(emp_name) AS employee_name,
    DATE_PART('year', AGE(CURRENT_DATE, last_hike)) AS years_since_hike,
    CASE
        WHEN rating = 5 THEN current_salary * 0.20
        WHEN rating = 4 THEN current_salary * 0.10
        ELSE 0
    END AS increment_amount,
    ROUND(
        current_salary +
        CASE
            WHEN rating = 5 THEN current_salary * 0.20
            WHEN rating = 4 THEN current_salary * 0.10
            ELSE 0
        END
    ) AS new_salary,
    CASE
        WHEN rating = 5 THEN 'High Increment'
        WHEN rating = 4 THEN 'Moderate'
        ELSE 'No Increment'
    END AS increment_status
 FROM salary_revision;

--10 – Customer Account Status Evaluation
SELECT
    account_id,
    customer_name,
    ABS(balance) AS absolute_balance,
    CURRENT_DATE - last_transaction AS days_since_transaction,
    INITCAP(branch) AS branch_name,
    SIGN(balance) AS balance_sign,
    CASE
        WHEN balance < 0 THEN 'Overdrawn'
        WHEN CURRENT_DATE - last_transaction > 365 THEN 'Dormant'
        ELSE 'Active'
    END AS account_status
FROM bank_accounts;

--level-1
--1 – Salary Risk Flagging Based on Tax Shock
SELECT
    LOWER(emp_name) AS employee_name,
    ROUND(salary - (salary * tax_percent/100)) AS net_salary,
    EXTRACT(YEAR FROM last_revision) AS revision_year,
    DATE_PART('month', AGE(CURRENT_DATE,last_revision)) AS months_since_revision,
    CASE
        WHEN tax_percent > 20
             AND DATE_PART('month', AGE(CURRENT_DATE,last_revision)) > 24
        THEN 'Tax Shock'
        WHEN tax_percent BETWEEN 15 AND 20
        THEN 'Review Needed'
        ELSE 'Stable'
    END AS status
FROM salary_audit;

--2– Bonus Abuse Detection
SELECT
    INITCAP(emp_name) AS employee_name,
    ROUND((bonus/base_salary) * 100,2) AS bonus_percentage,
    TO_CHAR(bonus_date,'Day') AS bonus_day,
    ABS(base_salary - bonus) AS salary_bonus_difference,
    CASE
        WHEN (bonus/base_salary) * 100 > 30
             AND TO_CHAR(bonus_date,'Day') IN ('Saturday ','Sunday   ')
        THEN 'Suspicious'
        WHEN (bonus/base_salary) * 100 <= 20
        THEN 'Normal'
        ELSE 'Audit'
    END AS audit_status
FROM bonus_monitor;

--3 – Experience Parity Validation
SELECT
    UPPER(emp_name) AS employee_name,
    DATE_PART('year', AGE(CURRENT_DATE, joining_date)) AS actual_experience,
    declared_experience - DATE_PART('year', AGE(CURRENT_DATE, joining_date))
        AS experience_difference,
    FLOOR(salary) AS floor_salary,
    CASE
        WHEN declared_experience > DATE_PART('year', AGE(CURRENT_DATE, joining_date))
        THEN 'Overstated'
        WHEN declared_experience < DATE_PART('year', AGE(CURRENT_DATE, joining_date))
        THEN 'Understated'
        ELSE 'Matched'
    END AS experience_status
FROM employee_experience;

--4 – Salary Digit Pattern Analysis
SELECT
    RIGHT(emp_name,2) AS last_two_characters,
    EXTRACT(DAY FROM credit_date) AS credit_day,
    TRUNC(salary) AS truncated_salary,
    MOD(TRUNC(salary),10) AS salary_mod,
    CASE
        WHEN MOD(TRUNC(salary),10) = EXTRACT(DAY FROM credit_date)
        THEN 'Pattern Match'
        ELSE 'No Match'
    END AS pattern_status
FROM salary_digits;

--5 – Odd–Even Salary Compliance
SELECT
    LOWER(emp_name) AS employee_name,
    TO_CHAR(payment_date,'Day') AS weekday_name,
    ROUND(salary) AS rounded_salary,
    MOD(ROUND(salary),2) AS salary_mod,
    CASE
        WHEN MOD(ROUND(salary),2)=0
             AND EXTRACT(DAY FROM payment_date)%2 = 1
        THEN 'Violation'
        ELSE 'Compliant'
    END AS compliance_status
FROM payroll_control;

--6 – Salary Inflation Drift
SELECT
    INITCAP(emp_name) AS employee_name,
    DATE_PART('year', AGE(CURRENT_DATE,last_hike)) AS years_since_hike,
    POWER(DATE_PART('year', AGE(CURRENT_DATE,last_hike)),2) AS inflation_power,
    ROUND(salary * POWER(1.05,
          DATE_PART('year', AGE(CURRENT_DATE,last_hike)))) AS salary_impact,
    CASE
        WHEN DATE_PART('year', AGE(CURRENT_DATE,last_hike)) > 5
        THEN 'High Inflation Risk'
        WHEN DATE_PART('year', AGE(CURRENT_DATE,last_hike)) BETWEEN 3 AND 5
        THEN 'Moderate'
        ELSE 'Low'
    END AS inflation_status
FROM inflation_watch;

--level-2
--1 – Employee Login Discipline & Performance Classification
SELECT
    INITCAP(emp_name) AS employee_name,
    CASE
        WHEN EXTRACT(DOW FROM login_time) IN (0,6)
        THEN 'Weekend'
        ELSE 'Weekday'
    END AS login_day_type,
    ROUND(EXTRACT(EPOCH FROM (logout_time - login_time))/3600,2)
        AS working_hours,
    CASE
        WHEN EXTRACT(DOW FROM login_time) NOT IN (0,6)
             AND EXTRACT(EPOCH FROM (logout_time - login_time))/3600 >= 8
        THEN 'Good Performer'
        WHEN EXTRACT(DOW FROM login_time) NOT IN (0,6)
             AND EXTRACT(EPOCH FROM (logout_time - login_time))/3600 < 6
        THEN 'Bad Performer'
        ELSE 'Weekend Login'
    END AS performance_status
FROM employee_login;

--2 – Past 7 Days Attendance & Productivity Check
SELECT
    UPPER(emp_name) AS employee_name,
    CASE
        WHEN login_date >= CURRENT_DATE - INTERVAL '7 days'
        THEN 'Within Last 7 Days'
        ELSE 'Old Record'
    END AS attendance_period,
    CASE
        WHEN EXTRACT(DOW FROM login_date) IN (0,6)
        THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    (logout_time - login_time) AS working_hours,
    CASE
        WHEN login_date >= CURRENT_DATE - INTERVAL '7 days'
             AND (logout_time - login_time) >= TIME '08:00:00'
        THEN 'Active & Productive'
        WHEN login_date >= CURRENT_DATE - INTERVAL '7 days'
             AND (logout_time - login_time) < TIME '08:00:00'
        THEN 'Active but Low Hours'
        ELSE 'Absent from Last 7 Days'
    END AS productivity_status
FROM attendance_log;

--3 – Weekend Work Abuse Detection
SELECT
    TO_CHAR(work_date,'Day') AS work_day,
    LOWER(emp_name) AS employee_name,
    EXTRACT(EPOCH FROM (logout_time - login_time))/3600 AS working_hours,
    CEIL(EXTRACT(EPOCH FROM (logout_time - login_time))/3600) AS rounded_hours,
    CASE
        WHEN EXTRACT(DOW FROM work_date) IN (0,6)
             AND EXTRACT(EP



