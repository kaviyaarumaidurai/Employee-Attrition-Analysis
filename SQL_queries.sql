#Total Attrition Rate

SELECT COUNT(CASE WHEN attrition='Yes' THEN 1 END)*100.0/COUNT(*) AS attrition_rate
FROM employees;

#Department-wise Attrition

SELECT department, COUNT(*) AS attrition_count
FROM employees
WHERE attrition='Yes'
GROUP BY department
ORDER BY attrition_count DESC;

#Job Role Attrition

SELECT job_role, COUNT(*)
FROM employees
WHERE attrition='Yes'
GROUP BY job_role;

#Experience vs Attrition

SELECT experience, COUNT(*)
FROM employees
WHERE attrition='Yes'
GROUP BY experience
ORDER BY experience;

#Salary Impact

SELECT attrition, AVG(salary)
FROM employees
GROUP BY attrition;

#Job Satisfaction Impact

SELECT job_satisfaction, COUNT(*)
FROM employees
WHERE attrition='Yes'
GROUP BY job_satisfaction
ORDER BY job_satisfaction;