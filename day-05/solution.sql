-- Customers from Canada or USA whose company is not NULL

SELECT * 
FROM Customer
WHERE Country IN ('USA', 'Canada') 
	AND Company IS NOT NULL;