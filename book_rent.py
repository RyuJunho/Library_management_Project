from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

# 전화번호로 회원을 확인
def Phone_input():
    print("전화번호 입력")
    if P_ShrEntry.get() == "1": # 전화번호가 동일한지(임시데이터)
        PhoneCheckBox = messagebox.askokcancel("본인확인", "'김길동'님이 맞으십니까?")
        if PhoneCheckBox == 1:
            phone_serch.destroy() # 확인을 누르면 창 닫기
    else:
        PhoneErBox = messagebox.showerror("확인불가", "존재하지 않는 회원입니다.")

# 도서 대출 버튼
def book_rentButton():
    RentYesBox = messagebox.showinfo("대출완료", "대출되었습니다.\n(반납예정일 : 2022)")
    
# 트리뷰 클릭 이벤트
def click_item(event): 
    selectedItem = Rent_ShrTreeV.focus() 
    getValue = Rent_ShrTreeV.item(selectedItem, 'values')
    Book_rent() # 새창 불러오는 함수 사용
   
# 트리튜 클릭 시 나오는 새창 
def Book_rent():
    rent_main = Tk()
    rent_main.geometry("800x500")

    frame = Frame(rent_main)

    # '도서대출' 레이블 생성 글자크기 설정
    # '도서대출' 레이블을 main에 부착
    B_RentLabel = Label(frame, text ="도서 대출", font=(None,12))
    B_RentLabel.grid(row=1,column=1,pady=10)

    Rent_frame = Frame(frame)
    Rent_frame.grid(row=2,column=1)

    # '도서명' 레이블 생성
    # '도서명' 레이블을 main에 부착
    B_RnameLabel = Label(Rent_frame, text="도서명")
    B_RnameLabel.grid(row=1,column=1,padx=10 ,pady=10)

    # '도서명' 엔트리(텍스트박스) 생성
    # '도서명' 엔트리를 읽기전용으로 상태설정
    # '도서명' 엔트리를 main에 부착
    B_RnameEntry = Entry(Rent_frame, width=50)
    B_RnameEntry.insert(0,"따라하며 배우는 파이썬과 데이터 과학")
    B_RnameEntry.config(state='disabled')
    B_RnameEntry.grid(row=1,column=2)

    # '출판사' 레이블 생성
    # '출판사' 레이블을 main에 부착
    B_RPubLabel = Label(Rent_frame, text ="출판사")
    B_RPubLabel.grid(row=2,column=1,pady=10)

    # '출판사' 엔트리(텍스트박스) 생성
    # '출판사' 엔트리를 읽기전용으로 상태설정
    # '출판사' 엔트리를 main에 부착
    B_RPubEntry = Entry(Rent_frame, width=50)
    B_RPubEntry.insert(0,"생능출판사")
    B_RPubEntry.config(state='disabled')
    B_RPubEntry.grid(row=2,column=2)

    # 'ISBN' 레이블 생성
    # 'ISBN' 레이블을 main에 부착
    B_RISBNLabel = Label(Rent_frame, text ="ISBN")
    B_RISBNLabel.grid(row=3,column=1,pady=10)

    # 'ISBN' 엔트리(텍스트박스) 생성
    # 'ISBN' 엔트리를 읽기전용으로 상태설정
    # 'ISBN' 엔트리를 main에 부착
    B_RISBNEntry = Entry(Rent_frame, width=50)
    B_RISBNEntry.insert(0,"9845632")
    B_RISBNEntry.config(state='disabled')
    B_RISBNEntry.grid(row=3,column=2)

    # '관련링크' 이블 생성
    # '관련링크' 레이블을 main에 부착
    B_RLinkLabel = Label(Rent_frame, text ="관련링크")
    B_RLinkLabel.grid(row=4,column=1,pady=10)

    # '관련링크' 엔트리(텍스트박스) 생성
    # '관련링크' 엔트리를 읽기전용으로 상태설정
    # '관련링크' 엔트리를 main에 부착
    B_RLinkEntry = Entry(Rent_frame, width=50)
    B_RLinkEntry.insert(0,"https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=259567419")
    B_RLinkEntry.config(state='disabled')
    B_RLinkEntry.grid(row=4,column=2)

    # '저자' 레이블 생성
    # '저자' 레이블을 main에 부착
    B_RWirLabel = Label(Rent_frame, text ="저자")
    B_RWirLabel.grid(row=5,column=1)

    Rent_frame_2 = Frame(Rent_frame)
    Rent_frame_2.grid(row=5,column=2)

    # '저자' 엔트리(텍스트박스) 생성
    # '저자' 엔트리를 읽기전용으로 상태설정
    # '저자' 엔트리를 main에 부착
    B_RWirEntry = Entry(Rent_frame_2, width=20)
    B_RWirEntry.insert(0,"천인국")
    B_RWirEntry.config(state='disabled')
    B_RWirEntry.grid(row=1,column=1)

    # '가격' 레이블 생성
    # '가격' 레이블을 main에 부착
    B_RPriLabel = Label(Rent_frame_2, text ="가격")
    B_RPriLabel.grid(row=1,column=2,padx=10)

    # '가격' 엔트리(텍스트박스) 생성
    # '가격' 엔트리를 읽기전용으로 상태설정
    # '가격' 엔트리를 main에 부착
    B_RPriEntry = Entry(Rent_frame_2, width=20)
    B_RPriEntry.insert(0,"26000")
    B_RPriEntry.config(state='disabled')
    B_RPriEntry.grid(row=1,column=3)

    # '도서소개' 레이블 생성
    # '도서소개' 레이블을 main에 부착
    B_RIntrLabel = Label(frame, text ="도서소개")
    B_RIntrLabel.grid(row=3,column=1,pady=10)

    # '도서소개' 스크롤텍스트(ScrolledText) 생성
    # '도서소개' 스크롤텍스트 읽기전용으로 상태설정
    # '도서소개' 스크롤텍스트(ScrolledText) main에 부착
    B_RIntrscr = scrolledtext.ScrolledText(frame, width=100, height=10, wrap=WORD)
    B_RIntrscr.insert("1.0","파이썬은 간결한 코드로도 엄청나게 많은 일을 할 수 있으며, 이것이 지금의 영예를 누릴 수 있게 된 가장 중요한 이유이다. 특히 최근의 컴퓨터 과학 분야에서 가장 중요한 영역이라 할 데이터 과학에 최적인 언어이면서, 기계학습과 인공지능 분야의 소프트웨어 개발을 가장 효율적으로 해낼 수 있는 언어이다. 저자들은 독자들에게 파이썬의 문법을 설명하는 일 이상을 하고 싶었다. 그러한 이유로 파이썬의 강력한 능력을 드러내어, 더 깊고 풍부한 프로그래밍의 세계로 독자를 안내하기 위해 이 책을 기획하였다.")
    B_RIntrscr.config(state='disabled')
    B_RIntrscr.grid(row=4,column=1)
    
    # if(대출이 가능할 경우):
    B_RentButton = Button(frame,text="대출", width=8, command=book_rentButton)
    B_RentButton.grid(row=5,column=1,pady=30)
    # else(대출이 불가능한 경우):
    '''
    대여 중인 도서일 경우 이름과 반납예정일
    NoRent_TreeV = Treeview(frame, columns=["one"])
    NoRent_TreeV.grid(row=5,column=1,pady=10)
    NoRent_TreeV.configure(height=2)
    # 각 컬럼 설정
    #'도서명'컬럼
    NoRent_TreeV.column("#0", width=80)
    NoRent_TreeV.heading("#0", text="이름")
    #'저자'컬럼
    NoRent_TreeV.column("#1", width=120)
    NoRent_TreeV.heading("#1", text="반납예정일")
    
    B_RentButton = Button(frame,text="대출", width=8, command=book_rentButton)
    B_RentButton.grid(row=6,column=1)
    '''
    frame.pack()
    rent_main.mainloop()

    
# 전화번호 입력 창
phone_serch = Tk()
phone_serch.geometry("320x120")

# 전화번호 입력 창 레이블
P_ShrLabel = Label(phone_serch, text ="전화번호")
P_ShrLabel.pack(side=LEFT, padx=20)

# 전화번호 입력 창 엔트리
P_ShrEntry = Entry(phone_serch, width=20)
P_ShrEntry.pack(side=LEFT)

# 전화번호 입력 창 버튼
P_ShrButton = Button(phone_serch,text="입력", width=8, command=Phone_input)
P_ShrButton.pack(side=LEFT)
phone_serch.mainloop()

# 임시 윈도우
main = Tk()
main.geometry("800x500")

# '대출' 레이블 생성 글자크기 설정
# 레이블을 main윈도우에 부착
Rent_Label = Label(main, text="대출",font=(None, 14))
Rent_Label.pack(pady=30)

R_search_frame = Frame(main)  # 콤보박스, 엔트리, 버튼이 들어갈 프레임 생성

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
Rent_ShrButton = Button(R_search_frame, text="검색", width=8)
Rent_ShrButton.pack(side=LEFT,padx=10, pady=10)

# search_frame을 main윈도우에 부착
R_search_frame.pack()

# 트리뷰(표) 생성
# 표를 main에 부착
Rent_columns = ('B_name', 'writer', 'ISBN', 'RentPossi')
Rent_ShrTreeV = Treeview(main, columns=Rent_columns, show='headings') 
Rent_ShrTreeV.pack(pady=10)
Rent_ShrTreeV.bind("<<TreeviewSelect>>", click_item)

# 각 컬럼 설정
#'도서명'컬럼
Rent_ShrTreeV.column("B_name", width=140)
Rent_ShrTreeV.heading("B_name", text="도서명")
#'저자'컬럼
Rent_ShrTreeV.column("writer", width=120)
Rent_ShrTreeV.heading("writer", text="저자")
#'ISBN'컬럼
Rent_ShrTreeV.column("ISBN", width=120)
Rent_ShrTreeV.heading("ISBN", text="ISBN")
#'대출가능여부'컬럼
Rent_ShrTreeV.column("RentPossi", width=120)
Rent_ShrTreeV.heading("RentPossi", text="대출가능여부")
# 표에 삽입될 데이터 (아직 구현 x)
Rent_treelist=[(1,"Tom", 80, False), (1,"Bani", 71, True), (1,"Boni", 90, True), (1,"Dannel", 78, True), (1,"Minho", 93, True)]

# 표에 데이터 삽입 (아직 구현 x)
for i in range(len(Rent_treelist)):
    Rent_ShrTreeV.insert('', 'end', text=i, values=Rent_treelist[i], iid=str(i)+"번")

main.mainloop()
