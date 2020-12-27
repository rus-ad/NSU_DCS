CREATE DATABASE songlist;
CREATE USER docker WITH PASSWORD 'docker';
GRANT ALL PRIVILEGES ON DATABASE songlist to docker;
\c songlist;
create table links (
	link_id SERIAL NOT NULL,
	link varchar(128)
);
INSERT INTO links (link_id, link) VALUES(0, 'EcDw3X4ImUU');
INSERT INTO links (link_id, link) VALUES(1, 'As03tlODkdw');
