---What is the total sales revenue of Samantha and Lisa?
select sum(sales_revenue) as total_revenue
from sales_performance
where salesperson = "Lisa"
    or salesperson = "Samantha"