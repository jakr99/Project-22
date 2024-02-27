from automata.fa.nfa import NFA

prob_1_8c = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q3', '1': 'q1'},
        'q3': {'0': 'q4', '1': 'q1'},
        'q4': {'0': 'q4', '1': 'q5'},
        'q5': {'0': 'q4', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q4'}
)

