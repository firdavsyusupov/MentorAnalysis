from  aiogram.dispatcher import  FSMContext
from  aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram import types, Dispatcher
from  create_bot import dp

class FSMAdmin(StatesGroup):
    mentor_ismi = State()




# @db.message_handler(commands="Mentor qo'shish", state=None)
async def cm_start(message : types.Message):
    await  FSMAdmin.mentor_ismi.set()
    await  message.reply("Mentor ismini kiriting !")

# @db.message_handler(state=FSMAdmin.mentor_ismi)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

def register_handler_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=["Mentor qo'shish"], state=None)
    dp.register_message_handler(load_name, state=FSMAdmin.mentor_ismi)