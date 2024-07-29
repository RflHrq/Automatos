# Automatos
Descrição
Este projeto implementa a criação e manipulação de Autômatos Finitos Não Determinísticos (AFN) e Autômatos Finitos Determinísticos (AFD), incluindo a conversão de um AFN para um AFD e a minimização do AFD. O código permite a definição interativa de um AFN, a conversão automática para AFD e a minimização do AFD. Também é possível testar se uma palavra é aceita pelo AFN, AFD e AFD minimizado.

Estrutura do Projeto
Classes
AFN (Autômato Finito Não Determinístico)
__init__: Inicializa um AFN vazio com estados, alfabeto, estado inicial, estados finais e transições.
add_state: Adiciona um estado ao AFN.
add_alphabet_symbol: Adiciona um símbolo ao alfabeto do AFN.
set_initial_state: Define o estado inicial do AFN.
add_final_state: Adiciona um estado final ao AFN.
add_transition: Adiciona uma transição ao AFN.
_dfs: Realiza uma busca em profundidade para verificar a aceitação de uma palavra.
accepts: Verifica se uma palavra é aceita pelo AFN.
AFD (Autômato Finito Determinístico)
__init__: Inicializa um AFD vazio com estados, alfabeto, estado inicial, estados finais e transições.
add_state: Adiciona um estado ao AFD.
add_alphabet_symbol: Adiciona um símbolo ao alfabeto do AFD.
set_initial_state: Define o estado inicial do AFD.
add_final_state: Adiciona um estado final ao AFD.
add_transition: Adiciona uma transição ao AFD.
set_dead_state: Define e adiciona o estado buraco ao AFD.
minimize: Minimiza o AFD.
split_block: Divide um bloco de estados para a minimização.
find_block: Encontra o bloco de um estado para a minimização.
accepts: Verifica se uma palavra é aceita pelo AFD.
Funções
afn_para_afd: Converte um AFN em um AFD.
print_afn: Imprime o AFN.
print_afd: Imprime o AFD.
Interação do Usuário
1. Inserir um AFN
O usuário é solicitado a inserir estados, símbolos do alfabeto, estado inicial, estados finais e transições do AFN.

Inserir Estados: O usuário insere os estados um por um.
Inserir Alfabeto: O usuário insere os símbolos do alfabeto um por um.
Definir Estado Inicial: O usuário define o estado inicial.
Definir Estados Finais: O usuário define os estados finais um por um.
Inserir Transições: O usuário insere as transições no formato estado,símbolo,estados_destino.
2. Converter AFN para AFD
A função afn_para_afd é usada para converter o AFN definido pelo usuário em um AFD equivalente.

3. Minimizar o AFD
A função minimize é usada para minimizar o AFD resultante da conversão.

4. Testar Aceitação de Palavra
O usuário pode inserir uma palavra para verificar se ela é aceita pelo AFN, AFD e AFD minimizado.

Exemplos de Uso
Exemplo de Entrada de AFN
plaintext
Copiar código
Insira um estado (ou deixe vazio para terminar): q0
Insira um estado (ou deixe vazio para terminar): q1
Insira um estado (ou deixe vazio para terminar): q2
Insira um estado (ou deixe vazio para terminar): 

Insira um símbolo do alfabeto (ou deixe vazio para terminar): a
Insira um símbolo do alfabeto (ou deixe vazio para terminar): b
Insira um símbolo do alfabeto (ou deixe vazio para terminar): 

Insira o estado inicial: q0

Insira um estado final (ou deixe vazio para terminar): q2
Insira um estado final (ou deixe vazio para terminar): 

Insira uma transição no formato 'estado,símbolo,estados_destino' (ou deixe vazio para terminar): q0,a,q1
Insira uma transição no formato 'estado,símbolo,estados_destino' (ou deixe vazio para terminar): q1,b,q2
Insira uma transição no formato 'estado,símbolo,estados_destino' (ou deixe vazio para terminar): 
Exemplo de Conversão para AFD
plaintext
Copiar código
AFN:
Estados: {'q0', 'q1', 'q2'}
Alfabeto: {'a', 'b'}
Estado inicial: q0
Estados finais: {'q2'}
Transições:
  q0 --a--> {'q1'}
  q1 --b--> {'q2'}

AFD:
Estados: [{'q0'}, {'q1'}, {'q2'}]
Alfabeto: {'a', 'b'}
Estado inicial: ['q0']
Estados finais: ['q2']
Transições:
  ['q0'] --a--> ['q1']
  ['q1'] --b--> ['q2']
Exemplo de Minimização de AFD
plaintext
Copiar código
AFD Minimizado:
Estados: [{'q0'}, {'q1'}, {'q2'}]
Alfabeto: {'a', 'b'}
Estado inicial: ['q0']
Estados finais: ['q2']
Transições:
  ['q0'] --a--> ['q1']
  ['q1'] --b--> ['q2']
Exemplo de Teste de Aceitação de Palavra
plaintext
Copiar código
Insira uma palavra para testar: ab

A palavra 'ab' é aceita pelo AFN
A palavra 'ab' é aceita pelo AFD
A palavra 'ab' é aceita pelo AFD minimizado
Execução do Projeto
Execute o script.
Siga as instruções para inserir estados, símbolos do alfabeto, estado inicial, estados finais e transições do AFN.
Veja a conversão do AFN para AFD e a minimização do AFD.
Teste se palavras são aceitas pelo AFN, AFD e AFD minimizado.
Requisitos
Python 3.x
Contribuição
Sinta-se à vontade para contribuir para o projeto abrindo issues e pull requests no GitHub.
