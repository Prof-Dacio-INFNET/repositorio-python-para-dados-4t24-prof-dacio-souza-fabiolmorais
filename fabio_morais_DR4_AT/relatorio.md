# Relatório Final AT Python para Dados

**Data:** 14/12/2024<br/>
**Responsável:** Fábio Leite Morais

## Introdução
Relatório criado com intuito de documentar as etapas realizadas e comentar sobre as dificuldades encontradas. Como teve algumas questões simples que não tive dificuldade, não irei abordar, mas toda questão que tive dificuldade irei explicar.

## Processos Realizados
### 1. Preparação dos Dados
Foi solicitado para criar uma função que retornasse um DF com os dados do arquivo especifaco no enunciado. Como todos os TP's o senhor inicia com questões simples e vai aumentando seu nível gradualmente.
Os dados dos usuários foram carregados e validado as colunas preenchendo campos faltantes com o valor "Não Informado".


### 2. Extração de Plataformas
Basicamente utiliza da função anterior para identificar quais os nomes únicos das plataformas que são mencionados pelos usuários e armazena num arquivo txt.

### 3. Tratamento de Exceções ao Carregar Plataformas
Criei um loop para carregar o arquivo txt e caso esteja errado o caminho, solicito ao usuario que passe o caminho correto ou digite 'sair' para encerrar o loop.

### 4. Download de Páginas da Wikipédia
A função faz o download das páginas da Wikipédia usando URLs formatadas. Ela salva cada página como um arquivo HTML e retorna uma lista com os caminhos desses arquivos. Caso ocorra algum erro durante o download ou salvamento, o erro é tratado e exibido no console utilizando o try except. Faço usi da biblioteca urllib para fazer o request da url formatada e depois salvo os arquivos. **IMPORTANTE!** Deixei a resolução dessa questão comentada por que a próxima questão é um complemento dessa, então reutilizei o código e deixei essa comentada.

### 5. Tratamento de Exceções no Download
A mesma coisa da questão acima, a diferença é que uso as exceções para escrever log de erros.

### 6. Parsing das Páginas HTML
Dessa questão em diante já começa a ficar muito dificil e trabalhaso resolver as questões. Adiantando um pouco do que vou falar na conclusão, mas gostei muito do classroom do github por que eu consigo re-ler os códigos que foram explicados nas aulas e isso me ajudou muito. Mas tive que buscar referências em blogs para me ajudar. Aproveito essa questão para deixar os links:
https://www.w3schools.com/python/ref_string_split.asp<br/>
https://www.digitalocean.com/<br/>
https://www.geeksforgeeks.org/<br/>
https://pt.stackoverflow.com/questions/257905/retornando-somente-o-maior-valor-de-uma-lista-python (o stackoverflow usei bastante para várias dúvidas)

### 7. Extração de Tabelas de Jogos
Extendo os comentários da questão 6 para essa.

### 8. Uso de Expressões Regulares
Nessa questão deixei o comentário no código e vou reescreve-lo aqui também, quando fiz a função com os regex passados no enunciado não achou nenhum, busquei por regex na internet e achei os 2 links acima, mesmo assim o regex do email não encontrou nada e o da url acho que está errado.

### 9. Exportação dos Dados
Se eu ficar calvo a culpa é dessa questão, juro! Passei muito tempo para conseguir resolve-la, estava com problema no formato do dados_jogos e quebrei muito a cabeça para deixar de acordo com o modelo pedido.

### 10. Associação de Jogos aos Usuários
Outra questão que tive muita dificuldade, penso que tenha sido por conta de algum erro nas funções anteriores. Devido o tempo curto para entrega (O tempo ao qual me refiro é o meu mesmo) deixei dessa forma para entregar o AT completo e em dia.

### 11. Atualização do Banco de Dados
Por causa de já está cansado mentalmente tive muita dificuldade com essa questão por que tive que serializar os dados com o json.dumps para poder inserir no banco de dados.

### 12. Consulta aos Dados
Essa questão achei mais tranquilo, em algum TP de projeto de bloco fizemos algo parecido e por isso decidi usar o sqlite3 ao invés do alchemy, foi por conforto mesmo.

### 13. Análise Estatística
Também achei uma questão fácil, provavelmente tem outras formas melhores de fazer essa questão, mas consegui entregar o que a questão pede então vai assim rsrs. Como na questão 2 a gente consegue saber as plataformas que os usuários utilizam, fiz apenas uma condição se o nome da plataforma está na string da lista e fui incrementado o contador da plataforma.

### 14. Guardando as Informações
Outra questão fácil devido a questão 11, é mais ou menos parecido e usei a mesma linha de raciocínio para resolver.

## Conclusão

Primeiramente gostaria de agradecer ao senhor pelas as aulas e os conhecimentos adquiridos nesse semestre. Pra mim foi um semestre muito difícil por causa do trabalho que me consumiu absurdamente, por isso mal pude assistir as aulas ao vivo, acho que nesse semestre se assisti mais de 3 aulas ao vivo foi muito, infelizmente. Mas assisti todas as aulas gravadas e consegui absorver o conteúdo bem, como disse anteriormente, o uso do git com o github classroom foi uma mão na roda, muito bom para revisar o código, fazer os testes da minha cabeça e como não precisava escrever os códigos, dava pra focar mais na aula. Uma pena não poder assistir as aulas ao vivo por que iria "sugar" muito do seu conhecimento que, na minha opinião, é muito vasto, para aprender mais ainda. Pelo o que vi e se não mudarem, o senhor será meu professor na máteria eletiva então terei mais uma chance kkk. Finalizo meu feedback agradecendo novamente pelas as aulas e os conhecimentos passados.
