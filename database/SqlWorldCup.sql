create table teams (
      team_id integer not null,
      team_name varchar(30) not null,
      unique(team_id)
  );


  create table matches (
      match_id integer not null,
      host_team integer not null,
      guest_team integer not null,
      host_goals integer not null,
      guest_goals integer not null,
      unique(match_id)
  );


insert into teams values (10, 'Give');
insert into teams values (20, 'Never');
insert into teams values (30, 'You');
insert into teams values (40, 'Up');
insert into teams values (50, 'Gonna');
insert into matches values (1, 30, 20, 1, 0);
insert into matches values (2, 10, 20, 1, 2);
insert into matches values (3, 20, 50, 2, 2);
insert into matches values (4, 10, 30, 1, 0);
insert into matches values (5, 30, 50, 0, 1);


-- Implement your solution here
SELECT 
	t.team_id,
	t.team_name,
	COALESCE(SUM(mm.points),0)				as num_points
	--SUM(mm.host_goals)					as goals_scored,
	--SUM(mm.guest_goals)					as goals_received,
	--SUM(mm.host_goals-mm.guest_goals)	as goals_diff
FROM 
teams t
LEFT JOIN(
	SELECT 
		mht.host_team as team_h,
		mht.host_goals,
		mht.guest_goals,
		CASE WHEN mht.host_goals > mht.guest_goals THEN 3
			 WHEN mht.host_goals = mht.guest_goals THEN 1
			 ELSE 0
		END													AS points
	FROM matches mht
	UNION ALL
	SELECT 
		mgt.guest_team as team_g,
		mgt.host_goals,
		mgt.guest_goals,
		CASE WHEN mgt.guest_goals > mgt.host_goals THEN 3
			 WHEN mgt.guest_goals = mgt.host_goals THEN 1
			 ELSE 0
		END													AS points
	FROM matches mgt
	) mm
ON T.team_id = mm.team_h
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC, team_id ASC
--goals_diff DESC







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
        ) 
) a,
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
            left outer join passenger p on b.origin = p.origin
            and b.destination = p.destination
            and p.time between b.prev_time
            and b.Time
    ) a
group by
    a.ID
order by
    a.ID