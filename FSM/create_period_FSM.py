from aiogram.fsm.state import State, StatesGroup

class PeriodFSM(StatesGroup):
    start_date = State()
    end_date = State()
    duration = State()