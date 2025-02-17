from automata.fa.nfa import NFA

prob_1_16b = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b', ''},
    transitions={
        'q0': {'a': {'q1'}, '': {'q3'}},
        'q1': {'a': {'q1'}, 'b': {'q2'}},
        'q2': {'a': {'q0'}, 'b': {'q2'}},  
        'q3': {'a': {'q3'}, 'b': {'q3'}}  
    },
    initial_state='q0',
    final_states={'q0','q1','q2'}
)
