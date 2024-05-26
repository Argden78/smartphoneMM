# Zadanie
# Smartfon może być włączony lub wyłączony oraz posiada określoną pamięć wewnętrzną
# Można na nim instalować aplikacje, które zużywają pamięć
# Napisz klasę, która obsłuży ten przypadek
# Stwórz jej instancję i sprawdź działanie

class Smartphone:
    def __init__(self, status, memory):
        # self.status = input("Podaj status telefonu: ON lub OFF: ")
        # self.memory = int(input("Podaj pamiec telefonu: "))
        self.status = status
        self.memory = memory
    def application(self, rozmiar_aplikacja):
        self.rozmiar_aplikacja = rozmiar_aplikacja
        wolna_pamiec = self.memory - self.rozmiar_aplikacja
        if wolna_pamiec < 0:
            print("Aplikacja jest za duza.")
        else:
            wolna_pamiec = self.memory - self.memory
            print("Aplikacja zainstalowana pomyślnie.")
        return wolna_pamiec

    def check_status(self,status):
        if status == "on":
            print("Smartphone jest wlaczony.")
        elif status == "off":
            print("Smartphone jest wylaczony.")
        else:
            print("ERROR")


telefon = Smartphone("ON", 500)

memory = int(input("Podaj pamiec telefonu: "))
status = input("Podaj status telefonu: ON lub OFF: ")

telefon.application(int(input("Podaj ile zajmuje aplikacja: ")))
telefon.check_status(status)


print("test")
