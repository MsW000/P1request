import requests


class ParsingCourses:
    def __init__(self):
        self.r = requests.get(
            "https://rate-api.com/api/v1/YOUR_API_KEY/latest"
        )

        if self.r.status_code == 200:
            self.data = self.r.json()
        else:
            print("Ошибка", self.r.status_code)
            self.data = None
        
        if self.data is None:
            print("Не удалось получить курсы валют")
            return


class MenuCLI(ParsingCourses):

    def menu(self):

        print("Добро пожаловать в первую версию конвертера валют.\nПока он работает только с BYN")
        print("1. Доллар")
        print("2. Евро")
        print("3. Российский рубль")
        print("4. Выйти")
        print("5.Конвертировать USD \u2192 BYN")
        print("6.Конвертировать EUR \u2192 BYN")
        print("7.Конвертировать RUB \u2192 BYN  ")
        

        while True:

            try:
                number = int(input("Выберите номер пункта меню: "))
            except ValueError:
                print("Нужно ввести число")
                continue

            if number == 1:
                print("1 USD =", self.data["rates"]["BYN"], "BYN")

            elif number == 2:
                print("EUR:", self.data["rates"]["EUR"])

            elif number == 3:
                print("RUB:", self.data["rates"]["RUB"])

            elif number == 4:
                return
            
            elif number == 5:
                usercount = float(input("Введите какую суммму вы хотите конвертировать: "))
                print("In USD =", usercount * self.data["rates"]["BYN"], "BYN")

            elif number == 6:
                usercount = float(input("Введите какую суммму вы хотите конвертировать: "))
                print("EUR:", usercount * self.data["rates"]["BYN"])

            elif number == 7:
                usercount = float(input("Введите какую суммму вы хотите конвертировать: "))
                rub_to_byn = self.data["rates"]["BYN"] / self.data["rates"]["RUB"]
                print(usercount * rub_to_byn)

            else:
                print("Введите от 1, до 7")

if __name__ == "__main__":
    app = MenuCLI()
    app.menu()