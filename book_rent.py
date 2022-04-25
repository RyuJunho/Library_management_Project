from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from book_Pandas_Class import *
from datetime import datetime, timedelta


def book_rent(main):
    # 전화번호로 회원을 확인
    # 전화번호로 회원을 확인
    def Phone_input():
        if len(P_ShrEntry.get()) == 13: #전화번호 형식인지 확인
            try :
                phone = str(P_ShrEntry.get())
                user_data_list = book_Pandas.user_check(phone)[0]   #전화번호로 회원데이터 추출
                print(user_data_list)
            except :
                messagebox.showerror("도서 관리 프로그램", "존재하지 않는 회원입니다.")
                return False

            PhoneCheckBox = messagebox.askokcancel("도서 관리 프로그램", user_data_list[0]+"님이 맞으십니까?")
            if PhoneCheckBox == 1:
                rent_insert(user_data_list[0])

        else:
            messagebox.showerror("도서 관리 프로그램", "형식에 맞게 입력해주세요.")
            
    # 도서 대출 버튼
    def book_rentButton(rent_main):
        rent_date = (datetime.today()).strftime("%Y-%m-%d")  # 대여일
        return_date = (datetime.today() + timedelta(14)).strftime("%Y-%m-%d")  # 대여 기간 계산
        book_Pandas.book_rent(P_ShrEntry.get(), getValue[2], rent_date, return_date)
        messagebox.showinfo("도서 관리 프로그램", "대출되었습니다.\n(반납예정일 : " + return_date + ")")
        phone_serch.destroy()  # 확인을 누르면 창 닫기
        rent_main.destroy()

    # 도서 검색 클래스
    def search():
        srh_np = book_Pandas.book_search(Rent_Box.get(), Rent_ShrEntry.get())
        print(srh_np)
        re(Rent_ShrTreeV)
        for i in srh_np.tolist():
            Rent_ShrTreeV.insert('', 'end', text=i, values=i)

    # 검색 버튼 클릭 시 데이터 삭제
    def re(Treeview):
        for row in Treeview.get_children():
            Treeview.delete(row)

            # 트리뷰 클릭 이벤트

    def click_item(event):
        selectedItem = Rent_ShrTreeV.focus()
        global getValue
        getValue = Rent_ShrTreeV.item(selectedItem, 'values')
        Book_info()  # 새창 불러오는 함수 사용

    # 엔트리에 데이터 삽입
    def df_insert(rent_entry, num, data):
        rent_entry.insert(num, data)
        rent_entry.config(state='disabled')

    # 대여 도서 트리뷰 데이터 삽입
    def rent_insert(tree):
        rent_np = book_Pandas.rent_data(getValue[2])
        for i in rent_np.tolist():
            tree.insert('', 'end', text=i, values=i)

    # 트리튜 클릭 시 나오는 새창
    def Book_info():
        rent_main = Tk()
        rent_main.geometry("800x600")

        frame = Frame(rent_main)

        # '도서대출' 레이블 생성 글자크기 설정
        # '도서대출' 레이블을 main에 부착
        B_RentLabel = Label(frame, text="도서 대출", font=(None, 12))
        B_RentLabel.grid(row=1, column=1, pady=10)

        Rent_frame = Frame(frame)
        Rent_frame.grid(row=2, column=1)

        # '도서명' 레이블 생성
        # '도서명' 레이블을 main에 부착
        B_RnameLabel = Label(Rent_frame, text="도서명")
        B_RnameLabel.grid(row=1, column=1, padx=10, pady=10)

        # '도서명' 엔트리(텍스트박스) 생성
        # '도서명' 엔트리를 읽기전용으로 상태설정
        # '도서명' 엔트리를 main에 부착
        B_RnameEntry = Entry(Rent_frame, width=50)
        B_RnameEntry.grid(row=1, column=2)

        # '출판사' 레이블 생성
        # '출판사' 레이블을 main에 부착
        B_RPubLabel = Label(Rent_frame, text="출판사")
        B_RPubLabel.grid(row=2, column=1, pady=10)

        # '출판사' 엔트리(텍스트박스) 생성
        # '출판사' 엔트리를 읽기전용으로 상태설정
        # '출판사' 엔트리를 main에 부착
        B_RPubEntry = Entry(Rent_frame, width=50)
        B_RPubEntry.grid(row=2, column=2)

        # 'ISBN' 레이블 생성
        # 'ISBN' 레이블을 main에 부착
        B_RISBNLabel = Label(Rent_frame, text="ISBN")
        B_RISBNLabel.grid(row=3, column=1, pady=10)

        # 'ISBN' 엔트리(텍스트박스) 생성
        # 'ISBN' 엔트리를 읽기전용으로 상태설정
        # 'ISBN' 엔트리를 main에 부착
        B_RISBNEntry = Entry(Rent_frame, width=50)
        B_RISBNEntry.grid(row=3, column=2)

        # '관련링크' 이블 생성
        # '관련링크' 레이블을 main에 부착
        B_RLinkLabel = Label(Rent_frame, text="관련링크")
        B_RLinkLabel.grid(row=4, column=1, pady=10)

        # '관련링크' 엔트리(텍스트박스) 생성
        # '관련링크' 엔트리를 읽기전용으로 상태설정
        # '관련링크' 엔트리를 main에 부착
        B_RLinkEntry = Entry(Rent_frame, width=50)
        B_RLinkEntry.grid(row=4, column=2)

        # '저자' 레이블 생성
        # '저자' 레이블을 main에 부착
        B_RWirLabel = Label(Rent_frame, text="저자")
        B_RWirLabel.grid(row=5, column=1)

        Rent_frame_2 = Frame(Rent_frame)
        Rent_frame_2.grid(row=5, column=2)

        # '저자' 엔트리(텍스트박스) 생성
        # '저자' 엔트리를 읽기전용으로 상태설정
        # '저자' 엔트리를 main에 부착
        B_RWirEntry = Entry(Rent_frame_2, width=23)
        B_RWirEntry.grid(row=1, column=1)

        # '가격' 레이블 생성
        # '가격' 레이블을 main에 부착
        B_RPriLabel = Label(Rent_frame_2, text="가격")
        B_RPriLabel.grid(row=1, column=2, padx=10)

        # '가격' 엔트리(텍스트박스) 생성
        # '가격' 엔트리를 읽기전용으로 상태설정
        # '가격' 엔트리를 main에 부착
        B_RPriEntry = Entry(Rent_frame_2, width=20)
        B_RPriEntry.grid(row=1, column=3)

        # '도서소개' 레이블 생성
        # '도서소개' 레이블을 main에 부착
        B_RIntrLabel = Label(frame, text="도서소개")
        B_RIntrLabel.grid(row=3, column=1, pady=10)

        # '도서소개' 스크롤텍스트(ScrolledText) 생성
        # '도서소개' 스크롤텍스트 읽기전용으로 상태설정
        # '도서소개' 스크롤텍스트(ScrolledText) main에 부착
        B_RIntrscr = scrolledtext.ScrolledText(frame, width=80, height=8, wrap=WORD)
        B_RIntrscr.grid(row=4, column=1)

        book_bookC_np = book_Pandas.ISBN_check(int(getValue[2]))

        df_insert(B_RISBNEntry, 0, book_bookC_np[0][0])
        df_insert(B_RnameEntry, 0, book_bookC_np[0][1])
        df_insert(B_RWirEntry, 0, book_bookC_np[0][2])
        df_insert(B_RPubEntry, 0, book_bookC_np[0][3])
        df_insert(B_RPriEntry, 0, book_bookC_np[0][4])
        df_insert(B_RLinkEntry, 0, book_bookC_np[0][5])
        df_insert(B_RIntrscr, "1.0", book_bookC_np[0][6])

        B_RentButton = Button(frame, text="대출", width=8, command= lambda : book_rentButton(rent_main))
        B_RentButton.grid(row=6, column=1, pady=30)
        # if(대출이 가능할 경우):
        if book_bookC_np[0][7] == True:
            pass
        # else(대출이 불가능한 경우):
        else:
            B_RentButton.config(state='disabled')
            norent_columns = ('U_name', 'return_date')
            NoRent_TreeV = Treeview(frame, columns=norent_columns, show='headings')
            NoRent_TreeV.grid(row=5, column=1, pady=10)
            NoRent_TreeV.configure(height=1)
            # 각 컬럼 설정
            # '도서명'컬럼
            NoRent_TreeV.column("U_name", width=120)
            NoRent_TreeV.heading("U_name", text="전화번호")
            # '저자'컬럼
            NoRent_TreeV.column("return_date", width=120)
            NoRent_TreeV.heading("return_date", text="반납예정일")
            rent_insert(NoRent_TreeV)

        frame.pack()
        rent_main.mainloop()

    book_Pandas = Panda('Book_list.csv', 'user_list.csv', 'Book_rent.csv')

    phone_serch = Toplevel(main)
    phone_serch.geometry("360x120")

    # 전화번호 입력 창 레이블
    ShrLabel = Label(phone_serch, text="000-0000-0000 으로 입력하세요.")
    ShrLabel.pack(padx=20, pady=10)
    P_ShrLabel = Label(phone_serch, text="전화번호")
    P_ShrLabel.pack(side=LEFT, padx=20)

    # 전화번호 입력 창 엔트리
    P_ShrEntry = Entry(phone_serch, width=20)
    P_ShrEntry.pack(side=LEFT)

    # 전화번호 입력 창 버튼
    P_ShrButton = Button(phone_serch, text="입력", width=8, command=Phone_input)
    P_ShrButton.pack(side=LEFT)

    frame = Frame(main)
    # '대출' 레이블 생성 글자크기 설정
    # 레이블을 main윈도우에 부착
    Rent_Label = Label(frame, text="대출", font=(None, 14))
    Rent_Label.pack(pady=30)

    R_search_frame = Frame(frame)  # 콤보박스, 엔트리, 버튼이 들어갈 프레임 생성

    # 콤보박스 생성(제목,저자) (읽기전용으로 설정)
    # 콤보박스 초기값을 '제목'으로 설정
    # 콤보박스를 search_frame에 부착
    Rent_Box = Combobox(R_search_frame, width=6, values=["제목", "저자"])
    Rent_Box.current(0)
    Rent_Box.pack(side=LEFT, padx=10, pady=10)

    # 엔트리(텍스트박스) 생성
    # 엔트리를 search_frame에 부착
    Rent_ShrEntry = Entry(R_search_frame, width=40)
    Rent_ShrEntry.pack(side=LEFT, pady=10)

    # '검색'버튼 생성
    # 버튼을 search_frame에 부착
    Rent_ShrButton = Button(R_search_frame, text="검색", width=8, command=search)
    Rent_ShrButton.pack(side=LEFT, padx=10, pady=10)

    # search_frame을 main윈도우에 부착
    R_search_frame.pack()

    # 트리뷰(표) 생성
    # 표를 main에 부착
    Rent_columns = ('B_name', 'writer', 'ISBN', 'RentPossi')
    Rent_ShrTreeV = Treeview(frame, columns=Rent_columns, show='headings')
    Rent_ShrTreeV.pack(pady=10)
    Rent_ShrTreeV.bind("<<TreeviewSelect>>", click_item)

    # 각 컬럼 설정
    # '도서명'컬럼
    Rent_ShrTreeV.column("B_name", width=140)
    Rent_ShrTreeV.heading("B_name", text="도서명")
    # '저자'컬럼
    Rent_ShrTreeV.column("writer", width=120)
    Rent_ShrTreeV.heading("writer", text="저자")
    # 'ISBN'컬럼
    Rent_ShrTreeV.column("ISBN", width=120)
    Rent_ShrTreeV.heading("ISBN", text="ISBN")
    # '대출가능여부'컬럼
    Rent_ShrTreeV.column("RentPossi", width=120)
    Rent_ShrTreeV.heading("RentPossi", text="대출가능여부")

    return frame

