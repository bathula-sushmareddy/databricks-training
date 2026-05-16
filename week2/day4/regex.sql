--1.Extract numbers present at the beginning of mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'^[0-9]+')
FROM regex_practice;

--2.Extract numbers present at the end of mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'[0-9]+$')
FROM regex_practice;

--3.Extract only the first character from mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'^.')
FROM regex_practice;

--4.Extract only the last character from mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'.$')
FROM regex_practice;

--5.Extract exactly two consecutive digits.
SELECT REGEXP_SUBSTR(mixed_value,'[0-9]{2}')
FROM regex_practice;

--6.Extract exactly one digit from mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'[0-9]')
FROM regex_practice;

--7.Extract country code from phone.
SELECT REGEXP_SUBSTR(phone,'[0-9]{1,3}')
FROM regex_practice;

--8.Extract numeric values between alphabets.
SELECT REGEXP_SUBSTR(mixed_value,'[0-9]+')
FROM regex_practice;

--9.Extract text before @ in email.
SELECT REGEXP_SUBSTR(email,'^[a-zA-Z0-9._-]+')
FROM regex_practice;

--10.Extract text after @ including domain.
SELECT REGEXP_SUBSTR(email,'@[a-zA-Z0-9.]+')
FROM regex_practice;

--11.Extract domain name without @.
SELECT REPLACE(
REGEXP_SUBSTR(email,'@[a-zA-Z0-9.]+'),
'@','')
FROM regex_practice;

--12.Extract extension after last dot.
SELECT REGEXP_SUBSTR(email,'[a-zA-Z]+$')
FROM regex_practice;

--13.Extract continuous alphabets from mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'[a-zA-Z]+')
FROM regex_practice;

--14.Extract continuous numbers from mixed_value.
SELECT REGEXP_SUBSTR(mixed_value,'[0-9]+')
FROM regex_practice;

--15.Extract first 3 characters from full_text.
SELECT REGEXP_SUBSTR(full_text,'^...')
FROM regex_practice;

--16.Extract last 2 characters from full_text.
SELECT REGEXP_SUBSTR(full_text,'..$')
FROM regex_practice;

--17.Extract employee number between text and underscore.
SELECT REGEXP_SUBSTR(full_text,'[0-9]+')
FROM regex_practice;

--18.Extract country code at end of full_text.
SELECT REGEXP_SUBSTR(full_text,'[0-9]+$')
FROM regex_practice;

--19.Extract text between underscores.
SELECT REGEXP_SUBSTR(full_text,'_[A-Z]+_')
FROM regex_practice;

--20.Extract country code after + in phone number.
SELECT REGEXP_SUBSTR(phone,'\\+[0-9]{1,3}')
FROM regex_practice;
