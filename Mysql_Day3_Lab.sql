Choose database
mysql> use prajyotdb;
Database changed
Create table Employee
mysql> create table Employee(emp_id int primary key not null,first_name varchar(50) not null,last_name varchar(50) not null,age int not null,email varchar(50) not null);
Query OK, 0 rows affected (0.06 sec)

mysql> desc Employee;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| emp_id     | int         | NO   | PRI | NULL    |       |
| first_name | varchar(50) | NO   |     | NULL    |       |
| last_name  | varchar(50) | NO   |     | NULL    |       |
| age        | int         | NO   |     | NULL    |       |
| email      | varchar(50) | NO   |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
5 rows in set (0.01 sec)
Task 1:Insertion of records in employee table
INSERT INTO Employee (emp_id, first_name, last_name, age, email)
    -> VALUES
    ->     (1, 'John', 'Doe', 28, 'john.doe@example.com'),
    ->     (2, 'Alice', 'Smith', 35, 'alice.smith@example.com'),
    ->     (3, 'Bob', 'Johnson', 40, 'bob.johnson@example.com'),
    ->     (4, 'Emma', 'Brown', 22, 'emma.brown@example.com'),
    ->     (5, 'Michael', 'Davis', 29, 'michael.davis@example.com');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

Show records
mysql> select * from employee;
+--------+------------+-----------+-----+---------------------------+
| emp_id | first_name | last_name | age | email                     |
+--------+------------+-----------+-----+---------------------------+
|      1 | John       | Doe       |  28 | john.doe@example.com      |
|      2 | Alice      | Smith     |  35 | alice.smith@example.com   |
|      3 | Bob        | Johnson   |  40 | bob.johnson@example.com   |
|      4 | Emma       | Brown     |  22 | emma.brown@example.com    |
|      5 | Michael    | Davis     |  29 | michael.davis@example.com |
+--------+------------+-----------+-----+---------------------------+
5 rows in set (0.00 sec)
Task 2: Retrieving first_name and last_name of all employees
select first_name,last_name from employee;
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| John       | Doe       |
| Alice      | Smith     |
| Bob        | Johnson   |
| Emma       | Brown     |
| Michael    | Davis     |
+------------+-----------+
5 rows in set (0.00 sec)
Task 3: Filtering Employees Older Than 30
select first_name,last_name,age from employee where age > 30;
+------------+-----------+-----+
| first_name | last_name | age |
+------------+-----------+-----+
| Alice      | Smith     |  35 |
| Bob        | Johnson   |  40 |
+------------+-----------+-----+
2 rows in set (0.00 sec)
Task 4: Updating Employee Age (+1 for employees older than 25)
update employee set age = age+1 where age > 25;
Query OK, 4 rows affected (0.01 sec)
Rows matched: 4  Changed: 4  Warnings: 0
select * from employee;
+--------+------------+-----------+-----+---------------------------+
| emp_id | first_name | last_name | age | email                     |
+--------+------------+-----------+-----+---------------------------+
|      1 | John       | Doe       |  29 | john.doe@example.com      |
|      2 | Alice      | Smith     |  36 | alice.smith@example.com   |
|      3 | Bob        | Johnson   |  41 | bob.johnson@example.com   |
|      4 | Emma       | Brown     |  22 | emma.brown@example.com    |
|      5 | Michael    | Davis     |  30 | michael.davis@example.com |
+--------+------------+-----------+-----+---------------------------+
5 rows in set (0.00 sec)


