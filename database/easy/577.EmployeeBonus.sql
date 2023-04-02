-- first solution
select name, bonus
from employee e
left join bonus b on b.empId = e.empId
where b.bonus < 1000 or bonus is null;