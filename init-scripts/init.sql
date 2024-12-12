
GRANT ALL PRIVILEGES ON DATABASE library_db TO postgres;
CREATE TABLE author(
  id serial primary key,
  name varchar(255) not null
);
CREATE TABLE category(
  id serial primary key,
  name varchar(255) not null
);
CREATE TABLE client(
  id serial primary key,
  first_name varchar(255) not null,
  last_name varchar(255) not null
);
CREATE TABLE book(
  id serial primary key,
  ISBN varchar(13) not null,
  name varchar(255) not null,
  description text not null,
  is_loaned BOOLEAN not null default false,
  author_id int not null,
  category_id int not null,
  foreign key(author_id) references author(id),
  foreign key(category_id) references category(id)
);
CREATE TABLE book_category(
  book_id int not null,
  category_id int not null,
  primary key(book_id, category_id),
  foreign key(book_id) references book(id),
  foreign key(category_id) references category(id)
);
CREATE TABLE client_book(
  client_id int not null,
  book_id int not null,
  loan_date date not null,
  return_date date,
  primary key(client_id, book_id),
  foreign key(client_id) references client(id),
  foreign key(book_id) references book(id)
)