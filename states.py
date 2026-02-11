from aiogram.fsm.state import State, StatesGroup


class AnketaState(StatesGroup):
    fio = State()
    phone = State()
    tajriba = State()
    old_ish = State()
    oylik = State()
    cv = State()
    tasdiq = State()
