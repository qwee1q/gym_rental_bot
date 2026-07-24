from aiogram.fsm.state import State, StatesGroup

class PollFSM(StatesGroup):
    start_date = State()
    end_date = State()
    type = State()
