  create table buses (
      id integer primary key,
      origin varchar(255) not null,
      destination varchar(255)  not null,
      time varchar(255)  not null,
      unique (origin, destination, time)
  );

  create table passengers (
      id integer primary key,
      origin varchar(255)  not null,
      destination varchar(255)  not null,
      time varchar(255)  not null
  );

insert into buses values (10, 'Warsaw', 'Berlin', '10:55');
insert into buses values (20, 'Berlin', 'Paris', '06:20');
insert into buses values (21, 'Berlin', 'Paris', '14:00');
insert into buses values (22, 'Berlin', 'Paris', '21:40');
insert into buses values (30, 'Paris', 'Madrid', '13:30');
insert into passengers values (1, 'Paris', 'Madrid', '13:30');
insert into passengers values (2, 'Paris', 'Madrid', '13:31');
insert into passengers values (10, 'Warsaw', 'Paris', '10:00');
insert into passengers values (11, 'Warsaw', 'Berlin', '22:31');
insert into passengers values (40, 'Berlin', 'Paris', '06:15');
insert into passengers values (41, 'Berlin', 'Paris', '06:50');
insert into passengers values (42, 'Berlin', 'Paris', '07:12');
insert into passengers values (43, 'Berlin', 'Paris', '12:03');
insert into passengers values (44, 'Berlin', 'Paris', '20:00');


SELECT * FROM buses;

SELECT * FROM passengers;

with 
bus_prev_time as(
    SELECT 
		id, 
		origin,
		destination, 
		coalesce(prevtime,'00:00') as prev_time,
		Time 
    FROM (
    SELECT 
		id, 
		origin,
		destination, 
		Time, 
		lag(Time) over(partition by origin,destination order by Time asc) as prevtime 
	FROM buses) a
			 ),
	passenger as (
	SELECT 
		origin,
		destination, 
		time 
	FROM passengers
	)

SELECT a.id, sum(a.passcount) as passengers_on_board  FROM (
SELECT b.id,
      case when p.time is null 
            then 0
      else 1 end as passcount 
FROM bus_prev_time b
left join passenger p
on b.origin = p.origin
and b.destination = p.destination
and p.time between b.prev_time and b.Time ) a 
group by a.ID
order by a.ID


----------------------------------------------------------------------------------------------------------------

  create table transactions (
        amount integer not null,
        date date not null
  );


 insert into transactions values ('1000', '2020-01-06');
insert into transactions values ('-10', '2020-01-14');
insert into transactions values ('-75', '2020-01-20');
insert into transactions values ('-5', '2020-01-25');
insert into transactions values ('-4', '2020-01-29');
insert into transactions values ('2000', '2020-03-10');
insert into transactions values ('-75', '2020-03-12');
insert into transactions values ('-20', '2020-03-15');
insert into transactions values ('40', '2020-03-15');
insert into transactions values ('-50', '2020-03-17');
insert into transactions values ('200', '2020-10-10');
insert into transactions values ('-200', '2020-10-10');


SELECT SUM(t.amount) as balance FROM transactions t
GROUP BY YEAR(t.date);

WITH monthly_credited_transactions
     AS (SELECT month(date) AS cred_month,
                Sum(CASE
                      WHEN amount < 0 THEN Abs(amount)
                      ELSE 0
                    END)                 AS credited_amount,
                Sum(CASE
                      WHEN amount < 0 THEN 1
                      ELSE 0
                    END)                 AS credited_cnt
         FROM   transactions
         GROUP  BY month(date)),
     credit_fee
     AS (SELECT ( 12 - Count(1) ) * 5 AS fee,
                1                     AS id
         FROM   monthly_credited_transactions
         WHERE  credited_amount >= 100
                AND credited_cnt >= 3),
     trans
     AS (SELECT Sum(amount) AS amount,
                1           AS id
         FROM   transactions)
SELECT amount - fee AS balance
FROM   trans a
       LEFT JOIN credit_fee b
              ON a.id = b.id 