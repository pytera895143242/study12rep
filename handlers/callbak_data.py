import asyncio
import json
from aiogram import types
from misc import dp, bot
from .sqlit import change_status,cheak_black
import random


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001970154406

text_stop = """<b>Аяяй я смотрю, кто-то решил
пошалить 😏

Сначала посмотри видео, а потом нажимай🙏🙃</b>"""

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


@dp.callback_query_handler(text = 'reg_prokladka', state = "*")
async def reg_prokladka(call, state: FSMContext):
    if int(cheak_black(call.message.chat.id)) == 0:
        await reg_p.step2.set() #ОЖИДАЕМ НАЗВАНИЕ КАНАЛА ЧЕРЕЗ @
        await call.message.answer("""<b>Отправь ссылку на свой канал через @ (собачку), как показано на видео!</b>

Не знаешь как это сделать? Посмотри видео еще раз😉""")

        await bot.answer_callback_query(call.id)  # Отвечаем на callback


@dp.message_handler(state=reg_p.step2, content_types='text')
async def name_channel(message: types.Message, state: FSMContext):
    if int(cheak_black(message.chat.id)) == 0:
        if message.text[0] == '@':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Продолжить обучение ✅',callback_data='bat_video12')
            markup.add(bat_a)
            await message.answer(text=f"""<b>Твоя «индивидуальная ссылка»:</b>
https://t.me/MovTokBot?start={message.text[1:]}""", disable_web_page_preview=True, reply_markup=markup)


        else:
            await message.answer(text="""<b>Отправь ссылку на канал через @, как это показано на видео☝️☝️☝️</b>
Пример : @BearPublic""")




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    if int(cheak_black(call.message.chat.id)) == 0:
        if call.data == 'bat_video2': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='ДАЛЕЕ🚀', callback_data='bat_video3')
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=5)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=6)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=7)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=8,reply_markup=markup)


        if call.data == 'bat_video3': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='🏃START🏃‍♀️', callback_data='bat_video4')
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=10)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=11,reply_markup=markup)

        if call.data == 'bat_video4': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ', url='https://youtu.be/XgMndhtCOhw')
            bat_b = types.InlineKeyboardButton(text='Я ВСЁ ПОНЯЛ(А)✅', callback_data='bat_video5')
            markup.add(bat_a)
            markup.add(bat_b)

            await state.update_data(video1='stop')
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=13,reply_markup=markup)
            await asyncio.sleep(70)  # 70
            await state.update_data(video1='start')

        if call.data == 'bat_video5': #отправляем второе видео
            try:
                if ((await state.get_data())['video1']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/wTv4CapiySI')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video6')
                markup.add(bat_a)
                markup.add(bat_b)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=16,reply_markup=markup)
                await state.update_data(video2='stop')
                await asyncio.sleep(200) #200
                await state.update_data(video2='start')


        if call.data == 'bat_video6': #отправляем второе видео
            try:
                if ((await state.get_data())['video2']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:

                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/eEFGje9pi6s')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video7')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video3='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=24,reply_markup=markup)
                await asyncio.sleep(210) #xxx
                await state.update_data(video3='start')

        if call.data == 'bat_video7': #отправляем второе видео
            try:
                if ((await state.get_data())['video3']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/_BsIFZ3edmI')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video8')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video4='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=30,reply_markup=markup)
                await asyncio.sleep(270)  # xxx
                await state.update_data(video4='start')

        if call.data == 'bat_video8':  # отправляем второе видео
            try:
                if ((await state.get_data())['video4']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/Zk0MKzDLy5U')
                bat_b = types.InlineKeyboardButton(text='Я ВЫПОЛНИЛ(А)✅', callback_data='bat_video9')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video5='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=36,reply_markup=markup)
                await asyncio.sleep(270)  # xxx
                await state.update_data(video5='start')



        if call.data == 'bat_video9':  # отправляем второе видео
            try:
                if ((await state.get_data())['video5']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:

                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/jo8L0KIXPv8')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video10')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video6='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=39,reply_markup=markup)
                await asyncio.sleep(60)  # xxx
                await state.update_data(video6='start')


        if call.data == 'bat_video10':  # отправляем второе видео
            try:
                if ((await state.get_data())['video6']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/i8QjJpLJKbs')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video11')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video7='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=39,reply_markup=markup)
                await asyncio.sleep(40)  # xxx
                await state.update_data(video7='start')


        if call.data == 'bat_video11':  # отправляем второе видео
            try:
                if ((await state.get_data())['video7']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer("""<b>Стоп⛔️

Сначала посмотри видео, а потом начинай делать индивидуальную ссылку (ИС)🙏🙃</b>""")
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/EaorL-D6pfM')
                bat_b = types.InlineKeyboardButton(text='СОЗДАТЬ ИС⚡️', callback_data='reg_prokladka')
                bat_с = types.InlineKeyboardButton(text='У МЕНЯ ЕСТЬ ИС😎', callback_data='bat_video12')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video8='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=42,reply_markup=markup)
                await asyncio.sleep(40)  # xxx
                await state.update_data(video8='start')

        if call.data == 'bat_video12':  # отправляем второе видео
            try:
                if ((await state.get_data())['video8']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/p_XJQvgqfsk')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video13')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video9='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=46,reply_markup=markup)
                await asyncio.sleep(120)  # xxx
                await state.update_data(video9='start')

        if call.data == 'bat_video13':  # отправляем второе видео
            try:
                if ((await state.get_data())['video9']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/ojXtgtKB1nw')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video14')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video10='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=49,reply_markup=markup)
                await asyncio.sleep(210)  # xxx
                await state.update_data(video10='start')

        if call.data == 'bat_video14':  # отправляем второе видео
            try:
                if ((await state.get_data())['video10']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/KAJtF2GIU0A')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video15')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video11='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=52,reply_markup=markup)
                await asyncio.sleep(320)  # xxx
                await state.update_data(video11='start')


        if call.data == 'bat_video15':  # отправляем второе видео
            try:
                if ((await state.get_data())['video11']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/ZZD5sPGJc1k')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video16')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video12='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=55,reply_markup=markup)
                await asyncio.sleep(60)  # xxx
                await state.update_data(video12='start')

        if call.data == 'bat_video16':  # отправляем второе видео
            try:
                if ((await state.get_data())['video12']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/u2dK3ZQWOG0')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video17')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video13='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=58,reply_markup=markup)
                await asyncio.sleep(150)  # xxx
                await state.update_data(video13='start')

        if call.data == 'bat_video17':  # отправляем второе видео
            try:
                if ((await state.get_data())['video13']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/TzH6Fy6VE-A')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video18')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video14='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=61,reply_markup=markup)
                await asyncio.sleep(200)  # xxx
                await state.update_data(video14='start')


        if call.data == 'bat_video18':  # отправляем второе видео
            try:
                if ((await state.get_data())['video15']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК🤓', url='https://youtu.be/usXJlIq78sI')
                bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video19')
                markup.add(bat_a)
                markup.add(bat_b)
                await state.update_data(video15='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=64,reply_markup=markup)
                await asyncio.sleep(180)  # xxx
                await state.update_data(video15='start')


        if call.data == 'bat_video19':  # отправляем второе видео
            try:
                if ((await state.get_data())['video16']) == 'start':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await call.message.answer(text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='ГЛЯНЬ ВИДОС🤠', url='https://youtu.be/UdjZjJR_uwE')
                bat_a1 = types.InlineKeyboardButton(text='🏃‍♀️ХОЧУ В ЧАТ🏃', url='https://t.me/+JD4idG9JTdQyZmRi')
                bat_a2 = types.InlineKeyboardButton(text='ЗАКАЗАТЬ БОТА👨🏻‍💻', url='https://docs.google.com/forms/d/e/1FAIpQLSd0fqwv9D431_so3rIH3uTCvyNi-VJlGy_WrMJjPQu0gIc8pA/viewform?usp=sf_link')
                bat_a3 = types.InlineKeyboardButton(text='🚀 УЗНАТЬ О PREMIUM🚀', url='https://t.me/Pablito_Escobare')
                markup.add(bat_a)

                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=74,reply_markup=markup)
                change_status(call.message.chat.id)

    await bot.answer_callback_query(call.id)