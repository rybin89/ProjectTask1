from tkinter import *
from tkinter import ttk


class GameItemView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Инвентарь для игр")
        self.geometry("1280x800")
        # Фрейм Добавить предмет
        self.add_frame = ttk.Frame(self,
                                   borderwidth=1,  # ширина границы фрейма
                                   relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                   padding=[8, 10],  # внутренние отступы фрейма
                                   )
        self.add_frame.pack(
            anchor=CENTER,  # расположение по центру
            fill=X,  # заполнение
            padx=10,  # расположение по оси x от верней левой точки окна
            pady=10,  # расположение по оси y от верней левой точки окна

        )
        # Фрайм в которм расположен текст Добавить Предмет (находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER,  # расположение по центру
                          fill=X,  # заполнение
                          padx=10,  # расположение по оси x от верней левой точки окна
                          pady=10,  # расположение по оси y от верней левой точки окна
                          )
        self.add_title = ttk.Label(self.add_title_frame, text="Добавить Предмет")
        self.add_title.pack()
        # Фрайм в которм расположены окна ввода данных о Предмете (находится внутри фрейма add_frame)
        self.add_input_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10]
                                         )
        self.add_input_frame.pack(fill=X,  # заполнение
                              padx=10,  # расположение по оси x от верней левой точки окна
                              pady=10,  # расположение по оси y от верней левой точки окна
                              )
        # Окна ввода данных предмета для добавленпия в таблицу БД
        self.add_title_name = ttk.Label(self.add_input_frame, text="Название")
        self.add_title_name.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add_title_rarity = ttk.Label(self.add_input_frame, text="Уникальность")
        self.add_title_rarity.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.add_title_player = ttk.Label(self.add_input_frame, text="Игрок")
        self.add_title_player.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.add_title_quantity = ttk.Label(self.add_input_frame, text="Количество")
        self.add_title_quantity.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        self.add_title_stats = ttk.Label(self.add_input_frame, text="Характерстики")
        self.add_title_stats.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

        self.add_name = ttk.Entry(self.add_input_frame)
        self.add_name.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.add_rarity = ttk.Entry(self.add_input_frame)
        self.add_rarity.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.add_player = ttk.Entry(self.add_input_frame)
        self.add_player.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.add_quantity = ttk.Entry(self.add_input_frame)
        self.add_quantity.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

        self.add_stats = ttk.Entry(self.add_input_frame)
        self.add_stats.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)


        # Фрейм Вывод предметов

        # Фрейм Найти предмет


if __name__ == "__main__":
    window = GameItemView()
    window.mainloop()
