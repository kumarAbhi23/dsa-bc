

-- window function : 

-- lets create a table of employees with their salaries and departments
CREATE TABLE employees (
    emp_id BIGINT,
    name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC
);

INSERT INTO employees (emp_id, name, department, salary) VALUES
(1, 'Alice', 'HR', 50000),
(2, 'Bob', 'HR', 55000),
(3, 'Charlie', 'IT', 60000),
(4, 'David', 'IT', 65000),
(5, 'Eve', 'Finance', 70000);

SELECT * FROM employees;

-- i wanted to find max salary in each department 

SELECT department,max(salary) as max_salary
from employees
GROUP BY department;

-- window function 
select emp_id,name,department,salary,
       max(salary) over(PARTITION BY department) as max_salary_in_dept
from employees

-- running total of slay ries in each department

SELECT emp_id, name, department, salary,
       SUM(salary) OVER (PARTITION BY department ORDER BY emp_id                
       ) AS running_total
FROM employees