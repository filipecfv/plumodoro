import os
import pandas as pd

from datetime import date, datetime
from time import sleep

path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'statistics'
            )
        )

history_file = '/plumodoro_history_{}.csv'.format(datetime.now().year)


def history(time_work):
    today = str(date.today())
    history = pd.read_csv(path + history_file)
    history.loc[len(history)] = [today,
                                 1,
                                 float('{0:.2f}'.format(time_work/60))]
    history = history.groupby('Date').sum()
    history.to_csv(path + history_file, index=True)


def check_for_history_file():
    try:
        pd.read_csv(path + history_file)
    except FileNotFoundError:
        print("creating a history file...")
        create_history_file()


def create_history_file():
    sleep(2)
    current_year = datetime.now().year
    dates = pd.date_range(
            start=f'{current_year}-01-01',
            end=f'{current_year}-12-31').strftime('%Y-%m-%d').tolist()
    file = pd.DataFrame(columns=['Date', 'Pomodoros', 'Work Hours'])
    file['Date'] = dates
    file.to_csv(path + history_file, index=False)
