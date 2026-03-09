# Leetcode 182 duplicate Emails
SELECT email as Email
FROM person
GROUP BY email
HAVING COUNT(email)>1; 