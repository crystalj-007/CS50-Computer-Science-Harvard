-- Objective: Solve the mystery of the CS50 duck theft

-- Given info: theft took place on July 28 2021 at Humphrey Street

-- Check the crime scene reports from the above date and street
SELECT description FROM crime_scene_reports
WHERE day = 28 
AND month=7 
AND street='Humphrey Street';

-- Information found:
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. 
-- Interviews were conducted today with three witnesses who were present at the time  
-- Each of their interview transcripts mentions the bakery.

-- Check the transcripts from the 3 people interviewed
-- The percent sign % represents zero, one, or multiple characters
SELECT name, transcript FROM interviews
WHERE day = 28 
AND month=7 
AND year=2021
AND transcript LIKE "%bakery%";

-- Information found:
-- RUTH: Within ten minutes of theft, I saw thief get into car in bakery parking lot + drive away. 
-- Check security footage from the bakery parking lot, look for cars that left in that time frame.
-- 
-- EUGENE: I don't know the thief's name, but it was someone I recognized. 
-- Earlier this morning, before I arrived at Emma's bakery, I saw thief withdrawing money at ATM on Leggett Street .
-- 
-- RAYMOND: As thief left bakery, they called someone for less than a minute. 
-- Thief said they were taking earliest flight out of Fiftyville tomorrow. 
-- The thief asked person to buy flight ticket.

-- Check bakery security logs of people who exited parking lot between 10:15 and 10:25
SELECT name
FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE day = 28 
AND month = 7 
AND year = 2021 
AND activity = "exit" 
AND hour = 10 
AND minute >= 15 
AND minute <= 25

INTERSECT

-- and who widthdrew money that morning from Legget Street
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.atm_location = "Leggett Street" 
AND day = 28 
AND month = 7 
AND year = 2021 
AND transaction_type = "withdraw"

INTERSECT

-- and check who made a phonecall for less than a minute
SELECT DISTINCT people.name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE phone_calls.day = 28 
AND phone_calls.month = 7 
AND phone_calls.year = 2021 
AND phone_calls.duration < 60

INTERSECT

--and check who took a flight out from Fiftyville on 29th July 2021 at earliest hour
SELECT DISTINCT people.name FROM people
JOIN passengers ON passengers.passport_number=people.passport_number
JOIN flights ON flights.id=passengers.flight_id
JOIN airports ON airports.id=flights.origin_airport_id
WHERE airports.city="Fiftyville" 
AND flights.day=29 
AND flights.month=7 
AND flights.year=2021 
AND flights.hour=8; 

-- Information found:
-- Bruce is the only one who did all of the above therefore he is the thief

-- Now lets see where Bruce is flying to
SELECT airports.city from airports
JOIN flights ON flights.destination_airport_id=airports.id
JOIN passengers ON passengers.flight_id=flights.id
JOIN people ON people.passport_number=passengers.passport_number
WHERE people.name="Bruce";

-- Information found:
-- He is flying to New York

-- Now lets find the Accomplice
-- Accomplice: 
-- Find Bruce number:
SELECT phone_number FROM people
WHERE name="Bruce";

-- Bruce Number = (367) 555-5533

-- Find accomplice by finding people who received a call on 28th July 2021 whos calls were less than 60s from Bruce
SELECT DISTINCT people.name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE phone_calls.day = 28 
AND phone_calls.month = 7 
AND phone_calls.year = 2021 
AND phone_calls.duration < 60 
AND caller="(367) 555-5533";




-- Alternative method
SELECT people_receiver.name AS receiver_name
FROM phone_calls
JOIN people AS people_caller ON people_caller.phone_number = phone_calls.caller
JOIN people AS people_receiver ON people_receiver.phone_number = phone_calls.receiver
WHERE people_caller.name = 'Bruce'
AND phone_calls.day = 28
AND phone_calls.month = 7
AND phone_calls.year = 2021
AND phone_calls.duration < 60;



