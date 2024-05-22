import logging

from datetime import datetime
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Year-%month-%day'
)
current_date = datetime.now().strftime('%Y-%m-%d')
logging.info(f'Поточна дата: {current_date}')
print(f"Повідомлення записане в лог файл з поточною датою: {current_date}")