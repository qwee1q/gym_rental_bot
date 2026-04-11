from aiogram.fsm.state import State, StatesGroup

class PollFSM(StatesGroup):
    date = State()
    day = State()
    type = State()
