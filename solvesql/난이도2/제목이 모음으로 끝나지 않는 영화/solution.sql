SELECT title
FROM film
WHERE rating IN ('R', 'NC-17')
  AND title NOT REGEXP '[AEIOU]$';
