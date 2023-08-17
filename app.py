from state_manager import App, State, Transition
from functions import *
from getkey import keys

app = App()

start_state = app.add_state(State(start))
options_state = app.add_state(State(options))
results_state = app.add_state(State(results))
end_state = app.add_state(State(end))

app.add_transition(start_state, Transition(keys.ENTER, options_state, setup))
app.add_transition(options_state, Transition("1", results_state, options_action))
app.add_transition(options_state, Transition("2", results_state, options_action))
app.add_transition(options_state, Transition("3", results_state, options_action))
app.add_transition(results_state, Transition(keys.ENTER, options_state))
app.add_transition(options_state, Transition(keys.ESCAPE, end_state))
app.add_transition(results_state, Transition(keys.ESCAPE, end_state))
app.add_transition(end_state, Transition(keys.ESCAPE, start_state))
