#!/usr/bin/env python3

# Python sample with greek variable names
# C-x 8 RET greek small letter lambda RET
# After an example by Thorsten Altenkirch

class DFA:                      # Deterministic Finite Automaton

    def __init__(self, Q, Σ, δ, q0, F):
        self.Q = Q              # Set of states
        self.Σ = Σ              # Alphabet = set of symbols
        self.δ = δ              # Transition fcn (State,Symbol) -> State
        self.q0 = q0            # Initial state
        self.F = F              # Final states

    def __repr__(self):
        return f"DFA({self.Q}, {self.Σ}, {self.δ}, {self.q0}, {self.F})"

    def run(self, w):
        q = self.q0
        while w != "":
            q = self.δ[(q, w[0])]
            w = w[1:]
        return q in self.F

D0 = DFA({0, 1, 2}, { "a", "b" },
         {(0, "a"): 0, (0, "b"): 1,
          (1, "a"): 2, (1, "b"): 1,
          (2, "a"): 2, (2, "b"): 2},
         0, {0, 1})

print(D0.run("aa"))
print(D0.run("aabbb"))
print(D0.run("ba"))
print(D0.run("aba"))
print(D0.run(""))
