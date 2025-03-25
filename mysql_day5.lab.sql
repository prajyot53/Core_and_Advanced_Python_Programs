create database rushi;
Query OK, 1 row affected (0.01 sec)

mysql> use rushi;
Database changed
mysql> create table student(id int primary key not null,firstname varchar(20) not null,lastname varchar(20) not null,gender varchar(20) not null,age int not null,address varchar(20) not null,phoneno int not null);
Query OK, 0 rows affected (0.05 sec)

mysql> desc student;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| id        | int         | NO   | PRI | NULL    |       |
| firstname | varchar(20) | NO   |     | NULL    |       |
| lastname  | varchar(20) | NO   |     | NULL    |       |
| gender    | varchar(20) | NO   |     | NULL    |       |
| age       | int         | NO   |     | NULL    |       |
| address   | varchar(20) | NO   |     | NULL    |       |
| phoneno   | int         | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> insert into student values(1,'Ajit','Swami','male',21,'Pune',123456);

 insert into student values(2,'Deepesh','sarsar','male',22,'mumbai',23456);
Query OK, 1 row affected (0.01 sec)

mysql> insert into student values(3,'Athrav','babar','male',23,'solapur',213456);
Query OK, 1 row affected (0.00 sec)

mysql> insert into student values(4,'Prajyot','Satpute','male',22,'sangamner',9029786);
Query OK, 1 row affected (0.00 sec)

mysql> insert into student values(5,'vipul','gomase','male',23,'amravati',789456123);
Query OK, 1 row affected (0.00 sec)

mysql> select * from student;
+----+-----------+----------+--------+-----+-----------+-----------+
| id | firstname | lastname | gender | age | address   | phoneno   |
+----+-----------+----------+--------+-----+-----------+-----------+
|  1 | Ajit      | Swami    | male   |  21 | Pune      |    123456 |
|  2 | Deepesh   | sarsar   | male   |  22 | mumbai    |     23456 |
|  3 | Athrav    | babar    | male   |  23 | solapur   |    213456 |
|  4 | Prajyot   | Satpute  | male   |  22 | sangamner |   9029786 |
|  5 | vipul     | gomase   | male   |  23 | amravati  | 789456123 |
+----+-----------+----------+--------+-----+-----------+-----------+

Lab 1: Retrieve students' information and sort by last name in ascending order

 select * from student order by lastname Asc;
+----+-----------+----------+--------+-----+-----------+-----------+
| id | firstname | lastname | gender | age | address   | phoneno   |
+----+-----------+----------+--------+-----+-----------+-----------+
|  3 | Athrav    | babar    | male   |  23 | solapur   |    213456 |
|  5 | vipul     | gomase   | male   |  23 | amravati  | 789456123 |
|  2 | Deepesh   | sarsar   | male   |  22 | mumbai    |     23456 |
|  4 | Prajyot   | Satpute  | male   |  22 | sangamner |   9029786 |
|  1 | Ajit      | Swami    | male   |  21 | Pune      |    123456 |
+----+-----------+----------+--------+-----+-----------+-----------+

Lab 2: Count the number of students based on their gender

select gender,count(*) as student_count from student group by gender;
+--------+---------------+
| gender | student_count |
+--------+---------------+
| male   |             5 |
+--------+---------------+