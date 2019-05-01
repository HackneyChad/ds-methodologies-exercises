-- USE telco_churn;

-- SELECT *
-- FROM internet_service_types;

-- # internet_service_type_id, internet_service_type
-- '3', 'None'
-- '2', 'Fiber optic'
-- '1', 'DSL'
-- ----------------------------------

-- USE telco_churn;

-- SELECT payment_type_id, payment_type
-- FROM payment_types;

-- # payment_type_id, payment_type
-- '1', 'Electronic check'
-- '2', 'Mailed check'
-- '3', 'Bank transfer (automatic)'
-- '4', 'Credit card (automatic)'
-- ----------------------------------

# USE telco_churn;

# SELECT *
# FROM contract_types;

-- # contract_type_id, contract_type
-- '1', 'Month-to-month'
-- '2', 'One year'
-- '3', 'Two year'
-- ------------------------------------------



# Extract a table containing all customers with a 2-year contract and, include the following information:
-- customer id,
-- tenure,
-- monthly charges... and,
-- total charges.

USE telco_churn;

SELECT c.customer_id, c.tenure, c.monthly_charges, c.total_charges
FROM customers c
JOIN contract_types ct ON c.contract_type_id = ct.contract_type_id
# JOIN payment_types pt ON c.payment_type_id = pt.payment_type_id
# JOIN internet_service_types it ON c.internet_service_type_id = it.internet_service_type_id
WHERE c.contract_type_id = 3
;

# query pulled 19 Mar 19, 8:19 pm
# 1695 row(s) returned
# 0.067 sec




-- for sql syntax refresher:
-- SELECT d.dept_name, s.emp_no, s.salary, ((s.salary-72012)/17310) AS z_salary
-- FROM employees.salaries s
-- JOIN employees.dept_emp de ON s.emp_no = de.emp_no
-- JOIN departments d ON de.dept_no = d.dept_no
-- WHERE s.to_date > NOW();






