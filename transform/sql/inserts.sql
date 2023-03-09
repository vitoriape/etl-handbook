INSERT INTO nome_tabela('FULANO', 'M', 'EMAIL@EMAIL.COM', '000.000.000-00', 'RUA X');--Insert com exclusão de colunas

INSERT INTO nome_tabela('NOME', 'SEXO', 'E-MAIL', 'CPF', 'ENDERECO') VALUES ('FULANO', 'M', 'EMAIL@EMAIL.COM', '000.000.000-00', 'RUA X');--Insert destacando as colunas

INSERT INTO nome_tabela VALUES
    ('FULANO', 'M', 'EMAIL@EMAIL.COM', '000.000.000-00', 'RUA X'),
    ('FULANA', 'F', 'EMAIL@OUTROMAIL.COM', '000.000.000-01', 'RUA W')--Insert compacto (funciona somente no MYSQL)