from state_manager import *
from functions import *
from getkey import keys

app = App()

state_start = app.add_state(State(start))
state_pressed = app.add_state(State(pressed))

app.add_transition(state_start, Transition(keys.ENTER, state_pressed))
app.add_transition(state_pressed, Transition("alnum", state_pressed, pressed_key))
app.add_transition(state_pressed, Transition(keys.ESCAPE, state_start, restart))
