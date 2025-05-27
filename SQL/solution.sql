--------- First part of the test / Premiere partie du test 

Select p.date as vente, SUM(t.prod_price * t.prod_qty) as vente
from transactrion t
where t.date between '01/01/2019' and '31/12/2019'
group by t.date
order by t.date;


--------- second part of the test / seconde partie du test 

select client_id,
SUM(CASE WHEN pm.product_type = 'MEUBLE' then t.prod_price * t.prod_qty else 0) as ventes_meuble
SUM(CASE WHEN pm.product_type = 'DECO' then t.prod_price * t.prod_qty else 0) as ventes_deco
from transactrion t 
join PRODUCT_NOMENCLATURE pm
on t.prod_id = pm.product_id
where t.date between '01/01/2019' and '31/12/2019'
group by client_id;
