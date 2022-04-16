from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

# 삭제 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def delete():
    print('추가 버튼 클릭')
    #대여중인 도서이면
        #메시지출력 후 삭제화면창으로 돌아감

    #삭제를 묻는 메시지박스 출력 (예, 아니오)
    DelCheckBox = messagebox.askokcancel("도서등록", "도서를 삭제하시겠습니까?")
    #'예'를 누를경우
        #csv파일에서 데이터 삭제 (아직 구현 x)
        #삭제되었다는 메시지박스 출력 (확인)
        #메인창으로 이동
    if DelCheckBox == 1:
        AppYesBox = messagebox.showinfo("삭제완료", "삭제되었습니다.")
    #'아니오'를 누를경우
        #삭제화면창으로 돌아감
    else:
        DelNoBox = messagebox.showinfo("삭제취소", "삭제가 취소 되었습니다.")

# 임시화면
main = Tk()
main.geometry("800x500")

# def book_delete(main) :    #도서수정(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

# 엔트리, 스크롤텍스트의 데이터 값은 csv파일에서 읽어옴 (아직 구현 x)
# 데이터가 비어있는 상태로 임시구현

# '도서 정보 수정' 레이블 생성 글자크기 설정
# '도서 정보 수정' 레이블을 main에 부착
B_DmodLabel = Label(main, text ="도서 정보 수정", font=(None,12))
B_DmodLabel.pack(side=TOP, ipadx=320, pady=20)

# '도서명' 레이블 생성
# '도서명' 레이블을 main에 부착
B_DnameLabel = Label(main, text="도서명")
B_DnameLabel.place(x = 180,y = 60)

# '도서명' 엔트리(텍스트박스) 생성
# '도서명' 엔트리를 읽기전용으로 상태설정
# '도서명' 엔트리를 main에 부착
B_nameEntry = Entry(main, width=50)
B_nameEntry.insert(0,"따라하며 배우는 파이썬과 데이터 과학")
B_nameEntry.config(state='disabled')
B_nameEntry.place(x = 240,y = 60)

# '출판사' 레이블 생성
# '출판사' 레이블을 main에 부착
B_DPubLabel = Label(main, text ="출판사")
B_DPubLabel.place(x = 180,y = 100)

# '출판사' 엔트리(텍스트박스) 생성
# '출판사' 엔트리를 읽기전용으로 상태설정
# '출판사' 엔트리를 main에 부착
B_DPubEntry = Entry(main, width=50)
B_DPubEntry.insert(0,"생능출판사")
B_DPubEntry.config(state='disabled')
B_DPubEntry.place(x = 240,y = 100)

# 'ISBN' 레이블 생성
# 'ISBN' 레이블을 main에 부착
B_DISBNLabel = Label(main, text ="ISBN")
B_DISBNLabel.place(x = 180,y = 140)

# 'ISBN' 엔트리(텍스트박스) 생성
# 'ISBN' 엔트리를 읽기전용으로 상태설정
# 'ISBN' 엔트리를 main에 부착
B_DISBNEntry = Entry(main, width=50)
B_DISBNEntry.insert(0,"9845632")
B_DISBNEntry.config(state='disabled')
B_DISBNEntry.place(x = 240,y = 140)

# '관련링크' 이블 생성
# '관련링크' 레이블을 main에 부착
B_DLinkLabel = Label(main, text ="관련링크")
B_DLinkLabel.place(x = 180,y = 180)

# '관련링크' 엔트리(텍스트박스) 생성
# '관련링크' 엔트리를 읽기전용으로 상태설정
# '관련링크' 엔트리를 main에 부착
B_DLinkEntry = Entry(main, width=50)
B_DLinkEntry.insert(0,"https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=259567419")
B_DLinkEntry.config(state='disabled')
B_DLinkEntry.place(x = 240,y = 180)

# '저자' 레이블 생성
# '저자' 레이블을 main에 부착
B_DWirLabel = Label(main, text ="저자")
B_DWirLabel.place(x = 180,y = 220)

# '저자' 엔트리(텍스트박스) 생성
# '저자' 엔트리를 읽기전용으로 상태설정
# '저자' 엔트리를 main에 부착
B_DWirEntry = Entry(main, width=20)
B_DWirEntry.insert(0,"천인국")
B_DWirEntry.config(state='disabled')
B_DWirEntry.place(x = 240,y = 220)

# '가격' 레이블 생성
# '가격' 레이블을 main에 부착
B_DPriLabel = Label(main, text ="가격")
B_DPriLabel.place(x = 420,y = 220)

# '가격' 엔트리(텍스트박스) 생성
# '가격' 엔트리를 읽기전용으로 상태설정
# '가격' 엔트리를 main에 부착
B_DPriEntry = Entry(main, width=16)
B_DPriEntry.insert(0,"26000")
B_DPriEntry.config(state='disabled')
B_DPriEntry.place(x = 478,y = 220)

# '도서소개' 레이블 생성
# '도서소개' 레이블을 main에 부착
B_DIntrLabel = Label(main, text ="도서소개")
B_DIntrLabel.pack(side=LEFT, padx=40, pady=20)

# '도서소개' 스크롤텍스트(ScrolledText) 생성
# '도서소개' 스크롤텍스트 읽기전용으로 상태설정
# '도서소개' 스크롤텍스트(ScrolledText) main에 부착
B_DIntrscr = scrolledtext.ScrolledText(main, width=100, height=10, wrap=WORD)
B_DIntrscr.insert("1.0","파이썬은 간결한 코드로도 엄청나게 많은 일을 할 수 있으며, 이것이 지금의 영예를 누릴 수 있게 된 가장 중요한 이유이다. 특히 최근의 컴퓨터 과학 분야에서 가장 중요한 영역이라 할 데이터 과학에 최적인 언어이면서, 기계학습과 인공지능 분야의 소프트웨어 개발을 가장 효율적으로 해낼 수 있는 언어이다. 저자들은 독자들에게 파이썬의 문법을 설명하는 일 이상을 하고 싶었다. 그러한 이유로 파이썬의 강력한 능력을 드러내어, 더 깊고 풍부한 프로그래밍의 세계로 독자를 안내하기 위해 이 책을 기획하였다.")
B_DIntrscr.config(state='disabled')
B_DIntrscr.place(x = 40,y = 300)

# '삭제'버튼 생성 (command = delete)
# 버튼을 main 부착
B_DelButton = Button(main,text="삭제", width=8, command=delete)
B_DelButton.place(x = 320,y = 450)

B_DCancButton = Button(main,text="취소", width=8)
B_DCancButton.place(x = 420,y = 450)

main.mainloop()

