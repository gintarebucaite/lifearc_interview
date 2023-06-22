CREATE DATABASE LIFEARC;

CREATE TABLE public.antibodies
(
    unique_id character varying(30) NOT NULL,
    id character varying(20) NOT NULL,
    seq text NOT NULL,
    origin text,
    date_created date NOT NULL,
    date_modified date NOT NULL,
    sequence_type character varying(10) NOT NULL,
    protein_id integer,
    last_updater character varying(30),
    format character varying(30) NOT NULL,
    isotype character varying(30) NOT NULL,
  project character varying(30) NOT NULL,
    PRIMARY KEY (unique_id)
);

ALTER TABLE IF EXISTS public.antibodies
    OWNER to postgres;




SELECT *
FROM antibodies
WHERE date_created > '2020-01-01' 
ORDER BY LOWER(project) ASC;
