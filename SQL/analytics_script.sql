-- Creating facts table

create table fact_events(
	event_id serial primary key,
	user_id text,
	content_id text, 
	session_id text, 
	event_type text, 
	event_time timestamp,
	year int,
	month int,
	event_date date 
);

/*
 * Creating dimension tables
 * 1. dim_users
 * 2. dim_content
 * 3. dim_dates
*/

create table dim_users(
	user_id text primary key,
	signup_date timestamp
);

create table dim_content(
	content_id text primary key,
	title text,
	contentType text, 
	lang text
);

create table dim_dates(
	date_id serial primary key,
	date date unique,
	year int, 
	month  int, 
	day int, 
	day_of_week varchar,
	quarter int
)

truncate table dim_dates;

INSERT INTO dim_dates (date, year, month, day, day_of_week, quarter)
SELECT DISTINCT
    event_date::date AS date,       
    year,
    month,
    EXTRACT(DAY FROM event_date::date) AS day,
    TO_CHAR(event_date::date, 'Day') AS day_of_week,
    EXTRACT(QUARTER FROM event_date::date) AS quarter
FROM fact_events
ORDER BY date;


alter table fact_events 
alter column useragent type text;

ALTER TABLE fact_events
ALTER COLUMN userregion TYPE TEXT;

ALTER TABLE fact_events
ALTER COLUMN usercountry TYPE TEXT;


