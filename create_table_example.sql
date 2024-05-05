CREATE TABLE IF NOT EXISTS products (
	product_id serial primary key not null,
	product_name varchar(255) default null,
	category varchar(255) default null,
	sub_category varchar(255) default null
);

CREATE TABLE IF NOT EXISTS users (
	customer_id serial primary key not null,
	name varchar(255) default null,
	city varchar(255) default null,
	state varchar(255) default null,
	postal varchar(255) default null,
	password varchar(255) default null
);

CREATE TABLE IF NOT EXISTS contacts (
	contact_id INT GENERATED ALWAYS AS identity not null,
   	customer_id INT UNIQUE,
   	contact_name VARCHAR(255) NOT NULL,
   	phone VARCHAR(15),
   	email VARCHAR(100) UNIQUE,
	PRIMARY KEY(contact_id),
   	CONSTRAINT fk_customer
      FOREIGN KEY(customer_id) 
	  REFERENCES users(customer_id)
);


CREATE TABLE IF NOT EXISTS profiles (
	profile_id serial primary key not null,
	image TEXT,
	username VARCHAR(100),
	customer_id INT UNIQUE,
	CONSTRAINT fk_customer
		FOREIGN KEY (customer_id)
		REFERENCES users(customer_id)
);