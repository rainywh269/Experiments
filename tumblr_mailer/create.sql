CREATE TABLE posts(
    id long,
    url text,
    text text,
    state int(5),
    type varchar(5),
    user_id int(3)
);

create table users(
    id long,
    name text,
    email text
);
