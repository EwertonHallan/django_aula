BEGIN;
--
-- Alter field descricao on documento
--
ALTER TABLE "pessoa_documento" RENAME TO "pessoa_documento__old";
CREATE TABLE "pessoa_documento" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "descricao" varchar(255) NULL, "file" varchar(100) NOT NULL, "upload_data" datetime NOT NULL);
INSERT INTO "pessoa_documento" ("file", "id", "descricao", "upload_data") SELECT "file", "id", "descricao", "upload_data" FROM "pessoa_documento__old";
DROP TABLE "pessoa_documento__old";
--
-- Alter field file on documento
--
ALTER TABLE "pessoa_documento" RENAME TO "pessoa_documento__old";
CREATE TABLE "pessoa_documento" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "descricao" varchar(255) NULL, "upload_data" datetime NOT NULL, "file" varchar(100) NULL);
INSERT INTO "pessoa_documento" ("file", "id", "descricao", "upload_data") SELECT "file", "id", "descricao", "upload_data" FROM "pessoa_documento__old";
DROP TABLE "pessoa_documento__old";
COMMIT;
