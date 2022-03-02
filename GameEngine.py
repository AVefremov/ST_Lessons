from random import randint


class BaseGame:
    def __init__(self):
        self.hidden_number = randint(1, 10)
        self.incorrect_lower_answer = 'Ответ, если число меньше'
        self.incorrect_higher_answer = 'Ответ, если число больше'
        self.start_game_message = 'Сообщение в начале игры'

    def get_answer(self):
        return 'Win'

    def start_game(self):
        print(self.start_game_message)
        while True:
            result = self.get_answer()
            match result:
                case 'Less':
                    print(self.incorrect_lower_answer)
                case 'More':
                    print(self.incorrect_higher_answer)
                case 'Win':
                    break
        print(f'Число угадано, ответ: {self.hidden_number}. Конец игры')


class PlayerVsGame(BaseGame):
    def __init__(self):
        super().__init__()
        self.incorrect_lower_answer = 'Введенное число меньше загаданного. попробуйте другой вариант.'
        self.incorrect_higher_answer = 'Введенное число больше загаданного. попробуйте другой вариант.'
        self.start_game_message = 'Я загадал целое число от 1 до 10. Попробуйте его угадать.'

    def get_answer(self):
        while True:
            answer = input(r"Введите целое число от 1 до 10: ")
            # if not answer.isnumeric():
            #     continue
            try:
                answer = int(answer)
            except TypeError:
                continue
            # if answer > 10 or answer < 1:
            #     continue
            try:
                assert answer <= 10
                assert answer >= 1
            except AssertionError:
                continue
            if answer < self.hidden_number:
                result = 'Less'
                break
            elif answer > self.hidden_number:
                result = 'More'
                break
            else:   # answer == self.hidden_number
                result = 'Win'
                break
        return result


class GameVsPlayer(BaseGame):
    def __init__(self):
        super().__init__()
        self.range_start = 1
        self.range_end = 10
        self.incorrect_lower_answer = 'Тогда я загадаю число побольше'
        self.incorrect_higher_answer = 'Тогда я загадаю число поменьше'
        self.start_game_message = 'Загадайте целое число от 1 до 10. Я попробую его угадать.'

    def get_answer(self):
        print(f"Я загадал число {self.hidden_number}. Это число больше, меньше или равно с загаданному Вами числу?")
        answer = input(r"Ответ должен быть одним из трех вариантов: <, > или =. Введите ответ:")
        match answer:
            case '<':
                result = 'Less'
                self.range_start = self.hidden_number + 1
            case '>':
                result = 'More'
                self.range_end = self.hidden_number - 1
            case '=':
                result = 'Win'
            case _:
                print(r"Ответ не является одним из трех допустимых вариантов: <, > или =.")
                result = self.get_answer()
        # if self.range_start > self.range_end:
        #     self.range_start = self.range_end
        #     result = 'Win'
        try:
            assert self.range_start <= self.range_end
        except AssertionError:
            self.range_start = self.range_end
            result = 'Win'
        self.hidden_number = randint(self.range_start, self.range_end)
        return result
