#175 Leetcode
SELECT 
p.firstname,
p.lastname,
a.city,
a.state
FROM Person p
INNER JOIN 
Address a
ON p.personId=a.personId;

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



