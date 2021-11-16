# adding FOREIGN KEY
# CREATE TABLE image(id SERIAL PRIMARY KEY NOT NULL, name VARCHAR(100) UNIQUE,
# profile_id INTEGER NOT NULL, FOREIGN KEY (profile_id) REFERENCES employees(id));

# JOIN
# SELECT e.id, e.name, i.image, i.profile_id, e.email, i.name FROM employees e JOIN image i ON e.id = i.profile_id;
# SELECT e.id, e.name, i.image, e.email, i.profile_id, i.name FROM employees e LEFT JOIN image i ON e.id = i.profile_id;
# SELECT e.id, e.name, i.image, e.email, i.profile_id, i.name FROM employees e RIGHT JOIN image i ON e.id = i.profile_id;

# group by -> having -> order by

# SELECT name, COUNT(name) FROM employees GROUP BY name HAVING COUNT(name)>1;