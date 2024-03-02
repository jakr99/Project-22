from automata.fa.nfa import NFA

prob_1_17a = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'0', '1', ''},
    transitions={
        'q0': {'0': {'q1'}},
        'q1': {'0': {'q2'}, '1': {'q3'}},
        'q2': {'1': {'q4'}},  
        'q3': {'0': {'q5'}, '': {'q0'}},
	'q4': {'': {'q0'}},
	'q5': {'': {'q0'}}  
    },
    initial_state='q0',
    final_states={'q0'}
)

