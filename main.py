import random


class Game:
    def __init__(self):
        self.hidden_number: int = 0
        self.user_number: int = 0
        self.range_from: int = 1
        self.range_to: int = 10

    def set_range(self, first_number: int, last_number: int) -> 'Успешно ли обновили диапазон: bool':
        if isinstance(first_number, int):
            if isinstance(last_number, int):
                self.range_from = first_number
                self.range_to = last_number
                return True
        return False

    def __randomise_number(self):
        random.seed()
        self.hidden_number = random.randint(self.range_from, self.range_to)

    def __get_answer(self) -> int:
        try:
            user_answer = int(input(r"Введите число: "))
            if user_answer <= self.range_to:
                if user_answer >= self.range_from:
                    return user_answer
            print(f"Введенная строка не является целым числом от {self.range_from} до {self.range_to}. "
                  f"Попробуйте угадать снова.")
        except ValueError:
            print(f"Введенная строка не является целым числом от {self.range_from} до {self.range_to}. "
                  f"Попробуйте угадать снова.")
        return self.__get_answer()

    def start(self):
        self.__randomise_number()
        print(f"Загадано целое число от {self.range_from} до {self.range_to}, попробуйте угадать.")
        self.user_number = self.__get_answer()
        while self.user_number != self.hidden_number:
            if self.user_number < self.hidden_number:
                print(f"Введенное число {self.user_number} меньше загаданного числа "
                      f"от {self.range_from} до {self.range_to}, попробуйте угадать снова.")
            else:
                print(f"Введенное число {self.user_number} больше загаданного числа "
                      f"от {self.range_from} до {self.range_to}, попробуйте угадать снова.")
            self.user_number = self.__get_answer()
        print(f"Было загадано число {self.hidden_number}. Вы победили. Попробовать снова?")
        if input(r"Да/Нет: ") == 'Да':
            self.start()


game = Game()
if game.set_range(1, 15):
    game.start()

# Загадано целое число от 1 до 10, попробуйте угадать.
# Введите число: 4
# Введенное число 4 меньше загаданного числа от 1 до 10, попробуйте угадать снова.
# Введите число: 6
# Введенное число 6 больше загаданного числа от 1 до 10, попробуйте угадать снова.
# Введите число: АБВ
# Введенная строка не является целым числом от 1 до 10. Попробуйте угадать снова.
# Введите число: 5
# Было загадано число 5. Вы победили. Попробовать снова?
# Да/Нет: