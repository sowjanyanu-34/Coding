#175 Leetcode
SELECT p.firstname,p.lastname,a.city,a.state
FROM Person p
INNER JOIN 
Address a
ON p.personId=a.personId;

//LEETCODE 176
# Write your MySQL query statement below
SELECT MAX(SALARY) AS SecondHighestSalary FROM EMPLOYEE WHERE SALARY<
(SELECT MAX(SALARY) FROM EMPLOYEE);

//leetcode 177
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
    SELECT DISTINCT SALARY 
    FROM EMPLOYEE
    ORDER BY SALARY
    LIMIT 1 OFFSET N
  );
END

#Leetcode 181 
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;

# Leetcode 182 duplicate Emails:
SELECT email as Email
FROM person
GROUP BY email
HAVING COUNT(email)>1; 



