# Teste para desenvolvedores Python

Instruções do teste
------

Desenvolva uma API REST em linguagem Python que seja acessível localmente e verifique se um determinado número de CPF está em uma        *Blacklist*.

A aplicação deve:
 
1. Ser acessível como um serviço através de uma URL do tipo `http://IP:PORT/<cpf>`, por exemplo:
`http://127.0.0.1:5000/00000000000`


2. Retorne um JSON na consulta onde indique um retorno "FREE" caso o CPF não esteja na Blacklist, ou "BLOCK" caso o CPF pertença a Blacklist, por exemplo:
`{
"status": "FREE"
}
`
 

Para este teste você pode usar qualquer framework de sua escolha.

Os CPFs a serem testados estão no arquivo `blacklist.txt`.


Como entregar este teste
-----

Você deve forkar este projeto em sua própria conta do GitHub e fazer o commit em seu próprio repositório.


-----

## As Dependências para executar essa aplicação são:

1- flask
2- flask_restx