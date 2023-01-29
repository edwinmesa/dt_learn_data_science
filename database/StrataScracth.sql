
-- find jill and eva
select 
    cust_id,
    first_name,
    order_date,
    order_details,
    total_order_cost
from customers c 
    inner join orders o 
        on o.cust_id = c.id
where first_name in ('Jill','Eva')
order by cust_id asc

-- find the popularty location from offices facebook_employees on facebook
select location, avg(cast(popularity as decimal)) as popularity
    from facebook_employees f 
    inner join facebook_hack_survey h
    on f.id = h.employee_id
group by location    

-- show the average by city and property_type in airbnb_search_details
select 
    avg(cast(bathrooms as float)) as avg_bathrooms,
    avg(cast(bedrooms as float)) as avg_bedrooms,
    city,
    property_type
from airbnb_search_details    
group by city,property_type    
    
-- SHOW the difference in days 	
SELECT distinct user_id
 FROM (
    SELECT user_id,
        DATEDIFF(day, created_at, LEAD(created_at) 
            OVER (PARTITION BY user_id ORDER BY user_id, created_at )) AS day_diff
     FROM amazon_transactions) AS d
WHERE day_diff <= 7     

-- find the user with most transactions in a period of time
select top 1 first_name, sum(total_order_cost) as daily, order_date from customers c 
    inner join orders o
    on o.cust_id = c.id
where order_date between '2019-02-01' and '2019-05-01'
group by first_name,order_date
order by daily desc

-- find the acceptance by rate
WITH Dataset AS(
    SELECT 
    A.user_id_sender,
    A.user_id_receiver,
    A.date,
    A.action AS SentAction,
    B.action AS AccepAction
    FROM fb_friend_requests A 
    LEFT JOIN fb_friend_requests B
        ON A.user_id_sender = B.user_id_sender
       AND A.user_id_receiver = B.user_id_receiver
       AND A.action = 'sent'
       AND B.action = 'accepted'
    WHERE B.action != 'sent' OR  A.action != 'accepted'
    )
-- SELECT * FROM Dataset;
select 
    date, 
    count(sentAction) AS SentCnt, 
    count(AccepAction) AS AccepCnt, 
    cast(count(AccepAction)as float)/count(sentAction) AS AcceptRate 
From Dataset
Group By date;   
-- user_id_sender:
-- user_id_receiver:
-- date:
-- action:

-- show the Customer Revenue In March
SELECT 
    cust_id, 
    sum(total_order_cost) as total_revenue 
    FROM orders
WHERE order_date between '2019-03-01' AND '2019-03-31'
group by cust_id
order by total_revenue desc

-- Highest Energy Consumption
-----UNION OF DATA
WITH energyConsuption AS(
    SELECT * FROM fb_eu_energy
    UNION
    SELECT * FROM fb_asia_energy
    UNION 
    SELECT * FROM fb_na_energy
)
,
dataEnergyAgg as (
    SELECT 
    date, 
    RANK() OVER(order by sum(consumption) desc) as ranks,
    sum(consumption) as totalEnergyCons
    FROM energyConsuption
    GROUP BY date)
    
SELECT 
    date, 
    totalEnergyCons 
FROM dataEnergyAgg
WHERE ranks = 1


-- Users By Average Session Time
WITH avgST AS (
    SELECT 
        user_id,
        DATEDIFF(SECOND, MAX(CASE WHEN action = 'page_load'
                        THEN timestamp
                        END),
                     MIN(CASE WHEN action = 'page_exit'
                        THEN timestamp
                        END)
                )                                               AS session_time
    FROM facebook_web_log
    GROUP BY user_id, CAST(timestamp AS DATE)
    )


-- SELECT * FROM avgST;    
SELECT 
     user_id,
     ROUND(SUM(session_time)*1.0/COUNT(session_time), 1) as session_time
FROM avgST
WHERE session_time IS NOT NULL
GROUP BY user_id


-- Monthly Percentage Difference
SELECT 
    created_month,
    -- tot,
    ROUND((CAST (tot as FLOAT) - LAG(tot) OVER (ORDER BY created_month)) / LAG(tot) OVER (ORDER BY created_month), 4) * 100 AS percent_change
FROM (
    SELECT 
        CONVERT(CHAR(7), created_at, 120) AS created_month,
        SUM(value) as tot
    FROM sf_transactions
    GROUP BY CONVERT(CHAR(7), created_at, 120)
) AS result ;



-- Popularity Percentage
-- Find the popularity percentage for each user on Meta/Facebook.
WITH cte AS (
SELECT  user1, COUNT(DISTINCT user2) AS user1_friend
FROM facebook_friends
GROUP BY user1
),
cte2 AS (
SELECT  user2, COUNT(DISTINCT user1) AS user2_friend
FROM facebook_friends
GROUP BY user2
)

SELECT user1, (menber_count*1.0/total_menber)*100 AS percentage
FROM(
    SELECT 
        user1, 
        SUM(user1_friend) AS menber_count,
        MAX(user1) OVER() AS total_menber
    FROM(
        SELECT * FROM
        cte
        UNION ALL
        SELECT * FROM
        cte2) AS td_01
    GROUP BY user1    
    ) AS final_td


-- Marketing Campaign Success [Advanced]
SELECT 
    COUNT(DISTINCT user_id) as count_user
FROM (
    SELECT
        DENSE_RANK() OVER (PARTITION BY user_id ORDER BY created_at) as rank1,
        DENSE_RANK() OVER (PARTITION BY user_id, product_id ORDER BY created_at) as rank2,
        user_id,
        product_id,
        created_at
    FROM marketing_campaign) data
WHERE
    rank1>1 AND rank2=1


-- Host Popularity Rental Prices
SELECT 
    pop_rating,
    MIN(price) as min_pop,
    AVG(price) as avg_pop,
    MAX(price) as max_pop
FROM
    (
    SELECT 
        host_id,
        price,
        CASE 
            WHEN num_reviews = 0 THEN 'New'
            WHEN num_reviews BETWEEN 1 AND 5 THEN 'Rising'
            WHEN num_reviews BETWEEN 6 AND 15 THEN 'Trending Up'
            WHEN num_reviews BETWEEN 16 AND 40 THEN 'Popular'
            WHEN num_reviews > 40 THEN 'Hot'
            ELSE 'N/A'
        END pop_rating
    FROM (
         SELECT
         CONCAT(price, room_type, host_since, zipcode, number_of_reviews) as host_id,
         price,
         SUM(number_of_reviews) as num_reviews
         FROM airbnb_host_searches
         GROUP BY CONCAT(price, room_type, host_since, zipcode, number_of_reviews), price) dt    
         ) dt2   
GROUP BY pop_rating             




with bus_prev_time as(
    SELECT
        id,
        origin,
        destination,
        coalesce(prevtime, '00:00') as prev_time,
        Time
    FROM
        (
            SELECT
                id,
                origin,
                destination,
                Time,
                lag(Time) over(
                    partition by origin,
                    destination
                    order by
                        Time asc
                ) as prevtime
            FROM
                buses
        ) a
),
passenger as (
    SELECT
        origin,
        destination,
        time
    FROM
        passengers
)
SELECT
    a.id,
    sum(a.passcount) as passengers_on_board
FROM
    (
        SELECT
            b.id,
            case
                when p.time is null then 0
                else 1
            end as passcount
        FROM
            bus_prev_time b
            left join passenger p on b.origin = p.origin
            and b.destination = p.destination
            and p.time between b.prev_time
            and b.Time
    ) a
group by
    a.ID
order by
    a.ID