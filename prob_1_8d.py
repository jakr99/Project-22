from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
def dfa_to_nfa(dfa):
    nfa_transitions = {}
    for state, transitions in dfa.transitions.items():
        nfa_transitions[state] = {symbol: {target_state} for symbol, target_state in transitions.items()}
    
    nfa = NFA(
        states=dfa.states,
        input_symbols=dfa.input_symbols,
        transitions=nfa_transitions,
        initial_state=dfa.initial_state,
        final_states=dfa.final_states
    )
    return nfa

prob_1_6f = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q2'},
        'q3': {'0': 'q3', '1': 'q3'},
    },
    initial_state='q0',
    final_states={'q0', 'q1', 'q2'}
)

prob_1_6h = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q4', '1': 'q1'},
        'q1': {'0': 'q4', '1': 'q2'},
        'q2': {'0': 'q4', '1': 'q3'},
        'q3': {'0': 'q4', '1': 'q4'},
        'q4': {'0': 'q4', '1': 'q4'},
    },
    initial_state='q0',
    final_states={'q0', 'q1', 'q4'}
)

nfa_prob_1_6f = dfa_to_nfa(prob_1_6f)
nfa_prob_1_6h = dfa_to_nfa(prob_1_6h)



prob_1_8d = nfa_prob_1_6f.union(nfa_prob_1_6h)  

