# Automatos

## Descrição
Este projeto implementa a criação e manipulação de Autômatos Finitos Não Determinísticos (AFN) e Autômatos Finitos Determinísticos (AFD). As funcionalidades incluem:

- Criação e definição interativa de um AFN.
- Conversão automática de um AFN para um AFD.
- Minimização do AFD.
- Teste de aceitação de palavras pelo AFN, AFD e AFD minimizado.

## Estrutura do Projeto

### Classes

**AFN (Autômato Finito Não Determinístico)**
- `__init__`: Inicializa um AFN vazio com estados, alfabeto, estado inicial, estados finais e transições.
- `add_state`: Adiciona um estado ao AFN.
- `add_alphabet_symbol`: Adiciona um símbolo ao alfabeto do AFN.
- `set_initial_state`: Define o estado inicial do AFN.
- `add_final_state`: Adiciona um estado final ao AFN.
- `add_transition`: Adiciona uma transição ao AFN.
- `_dfs`: Realiza uma busca em profundidade para verificar a aceitação de uma palavra.
- `accepts`: Verifica se uma palavra é aceita pelo AFN.

**AFD (Autômato Finito Determinístico)**
- `__init__`: Inicializa um AFD vazio com estados, alfabeto, estado inicial, estados finais e transições.
- `add_state`: Adiciona um estado ao AFD.
- `add_alphabet_symbol`: Adiciona um símbolo ao alfabeto do AFD.
- `set_initial_state`: Define o estado inicial do AFD.
- `add_final_state`: Adiciona um estado final ao AFD.
- `add_transition`: Adiciona uma transição ao AFD.
- `set_dead_state`: Define e adiciona o estado buraco ao AFD.
- `minimize`: Minimiza o AFD.
- `split_block`: Divide um bloco de estados para a minimização.
- `find_block`: Encontra o bloco de um estado para a minimização.
- `accepts`: Verifica se uma palavra é aceita pelo AFD.

### Funções
- `afn_para_afd`: Converte um AFN em um AFD.
- `print_afn`: Imprime o AFN.
- `print_afd`: Imprime o AFD.

## Interação do Usuário

### 1. Inserir um AFN
O usuário é solicitado a inserir:
- **Estados**: Inserir os estados um por um.
- **Símbolos do Alfabeto**: Inserir os símbolos do alfabeto um por um.
- **Estado Inicial**: Definir o estado inicial.
- **Estados Finais**: Definir os estados finais um por um.
- **Transições**: Inserir as transições no formato `estado,símbolo,estados_destino`.

### 2. Converter AFN para AFD
A função `afn_para_afd` é usada para converter o AFN definido pelo usuário em um AFD equivalente.

### 3. Minimizar o AFD
A função `minimize` é utilizada para minimizar o AFD resultante da conversão.

### 4. Testar Aceitação de Palavra
O usuário pode inserir uma palavra para verificar se ela é aceita pelo AFN, AFD e AFD minimizado.

## Exemplos de Uso

### Exemplo de Entrada de AFN
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

Insira uma palavra para testar: ab
A palavra `'ab'` é aceita pelo AFN, AFD e AFD minimizado.

## Execução do Projeto
1. Execute o script.
2. Siga as instruções para inserir estados, símbolos do alfabeto, estado inicial, estados finais e transições do AFN.
3. Observe a conversão do AFN para AFD e a minimização do AFD.
4. Teste se palavras são aceitas pelo AFN, AFD e AFD minimizado.

## Requisitos
- Python 3.x

## Contribuição
Sinta-se à vontade para contribuir para o projeto abrindo issues e pull requests no GitHub.
