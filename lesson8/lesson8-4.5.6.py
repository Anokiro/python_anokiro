# Урок 8, задачи 4, 5, 6
# Организация склада (при помощи TKinter)

import ast
import os
from tkinter import *
from tkinter import messagebox


def warehouse():
    class OfficeTech:
        def __init__(self):
            # Конструктор для окна и заглавие
            self.window = Tk()
            self.window.geometry('600x400')
            # self.window['bg'] = 'orange'
            self.window.wm_attributes('-alpha', 0.95)
            self.window.title('Ardalion')
            self.top_frame = Frame(self.window)
            self.label = Label(self.top_frame, text="Склад компании 'Ардалион'", font='Arial 18', bg='orange',
                               fg='snow')
            self.label.pack()
            self.top_frame.pack()

            # Кнопка 'Добавить товар'
            self.button_frame = Frame(self.window)
            self.button_add = Button(self.button_frame, text=' Добавить товар ', font='Arial 14', bg='grey',
                                     relief='groove',
                                     command=self.add_product)
            self.button_add.pack(side='left', padx=10, pady=30)

            # Кнопка 'Удалить товар'
            self.button_del = Button(self.button_frame, text=' Удалить товар ', font='Arial 14', bg='grey',
                                     relief='groove',
                                     command=self.del_product)
            self.button_del.pack(side='left', padx=10, pady=30)
            self.button_frame.pack()

            # Кнопка 'Просмотреть статистику'
            self.button_frame2 = Frame(self.window)
            self.button_list = Button(self.button_frame2, text='Просмотреть товары в отделах.', font='Arial 14',
                                      relief='groove',
                                      bg='grey', command=self.window_show)
            self.button_list.pack(side='left', padx=10, pady=0)
            self.button_frame2.pack()
            mainloop()

        # ------------------------ Окно 1: Добавление товаров на склад (валидация введенных данных)-----------------------------
        def add_product(self):
            self.window.withdraw()
            self.window_add = Tk()
            self.window_add.geometry('600x400')
            self.window_add.title('Добавление товара на склад Ardalion')

            self.frame_add = Frame(self.window_add)
            self.frame_add2 = Frame(self.window_add)
            self.frame_add3 = Frame(self.window_add)

            # Фрейм 1
            self.label_add = Label(self.frame_add, text="Введите наименование техники (товара): ", font='Arial 13',
                                   bg='orange', fg='snow')
            self.label_add.pack(side='left')
            self.entry1 = Entry(self.frame_add, width=20, font='Arial 15')
            self.entry1.pack(side='left', padx=10)

            # Фрейм 2
            self.label_add2 = Label(self.frame_add2, text="Введите стоимость (за 1 единицу): ", font='Arial 13',
                                    bg='orange', fg='snow')
            self.label_add2.pack(side='left')
            self.entry2 = Entry(self.frame_add2, width=20, font='Arial 15')
            self.entry2.pack(side='left', padx=10)

            # Фрейм 3
            self.label_add3 = Label(self.frame_add3, text="Введите количество товара: ", font='Arial 13',
                                    bg='orange', fg='snow')
            self.label_add3.pack(side='left')
            self.entry3 = Entry(self.frame_add3, width=20, font='Arial 15')
            self.entry3.pack(side='left', padx=10)

            self.frame_add.pack(padx=10, pady=10, anchor=E)
            self.frame_add2.pack(padx=10, pady=10, anchor=E)
            self.frame_add3.pack(padx=10, pady=10, anchor=E)

            # Кнопка 'Добавить товар на склад'
            self.button_frame_list = Frame(self.window_add)
            self.button_add_list = Button(self.button_frame_list, text='Добавить товар на склад', font='Arial 13',
                                          bg='grey', width=24, command=self.add_product_on_warehouse)
            self.button_add_list.pack(padx=10, pady=10)
            self.button_frame_list.pack(padx=10, anchor=E)

            # Кнопка '<- Вернуться назад'
            self.button_frame_list_2 = Frame(self.window_add)
            self.button_add_list_2 = Button(self.button_frame_list_2, text='<- Вернуться назад', font='Arial 13',
                                            bg='grey', command=self.back_on_window)
            self.button_add_list_2.pack(padx=10, pady=10)
            self.button_frame_list_2.pack(side='right', padx=10, anchor=E)

        def add_product_on_warehouse(self):
            # Проверка заполнения формы (3-х строк)
            local_check_list1 = '0'
            if self.entry2.get():
                for i in self.entry2.get():
                    if i.isalpha():
                        local_check_list1 += str(i)
                        messagebox.showinfo("ОШИБКА!", f"В строке 'цена за ед.' введите целое число!")
            # ---------------------------
            local_check_list2 = '0'
            if self.entry3.get():
                for i in self.entry3.get():
                    if i.isalpha():
                        local_check_list2 += str(i)
                        messagebox.showinfo("ОШИБКА!", f"В строке 'количество товара' введите целое число!")
            if not self.entry1.get() or not self.entry2.get() or not self.entry3.get():
                messagebox.showinfo("ОШИБКА!", f"Не все строки заполнены!")
            # Если все выполнено успешно, то запишем данные в файл.
            if self.entry1.get() and local_check_list1 == '0' and local_check_list2 == '0' and self.entry2.get() \
                    and self.entry3.get():
                if len(self.entry2.get().split()) == 1 and len(self.entry3.get().split()) == 1:
                    messagebox.showinfo("Операция выполнена.", f'Товар: {self.entry1.get()}\n '
                                                               f'по цене за ед.: {self.entry2.get()}\n'
                                                               f' в количестве: {self.entry3.get()}\n\nдобавлен на склад!')
                    # Запись в файл введенных данных
                    file = open('warehouse(lesson8-4,5,6).txt', 'a')
                    self.dict = {"Название товара": self.entry1.get(), "Цена": self.entry2.get(),
                                 "Количество": self.entry3.get()}
                    file.write(str(self.dict) + '\n')
                    file.close()
                else:
                    messagebox.showinfo("ОШИБКА!", f'Проверьте заполенение строк с ценой и количеством товара!')

        def back_on_window(self):
            self.window_add.withdraw()
            self.window.deiconify()

        # ------------------------ Окно 2: Удаление и просмотр товаров. -------------------------------------------------------
        def del_product(self):
            self.window_del = Tk()
            self.window.withdraw()
            self.window_del.geometry('600x400')
            self.window_del.title('Удаление товара со склада Ardalion')

            self.frame_del = Frame(self.window_del)
            self.label_del = Label(self.frame_del, text="Введите наименование товара для удаления: ", font='Arial 13',
                                   bg='orange', fg='snow')
            self.label_del.pack(side='left')
            self.entry_del = Entry(self.frame_del, width=20, font='Arial 15')
            self.entry_del.pack(side='left', padx=10)
            self.frame_del.pack(padx=10, pady=10)

            self.frame_del2 = Frame(self.window_del)
            self.button_list_del = Button(self.frame_del2, text='Просмотреть весь товар на складе', font='Arial 14',
                                          bg='grey', relief='ridge', command=self.show_list_for_del)
            self.button_list_del.pack(side='left', padx=10, pady=0)

            self.button_list_del_2 = Button(self.frame_del2, text='Удалить', font='Arial 14',
                                            bg='grey', relief='flat', command=self.delete_name)
            self.button_list_del_2.pack(side='left', padx=10, pady=0)
            self.frame_del2.pack(padx=10, pady=10)

            # Кнопка '<- Вернуться назад'
            self.button_frame_list_2_2 = Frame(self.window_del)
            self.button_add_list_2_2 = Button(self.button_frame_list_2_2, text='<- Вернуться назад', font='Arial 13',
                                              bg='grey', command=self.back_on_window_2)
            self.button_add_list_2_2.pack(padx=10, pady=10)
            self.button_frame_list_2_2.pack(padx=10, anchor=E)

        def back_on_window_2(self):
            self.window_del.withdraw()
            self.window.deiconify()

        def show_list_for_del(self):
            self.frame_del3_show_list = Frame(self.window_del)
            self.label_list_del = Label(self.frame_del3_show_list, text='Название товара')
            self.label_list_del2 = Label(self.frame_del3_show_list, text='Цена (шт.)')
            self.label_list_del3 = Label(self.frame_del3_show_list, text='Количество')
            self.label_list_del.pack(side='left', padx=60)
            self.label_list_del2.pack(side='left', padx=60)
            self.label_list_del3.pack(side='left', padx=60)
            self.frame_del3_show_list.pack()

            self.frame_del4_show_list = Frame(self.window_del)
            self.canvas = Canvas(self.frame_del4_show_list, width=600, height=5)
            self.canvas.create_line(2, 2, 599, 2, width=3)
            self.canvas.pack()
            self.frame_del4_show_list.pack()

            file2 = open('warehouse(lesson8-4,5,6).txt', 'r')
            for line in file2:
                str_on_dict = ast.literal_eval(line)
                self.local_frame = Frame(self.window_del)

                self.local_frame_in1 = Frame(self.local_frame)
                self.text_str1 = Label(self.local_frame_in1, text=f"{str_on_dict['Название товара']:<10}")
                self.text_str1.pack(pady=3, ipadx=40)
                self.local_frame_in1.pack(side='left', ipadx=40)

                self.local_frame_in2 = Frame(self.local_frame)
                self.text_str2 = Label(self.local_frame_in2, text=f"{str_on_dict['Цена']:<10}")
                self.text_str2.pack(pady=3, ipadx=40)
                self.local_frame_in2.pack(side='left', ipadx=40)

                self.local_frame_in3 = Frame(self.local_frame)
                self.text_str3 = Label(self.local_frame_in3, text=f"{str_on_dict['Количество']:<0}")
                self.text_str3.pack(pady=3, ipadx=40)
                self.local_frame_in3.pack(side='left', ipadx=40)
                self.local_frame.pack()
            file2.close()

        def delete_name(self):
            check = self.entry_del.get()

            if len(check) < 2:
                messagebox.showinfo("ОШИБКА!", f'Проверьте правильность заполнения строки!')
            elif len(check) > 1 and check.isnumeric() == True:
                messagebox.showinfo("ОШИБКА!", f'Название товара не может состоять только из цифр')
            else:
                with open('warehouse(lesson8-4,5,6).txt', 'r') as file3:
                    for line in file3:
                        allresults = re.findall(self.entry_del.get(), line)
                        if allresults:
                            messagebox.showinfo("Удаление успешно", f'Товар {self.entry_del.get()} удален со склада!')
                        if allresults == []:
                            file4 = open('lesson8-4,5,6(dump).txt', 'a')
                            file4.write(line)
                            file4.close()
                    file3.close()

                os.remove('warehouse(lesson8-4,5,6).txt')
                os.rename('lesson8-4,5,6(dump).txt', 'warehouse(lesson8-4,5,6).txt')

        # ------------------------ Окно 3: Просмотр товаров в отделах. -------------------------------------------------------
        def window_show(self):
            self.window_show = Tk()
            self.window.withdraw()
            self.window_show['bg'] = 'orange'
            self.window_show.wm_attributes('-alpha', 0.92)
            self.window_show.geometry('600x400')
            self.window_show.title('Просмотр техники (товаров) в отделах')

            self.frame_show_1 = Frame(self.window_show)
            self.label_1 = Label(self.frame_show_1, text='Финансовый отдел:', font="Arial 13")
            self.label_1.pack()
            file5 = open('lesson8-4,5,6(info1).txt', "r", encoding='utf-8')
            for i in file5:
                str_on_dict2 = ast.literal_eval(i)
                a = (f"Техника {str_on_dict2['Название товара']} в количестве {str_on_dict2['Количество']} шт.")
                self.label_2 = Label(self.frame_show_1, text=a, font="Arial 12", relief='groove', height=1)
                self.label_2.pack(pady=1)
            file5.close()
            self.frame_show_1.pack(side='left', padx=10)

            self.frame_show_2 = Frame(self.window_show)
            self.label_12 = Label(self.frame_show_2, text='Производственный отдел:', font="Arial 13")
            self.label_12.pack()
            file6 = open('lesson8-4,5,6(info2).txt', "r", encoding='utf-8')
            for i in file6:
                str_on_dict2 = ast.literal_eval(i)
                a = (f"Техника {str_on_dict2['Название товара']} в количестве {str_on_dict2['Количество']} шт.")
                self.label_22 = Label(self.frame_show_2, text=a, font="Arial 12", relief='groove', height=1)
                self.label_22.pack(pady=1)
            file5.close()
            self.frame_show_2.pack(side='left', padx=10)

            # Кнопка '<- Вернуться назад'
            self.button_frame_list_2_2_2 = Frame(self.window_show)
            self.button_add_list_2_2_2 = Button(self.button_frame_list_2_2_2, text='<- Вернуться назад',
                                                font='Arial 13',
                                                bg='grey', command=self.back_on_window_3)
            self.button_add_list_2_2_2.pack(padx=10, pady=10)
            self.button_frame_list_2_2_2.place(x=10, y=10)

            # Кнопка 'Изменить список'
            self.button_frame_list_q = Frame(self.window_show)
            self.button_add_list_q = Button(self.button_frame_list_q, text='Изменить список',
                                            font='Arial 13', bg='grey', command=self.change_part)
            self.button_add_list_q.pack(padx=10, pady=10)
            self.button_frame_list_q.place(x=200, y=10)

        def back_on_window_3(self):
            self.window_show.withdraw()
            self.window.deiconify()

        def change_part(self):
            self.main_window = Tk()
            self.main_window.geometry('300x300')
            self.frame100 = Frame(self.main_window)
            self.labelll = Label(self.frame100, text='Выберите отдел', font='Arial 13')
            self.labelll.pack()
            self.frame100.pack()

            self.frame99 = Frame(self.main_window)
            self.cb1 = Button(self.frame99, text='1. Финансовый отдел', command=self.open_file_1)
            self.cb2 = Button(self.frame99, text='2. Производственный отдел', command=self.open_file_2)
            self.cb1.pack()
            self.cb2.pack()
            self.frame99.pack()

        def open_file_1(self):
            os.startfile('lesson8-4,5,6(info1).txt')

        def open_file_2(self):
            os.startfile('lesson8-4,5,6(info2).txt')

    office = OfficeTech()


warehouse()

#
#
#     class Printer(OfficeTechniks):
#         def to_print(self):
#             return f'to print smth {self.numb} times'
#
#
#     class Scanner(OfficeTechniks):
#         def to_scan(self):
#             return f'to scan smth {self.numb} times'
#
#
#     class Copier(OfficeTechniks):
#         def to_copier(self):
#             return f'to copier smth  {self.numb} times'
#
