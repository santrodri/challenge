# Documentação do desafio técnico V3  
### Autor: Paulo Rodrigo dos Santos Braga

Essa documentação seguirá o mesmo fluxo apresentado no corpo do desafio no nível 6, serão esses

* Diagramas da arquitetura  
* Documentação técnica detalhada  
* Guia de operação e manutenção  
* Procedimentos de backup e recuperação  
* Guia de troubleshooting  
* Documentação de APIs usando OpenAPI/Swagger  
* Guia de segurança e boas práticas  
* Procedimentos de escalabilidade e resiliência  
* Documentação de configuração e variáveis de ambiente  
* Guia de contribuição e desenvolvimento
___
### Diagramas da arquitetura  
Essa API segue o padrão rest conforme descrito no primeiro item do desafio  
contento as rotas rotas descritas no nível 1 do desafio e gerando o fluxo abaixo!
![imagem](.github/Classe%20UML.png)
___
### Documentação técnica detalhada  
Essa aplicação tem o objetivo de ser um MPV(Minimum Viable Product) com   
o foco em velocidade de entrega seguindo o projeto disponível no [repositorio](https://github.com/v3-tecnologia/challenge/blob/main/CLOUD.md), tento emisso em vista, as tecnologias utilizadas foram as mais simples e rapidas para desenvolver:

    * Django-rest-framework: backend  
    * Sqlite: Banco: banco de dados   
    * Git: Versionamento  
    * AWS: Hospedagem e processamento  
    * JWT: Para autenticação  
Esse projeto foi desenvolvido em dois dias (incluindo sua documentação).  
Seus detalhes técnicos para construir a aplicação e subir o servidor podem ser encontrados no seu arquivo readme, isso inclui execução de testes, migração do banco de dados e instruções de uso para o DjangoServer(motor da API).


### Guia de operação e manutenção  
Os processos de operação constam no próprio código do sistema.

### Procedimentos de backup e recuperação  
Após os processos de migração forem concluídos um arquivo .db será criado   
e ele deve ser copiado para que uma nova versão do banco seja criada, para que o sistema a reconheça como a base em uso o arquivo gerado deve substituir o arquivo .db em uso.

### Guia de troubleshooting  
O servidor expõe em seu console as rotas consumidas, isso vai ajudar a corrigir os erros. Partes mais críticas como o sistema de processamento de imagem é gerenciado com mais cuidado e apresenta mais logs, problemas que podem ocorrer com certa frequência: 
    * Erros nas bibliotecas do EC2  
    * Errors envolvendo o Rekognition  
    Reinicie os serviços usados, reinstale as dependências via pip, e veja as permissões nos consoles.


### Documentação de APIs usando OpenAPI/Swagger  
Disponível na rota `/swagger`.

### Procedimentos de escalabilidade e resiliência  
A escalabilidade deve ser vertical adicionando poder de processamento a instância do EC2, e uso de um servidor para balanceamento de carga, esses  
processos não foram implementados pela falta de tempo, caso a API tenha um grande crescimento o recomendado é migrar a database para um banco de dados mais robusto, recomenda-se o PostgreSql pelo alto nível de integração com rest framework.

### Documentação de configuração e variáveis de ambiente  
A configuração das variáveis de ambiente são feitas de forma automática pelo github actions, mas caso seja necessário defina as variaveis SECRET\_KEY e FERNET\_KEY, tome muito cuidado com as chaves de criptografia, em especial com a FERNET\_KEY, pois caso ela seja perdida os dados criptografados serão perdidos.

### Guia de contribuição e desenvolvimento  
Crie um fork do repositório no github e submeta um pull request, ele será analisado e poderá ser integrado ao código.