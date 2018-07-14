瀑布流demo
===

建立mysql数据库

```
create database waterfall default charset=utf8;

use waterfall;

create table goods (
    id int unsigned not null auto_increment primary key,
    title varchar(32) not null,
    pic varchar(64),
    price double not null
) engine=innodb default charset=utf8;
```