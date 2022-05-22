from main import bot, dp
from aiogram.types import Message
admin_id = 272543202
import openpyxl

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id,text=f"Привіт,я допоможу тобі дізнатись, чи тестується продукція обраного бренду на тваринках.Просто введи назву англійською)")
wb=openpyxl.reader.excel.load_workbook(filename='pets.xlsx',data_only=True)
wb.active=0
sheet=wb.active
print(sheet['A1'].value)
@dp.message_handler()
async def echo(message: Message):
    if f"{message.text}" != "/start":
         for i in range(1, 431):
            if sheet['A' + str(i)].value == f"{message.text}":
                await message.answer(text=sheet['C' + str(i)].value)
                break
    else:
        await bot.send_message(chat_id=message.chat.id,text=f"Привіт,я допоможу тобі дізнатись, чи тестується продукція обраного бренду на тваринках.Просто введи назву англійською)")