create DATABASE pawan;
use pawan;
create table STUDENTS(S_name char(20),
S_class char(10),
S_rollno int,
Total_marks int );
insert into STUDENTS(S_name,S_class,S_rollno,Total_marks)
values('Pawan','BCA',2410997260,499),
('Parv','BCA',2410997257,499),
('Parshav','BCA',2410997255,499),
('Nischay','BCA',2410997244,499),
('Pingaksh','BCA',2410997261,499);
select * from STUDENTS;
