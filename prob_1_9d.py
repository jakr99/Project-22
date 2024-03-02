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

prob_1_6k = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q2', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'},
    },
    initial_state='q0',
    final_states={'q0', 'q1'}
)

prob_1_6n = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1', ''},
    transitions={
        'q0': {'1': 'q1', '0': 'q1', '': 'q0'}, 
        'q1': {'0': 'q1', '1': 'q1', '': 'q0'},
        },
    initial_state='q0',
    final_states={'q1'}
)

nfa_prob_1_6k = dfa_to_nfa(prob_1_6k)
nfa_prob_1_6n = dfa_to_nfa(prob_1_6n)

prob_1_9d = nfa_prob_1_6k.concatenate(nfa_prob_1_6n)

