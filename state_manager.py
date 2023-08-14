class Transition:
    def __init__(self, key: str, target_id: int, listener=None):
        self.key = key
        self.target_id = target_id
        self.listener = listener

class State:
    def __init__(self, function=None, transitions: list[Transition]=None):
        if transitions is None:
            transitions = []
        self.function = function
        self.transitions = transitions

    def add_transition(self, transition: Transition):
        self.transitions.append(transition)
        return True

    def remove_transition(self, transition: Transition):
        if transition not in self.transitions:
            return False
        self.transitions.remove(transition)
        return True

class App:
    def __init__(self, states: list[State]=None, current_state: int=0):
        if states is None:
            states = []
        self.states = states
        self.current_state = current_state

    def add_state(self, state: State):
        i = 0
        while i < len(self.states):
            if self.states[i] is None:
                self.states[i] = state
                return i
            i += 1
        self.states.append(state)
        return len(self.states) - 1

    def remove_state(self, state_id: int):
        if state_id < 0 or state_id >= len(self.states):
            return False
        self.states[state_id] = None
        return True
    
    def add_transition(self, state_id: int, transition: Transition):
        if state_id < 0 or state_id >= len(self.states):
            return False
        return self.states[state_id].add_transition(transition)

    def remove_transition(self, state_id: int, transition: Transition):
        if state_id < 0 or state_id >= len(self.states):
            return False
        state = self.states[state_id]
        return state.remove_transition(transition)
    
    def call(self, data: dict=None):
        if data is None:
            data = {}
        if self.current_state < 0 or self.current_state >= len(self.states):
            return False
        state = self.states[self.current_state]
        if state.function is None:
            return False
        state.function(data)
        return True

    def transition(self, key: str, data: dict=None):
        if data is None:
            data = {}
        if self.current_state < 0 or self.current_state >= len(self.states):
            return False
        state = self.states[self.current_state]
        for transition in state.transitions:
            if transition.key == key:
                self.current_state = transition.target_id
                if transition.listener is not None:
                    transition.listener(key, data)
                return True

    def get_current_state(self):
        if self.current_state < 0 or self.current_state >= len(self.states):
            return None
        return self.states[self.current_state]

    def get_state_id(self, state: State):
        for i, st in enumerate(self.states):
            if st == state:
                return i
