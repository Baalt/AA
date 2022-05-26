import csv

class StatisticPrinter:
    def __init__(self, estimated_winnings, real_winnings, win, draw, lose, balance):
        self.estimated_winnings = estimated_winnings
        self.real_winnings = real_winnings
        self.win, self.draw, self.lose = win, draw, lose
        self.balance = balance

    def print_report(self):
        print(f'''
        Количество матчей:____ {self.win + self.draw + self.lose}
        Выиграно:_____________ {self.win}
        Проиграно:____________ {self.lose}
        Ничьи:________________ {self.draw}
        Реально в кушках:_____ {self.real_winnings}
        Прогноз в кушах:______ {self.estimated_winnings}
        Баланс:_______________ {self.balance}
        ''')

class StatisticReport:
    def create_report(self, file):
        with open(file, 'r') as f:
            file = csv.reader(f)
            estimated_winnings, real_winnings, win, draw, lose, balance = 0, 0, 0, 0, 0, 0

            for row in file:
                if len(row) == 10 and row[0] != 'date':
                    print(' | '.join(row))
                    kush = float(row[8])
                    wdl = row[9]
                    estimated_winnings += kush

                    if wdl == 'w':
                        win += 1
                        coeff = float(row[7])
                        real_winnings += coeff - 1
                        bet_amount = float(row[1])
                        balance += (bet_amount * coeff) - bet_amount
                    elif wdl == 'l':
                        bet_amount = float(row[1])
                        lose += 1
                        real_winnings += - 1
                        balance += - bet_amount
                    elif wdl == 'd':
                        draw += 1

                else:
                    print('ERROR IN ROW: ', row)

            StatisticPrinter(estimated_winnings=estimated_winnings,
                             real_winnings=real_winnings,
                             win=win,
                             draw=draw,
                             lose=lose,
                             balance=balance).print_report()


if __name__ == '__main__':
    report = StatisticReport()
    report.create_report('real_may.csv')
