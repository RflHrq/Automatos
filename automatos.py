class AFN:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.initial_state = None
        self.final_states = set()
        self.transitions = {}

    def add_state(self, state):
        if state in self.states:
            raise ValueError("Estado já existente")
        self.states.add(state)

    def add_alphabet_symbol(self, symbol):
        if symbol in self.alphabet:
            raise ValueError("Símbolo já existente")
        self.alphabet.add(symbol)

    def set_initial_state(self, state):
        if state not in self.states:
            raise ValueError("Estado inicial deve estar nos estados inseridos")
        self.initial_state = state

    def add_final_state(self, state):
        if state not in self.states:
            raise ValueError("Estado final deve estar nos estados inseridos")
        self.final_states.add(state)

    def add_transition(self, from_state, symbol, to_states):
        if from_state not in self.states or any(to_state not in self.states for to_state in to_states):
            raise ValueError("Estados de transição devem estar nos estados inseridos")
        if symbol not in self.alphabet:
            raise ValueError("Símbolo de transição deve estar no alfabeto inserido")
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        if symbol not in self.transitions[from_state]:
            self.transitions[from_state][symbol] = set()
        self.transitions[from_state][symbol].update(to_states)

    def _dfs(self, current_state, word):
        if len(word) == 0:
            return current_state in self.final_states
        if current_state not in self.transitions or word[0] not in self.transitions[current_state]:
            return False
        next_states = self.transitions[current_state][word[0]]
        for state in next_states:
            if self._dfs(state, word[1:]):
                return True
        return False

    def accepts(self, word):
        return self._dfs(self.initial_state, word)


class AFD:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.initial_state = None
        self.final_states = set()
        self.transitions = {}

    def add_state(self, state):
        self.states.add(state)

    def add_alphabet_symbol(self, symbol):
        self.alphabet.add(symbol)

    def set_initial_state(self, state):
        self.initial_state = state

    def add_final_state(self, state):
        self.final_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][symbol] = to_state

    def set_dead_state(self):
        self.dead_state = 'dead'
        self.states.add(self.dead_state)
        for symbol in self.alphabet:
            self.transitions[self.dead_state] = {symbol: self.dead_state}

    def minimize(self):
        self.set_dead_state()  # Adiciona o estado buraco
        for state in self.states:
            if state not in self.transitions:
                self.transitions[state] = {symbol: self.dead_state for symbol in self.alphabet}
        
        P = [self.final_states, self.states - self.final_states]
        while True:
            new_P = []
            for block in P:
                sub_blocks = self.split_block(block, P)
                new_P.extend(sub_blocks)
            if new_P == P:
                break
            P = new_P
        
        minimized_afd = AFD()
        state_map = {frozenset(block): f'S{idx}' for idx, block in enumerate(P)}
        minimized_afd.initial_state = state_map[frozenset(next(block for block in P if self.initial_state in block))]
        for block in P:
            representative = state_map[frozenset(block)]
            if block & self.final_states:
                minimized_afd.add_final_state(representative)
            for symbol in self.alphabet:
                next_state = self.transitions[next(iter(block))].get(symbol, self.dead_state)
                minimized_afd.add_transition(representative, symbol, state_map[frozenset(self.find_block(next_state, P))])
        
        minimized_afd.states = set(state_map.values())
        minimized_afd.alphabet = self.alphabet
        minimized_afd.final_states = set(state_map[frozenset(block)] for block in P if block & self.final_states)
        minimized_afd.initial_state = state_map[frozenset(self.find_block(self.initial_state, P))]
        minimized_afd.transitions = {}
        for block in P:
            representative = state_map[frozenset(block)]
            minimized_afd.transitions[representative] = {}
            for symbol in self.alphabet:
                next_state = self.transitions[next(iter(block))].get(symbol, self.dead_state)
                minimized_afd.transitions[representative][symbol] = state_map[frozenset(self.find_block(next_state, P))]
        
        return minimized_afd

    def split_block(self, block, P):
        blocks = {}
        for state in block:
            signature = tuple(self.transitions[state].get(symbol, self.dead_state) for symbol in self.alphabet)
            if signature not in blocks:
                blocks[signature] = set()
            blocks[signature].add(state)
        return list(blocks.values())

    def find_block(self, state, P):
        for block in P:
            if state in block:
                return block
        return None

    def accepts(self, word):
        current_state = self.initial_state
        for symbol in word:
            if symbol not in self.transitions.get(current_state, {}):
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.final_states


def afn_para_afd(afn):
    afd = AFD()
    afd.alphabet = afn.alphabet  # Copia o alfabeto do AFN para o AFD
    initial_state = frozenset([afn.initial_state])
    afd.set_initial_state(initial_state)
    estados_afd = [initial_state]
    estados_marcados = {initial_state: False}
    
    while any(not marcados for marcados in estados_marcados.values()):
        for estado in estados_afd:
            if not estados_marcados[estado]:
                estados_marcados[estado] = True
                afd.add_state(estado)
                
                for simbolo in afn.alphabet:
                    novo_estado = set()
                    for subestado in estado:
                        if subestado in afn.transitions and simbolo in afn.transitions[subestado]:
                            novo_estado.update(afn.transitions[subestado][simbolo])
                    novo_estado = frozenset(novo_estado)
                    
                    if novo_estado:  # Apenas adiciona transições para estados não vazios
                        afd.add_transition(estado, simbolo, novo_estado)
                        if novo_estado not in estados_afd:
                            estados_afd.append(novo_estado)
                            estados_marcados[novo_estado] = False

    for estado in estados_afd:
        if any(subestado in afn.final_states for subestado in estado):
            afd.add_final_state(estado)

    return afd


def print_afn(afn):
    print("AFN:")
    print("Estados:", afn.states)
    print("Alfabeto:", afn.alphabet)
    print("Estado inicial:", afn.initial_state)
    print("Estados finais:", afn.final_states)
    print("Transições:")
    for from_state, transitions in afn.transitions.items():
        for symbol, to_states in transitions.items():
            print(f"  {from_state} --{symbol}--> {to_states}")


def print_afd(afd):
    print("\nAFD:")
    print("Estados:", [list(state) for state in afd.states])
    print("Alfabeto:", afd.alphabet)
    print("Estado inicial:", list(afd.initial_state))
    print("Estados finais:", [list(state) for state in afd.final_states])
    print("Transições:")
    for from_state, transitions in afd.transitions.items():
        for symbol, to_state in transitions.items():
            print(f"  {list(from_state)} --{symbol}--> {list(to_state)}")


# Interface para criar o AFN
afn = AFN()

# Inserção de estados
while True:
    state = input("Insira um estado (ou deixe vazio para terminar): ")
    if state == "":
        break
    try:
        afn.add_state(state)
    except ValueError as e:
        print(e)

# Inserção do alfabeto
while True:
    symbol = input("Insira um símbolo do alfabeto (ou deixe vazio para terminar): ")
    if symbol == "":
        break
    try:
        afn.add_alphabet_symbol(symbol)
    except ValueError as e:
        print(e)

# Definição do estado inicial
while True:
    initial_state = input("Insira o estado inicial: ")
    try:
        afn.set_initial_state(initial_state)
        break
    except ValueError as e:
        print(e)

# Definição dos estados finais
while True:
    final_state = input("Insira um estado final (ou deixe vazio para terminar): ")
    if final_state == "":
        break
    try:
        afn.add_final_state(final_state)
    except ValueError as e:
        print(e)

# Inserção de transições
while True:
    transition = input("Insira uma transição no formato 'estado,símbolo,estados_destino' (ou deixe vazio para terminar): ")
    if transition == "":
        break
    try:
        from_state, symbol, to_states_str = transition.split(',')
        to_states = set(to_states_str.split())
        afn.add_transition(from_state, symbol, to_states)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Formato inválido. Use 'estado,símbolo,estados_destino'")

print_afn(afn)

# Conversão do AFN para AFD
afd = afn_para_afd(afn)
print_afd(afd)

# Minimização do AFD
afd_minimizado = afd.minimize()
print("\nAFD Minimizado:")
print_afd(afd_minimizado)

# Teste de aceitação de palavra no AFN
word = input("Insira uma palavra para testar: ")

# Teste de aceitação de palavra no AFN
if afn.accepts(word):
    print(f"A palavra '{word}' é aceita pelo AFN")
else:
    print(f"A palavra '{word}' não é aceita pelo AFN")

# Teste de aceitação de palavra no AFD
if afd.accepts(word):
    print(f"A palavra '{word}' é aceita pelo AFD")
else:
    print(f"A palavra '{word}' não é aceita pelo AFD")

# Teste de aceitação de palavra no AFD minimizado
if afd_minimizado.accepts(word):
    print(f"A palavra '{word}' é aceita pelo AFD minimizado")
else:
    print(f"A palavra '{word}' não é aceita pelo AFD minimizado")
