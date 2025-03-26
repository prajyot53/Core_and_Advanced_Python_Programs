use prajyotdb;
Database changed
mysql> desc prajyotdb;
ERROR 1146 (42S02): Table 'prajyotdb.prajyotdb' doesn't exist
mysql> CREATE TABLE departments (
    ->     department_id INT PRIMARY KEY AUTO_INCREMENT,
    ->     department_name VARCHAR(100) NOT NULL
    -> );
Query OK, 0 rows affected (0.11 sec)

mysql> CREATE TABLE employees (
    ->     employee_id INT PRIMARY KEY AUTO_INCREMENT,
    ->     employee_name VARCHAR(100) NOT NULL,
    ->     department_id INT,
    ->     FOREIGN KEY (department_id) REFERENCES departments(department_id)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> INSERT INTO departments (department_name) VALUES
    -> ('HR'),
    -> ('IT'),
    -> ('Finance'),
    -> ('Marketing');
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> INSERT INTO employees (employee_name, department_id) VALUES
    -> ('John Doe', 1),
    -> ('Jane Smith', 2),
    -> ('Michael Brown', 3),
    -> ('Emily Davis', NULL),  -- Employee without department
    -> ('Robert Wilson', 2);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from departments;
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|             1 | HR              |
|             2 | IT              |
|             3 | Finance         |
|             4 | Marketing       |
+---------------+-----------------+
4 rows in set (0.00 sec)

mysql> select * from employees;
+-------------+---------------+---------------+
| employee_id | employee_name | department_id |
+-------------+---------------+---------------+
|           1 | John Doe      |             1 |
|           2 | Jane Smith    |             2 |
|           3 | Michael Brown |             3 |
|           4 | Emily Davis   |          NULL |
|           5 | Robert Wilson |             2 |
+-------------+---------------+---------------+
5 rows in set (0.00 sec)

mysql> SELECT employees.employee_name, departments.department_name
    -> FROM employees
    -> INNER JOIN departments ON employees.department_id = departments.department_id;
+---------------+-----------------+
| employee_name | department_name |
+---------------+-----------------+
| John Doe      | HR              |
| Jane Smith    | IT              |
| Robert Wilson | IT              |
| Michael Brown | Finance         |
+---------------+-----------------+
4 rows in set (0.00 sec)

mysql> SELECT employees.employee_name, COALESCE(departments.department_name, 'No Department') AS department_name
    -> FROM employees
    -> LEFT JOIN departments ON employees.department_id = departments.department_id;
+---------------+-----------------+
| employee_name | department_name |
+---------------+-----------------+
| John Doe      | HR              |
| Jane Smith    | IT              |
| Michael Brown | Finance         |
| Emily Davis   | No Department   |
| Robert Wilson | IT              |
+---------------+-----------------+
5 rows in set (0.00 sec)

