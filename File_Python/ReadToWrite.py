import pandas as pd
import multiprocessing as mp

def file(row, year_, path_open, path_save):
    const = row
    while True:
        try:
            file = pd.read_csv(path_open, skiprows=range(1, row), nrows=98125)
            if file.empty:
                print(mp.current_process(), 'я пустой')
                break
            file['Created Date'] = pd.to_datetime(file['Created Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
            file['Closed Date'] = pd.to_datetime(file['Closed Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
            file[file.set_index(file['Created Date']).index.year == year_].to_csv(path_save, header=None, mode='a')
            row += 98125
            print(mp.current_process(), row, '>=', const + 3925000)
            if row >= const + 3925000:
                break
        except BaseException as e:
            print(mp.current_process(), 'Ошибка:', e)
            break
    print(mp.current_process(), 'Процессор отработал')

if __name__ == '__main__':
    year_, row = 2020, 1
    path_open = '/home/exclusive/Рабочий стол/Файлы Ubuntu/311_Service_Requests_from_2010_to_Present.csv'
    path_save = f'/home/exclusive/Рабочий стол/Файлы Ubuntu/NYC_311_service_{year_}.csv'
    pd.read_csv(path_open, nrows=0).to_csv(path_save)
    p = {'process':{}}
    for i in range(8):
        p[i] = mp.Process(target=file, args=(row, year_, path_open, path_save))
        p[i].start()
        row += 3925000
    for i in range(8):
        p[i].join()
    print('Я закончил обрабатывать данные')