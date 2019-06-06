-- Laboratorio 12 - ESTEBAN CABRERA

-- A --
CREATE USER operador PASSWORD '111111';
GRANT CONNECT ON DATABASE laboratorio12 TO operador;

-- B -- 
CREATE USER gerente PASSWORD '222222';
GRANT CONNECT ON DATABASE laboratorio12 TO gerente;

-- C --
CREATE USER administrador PASSWORD '333333';
GRANT CONNECT ON DATABASE laboratorio12 TO administrador;

-- D --
GRANT ALL PRIVILEGES ON DATABASE laboratorio12 TO administrador WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administrador WITH GRANT OPTION; 

-- E --
GRANT SELECT ON ALL TABLES IN SCHEMA public TO operador;

-- F --
GRANT SELECT,INSERT ON ALL TABLES IN SCHEMA public TO gerente;

-- G --
GRANT CREATE ON DATABASE laboratorio12 TO gerente;

-- H --
REVOKE REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public FROM operador;