--Find the total cost of each customer's orders. Output customer's id, first name, and the total order cost. 
--Order records by customer's first name alphabetically.
select c.id as id,
    c.first_name,
    sum(o.total_order_cost) as total_order_cost
from customers as c
    join orders as o on c.id = o.cust_id
group by c.id
order by c.first_name