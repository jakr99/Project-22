from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

prob_1_16a = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q2'}, 'b': {'q1'}},
        'q1': {'a': {'q3'}, 'b': {'q0'}},
        'q2': {'a': {'q2'}, 'b': {'q2'}}, 
        'q3': {} 
    },
    initial_state='q0',
    final_states={'q0', 'q2'}
)
