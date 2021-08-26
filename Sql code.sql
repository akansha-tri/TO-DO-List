use project;
create table tasks(ids INT NOT NULL primary key, title varchar(30), descr varchar(30), hours varchar(30));
select*from tasks;
create table comptasks(ids INT NOT NULL primary key, title varchar(30), hours varchar(30));
select*from comptasks;
truncate table tasks;
truncate table comptasks;
create table login(user varchar(30), password varchar(30));
select*from login;
