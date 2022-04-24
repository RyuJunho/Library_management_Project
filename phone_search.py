from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from book_Pandas_Class import *
from book_rent import *


def phone_search(main):
    def Phone_input():
            print("전화번호 입력")
            book_userC_p = book_Pandas.user_check(P_ShrEntry.get())
            
            if len(P_ShrEntry.get()) < 13 and P_ShrEntry.get().isdigit():
                messagebox.showerror("도서 관리 프로그램", "잘못된 형식입니다.")

            else:     
                if book_userC_p[0][0] == P_ShrEntry.get():  # 전화번호가 동일한지(임시데이터)
                    PhoneCheckBox = messagebox.askokcancel("도서 관리 프로그램", book_userC_p[0][1] + "님이 맞으십니까?")
                    if PhoneCheckBox == 1:
                        pass
                else:
                    messagebox.showerror("도서 관리 프로그램", "존재하지 않는 회원입니다.")
        

    book_Pandas = Panda('Book_list.csv', 'user_list.csv', 'Book_rent.csv')
    frame = Frame(main)

    # 전화번호 입력 창 레이블
    ShrLabel = Label(frame, text="000-0000-0000 으로 입력하세요.")
    ShrLabel.pack(padx=20, pady=10)
    P_ShrLabel = Label(frame, text="전화번호")
    P_ShrLabel.pack(side=LEFT, padx=20)

    # 전화번호 입력 창 엔트리
    P_ShrEntry = Entry(frame, width=20)
    P_ShrEntry.pack(side=LEFT)

    # 전화번호 입력 창 버튼
    P_ShrButton = Button(frame, text="입력", width=8, command=Phone_input)
    P_ShrButton.pack(side=LEFT)
    
    return frame