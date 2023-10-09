SELECT d.NAME AS DEPT_NAME, AVG(s.AMT(USD)) AS AVG_MONTHLY_SALARY(USD) FROM Departments d 
JOIN Employees e on d.ID=e.DEPT ID 
JOIN Salaries s on e.ID=s.EMP_ID 
GROUP BY d.NAME 
ORDER BY AVG_MONTHLY_SALARY(USD) DESC 
LIMIT 3;
/*
In above query I joined three tables and used group by condition to group by to group the employees to their 
respective departments and used aggregate function(avg) to calculate average  salaries of each departments 
and used order by to sort in descending order and use limit to display top 3.
*/
