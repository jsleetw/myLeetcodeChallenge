# Write your MySQL query statement below
#select FirstName, LastName, City, State
#from Person as a, Address as b where a.PersonId = b.PersonId

select FirstName, LastName, City, State from Person LEFT JOIN Address on Person.PersonId = Address.PersonId
