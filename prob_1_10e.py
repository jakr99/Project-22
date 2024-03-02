from automata.fa.nfa import NFA

prob_1_10e = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1', ''},
    transitions={
        'q0': {'0': {'q1'}, '': {'q1'}},
        'q1': {'0': {'q1'}, '1': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q1'}
)