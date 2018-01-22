CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id UUID NOT NULL DEFAULT uuid_generate_v4(),
	login TEXT NOT NULL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL
);
CREATE UNIQUE INDEX pk_users ON users(id);
CREATE UNIQUE INDEX users_unique_login ON users(login);
