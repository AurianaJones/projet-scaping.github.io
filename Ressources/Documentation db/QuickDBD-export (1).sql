-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "games" (
    "id"  SERIAL  NOT NULL,
    "titre" varchar,   NOT NULL,
    "release_date" date,   NOT NULL,
    "lang" varchar,   NOT NULL,
    "nb_player" int,   NOT NULL,
    "types" varchar,   NOT NULL,
    CONSTRAINT "pk_games" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "release_details" (
    "id"  SERIAL  NOT NULL,
    "game_id" int,   NOT NULL,
    "platform" varchar,   NOT NULL,
    "price" int,   NOT NULL,
    CONSTRAINT "pk_release_details" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "games_details" (
    "id"  SERIAL  NOT NULL,
    "game_id" int,   NOT NULL,
    "developer" varchar,   NOT NULL,
    "publisher" varchar,   NOT NULL,
    "description" text,   NOT NULL,
    CONSTRAINT "pk_games_details" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "release_details" ADD CONSTRAINT "fk_release_details_game_id" FOREIGN KEY("game_id")
REFERENCES "games" ("id");

ALTER TABLE "games_details" ADD CONSTRAINT "fk_games_details_game_id" FOREIGN KEY("game_id")
REFERENCES "games" ("id");

