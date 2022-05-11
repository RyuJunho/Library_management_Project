from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from book_Pandas_Class import*


def book_append(main) :    #도서등록(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

    # 추가 버튼을 클릭했을 때 호출되는 이벤트 핸들러
    def append():
        print('추가 버튼 클릭')
        # 빈칸이 있으면
        # 메시지박스 출력 후 등록화면창으로 돌아감
        if len(B_nameEntry.get()) == 0 or len(B_PubEntry.get()) == 0 or len(B_ISBNEntry.get()) == 0 or len(
                B_LinkEntry.get()) == 0 or len(B_PriEntry.get()) == 0 or len(B_WirEntry.get()) == 0 or len(
                B_Intrscr.get("1.0", "end-1c")) == 0:
                    messagebox.showerror("도서 관리 프로그램", "빈칸이 존재합니다.\n빈칸을 입력하세요.")

        # 등록을 묻는 메시지박스 출력 (예, 아니오)
        else:
            AppCheckBox = messagebox.askokcancel("도서 관리 프로그램", "도서를 등록하시겠습니까?")
            # '예'를 누를경우
            # 등록되었다는 메시지박스 출력 (확인)
            # 엔트리와 텍스트의 내용을 비움
            if AppCheckBox == 1:
                if B_ISBNEntry.get().isdigit() and B_PriEntry.get().isdigit() and B_ISBNEntry.get().isdecimal(): # 가격과 ISBN이 숫자인 경우
                    book_append_p = book_Pandas.book_append(B_ISBNEntry.get(),B_nameEntry.get(), B_WirEntry.get(), B_PubEntry.get(), 
                                                            B_PriEntry.get(), B_LinkEntry.get(), B_Intrscr.get("1.0", "end"))
                    # ISBN 중복 되면 메시지박스 출력 후 등록화면창으로 돌아감
                    if book_append_p == True:   # 도서 추가 함수 리턴값이 True일 때 도서 추가 불가능 메세지 띄움
                        messagebox.showerror("도서 관리 프로그램", "ISBN이 존재하는 도서입니다.")
                    else: 
                        messagebox.showinfo("도서 관리 프로그램", "등록되었습니다.")
                        B_nameEntry.delete(0, "end")
                        B_PubEntry.delete(0, "end")
                        B_ISBNEntry.delete(0, "end")
                        B_LinkEntry.delete(0, "end")
                        B_WirEntry.delete(0, "end")
                        B_PriEntry.delete(0, "end")
                        B_Intrscr.delete("1.0", "end")
                else:
                    messagebox.showerror("도서 관리 프로그램", "ISBN과 가격은 숫자를 입력해주세요.")
            # '아니오'를 누를경우
            # 등록화면창으로 돌아감 (내용을 비우지 않음)
            else:
                messagebox.showinfo("도서 관리 프로그램", "등록이 취소 되었습니다.")

    frame = Frame(main)
    book_Pandas = Panda('Book_list.csv', 'user_list.csv','Book_rent.csv')
    # '도서등록' 레이블 생성 글자크기 설정
    # '도서등록' 레이블을 main에 부착
    B_ApeLabel = Label(frame, text ="도서등록", font=(None,12))
    B_ApeLabel.grid(row=1,column=1,pady=10)

    B_frame_1 = Frame(frame)
    B_frame_1.grid(row=2,column=1)

    # '도서명' 레이블 생성
    # '도서명' 레이블을 main에 부착
    B_nameLabel = Label(B_frame_1, text="도서명")
    B_nameLabel.grid(row=1,column=1,padx=10 ,pady=10)

    # '도서명' 엔트리(텍스트박스) 생성
    # '도서명' 엔트리를 main에 부착
    B_nameEntry = Entry(B_frame_1, width=50)
    B_nameEntry.grid(row=1,column=2)

    # '출판사' 레이블 생성
    # '출판사' 레이블을 main에 부착
    B_PubLabel = Label(B_frame_1, text ="출판사")
    B_PubLabel.grid(row=2,column=1,pady=10)

    # '출판사' 엔트리(텍스트박스) 생성
    # '출판사' 엔트리를 main에 부착
    B_PubEntry = Entry(B_frame_1, width=50)
    B_PubEntry.grid(row=2,column=2)

    # 'ISBN' 레이블 생성
    # 'ISBN' 레이블을 main에 부착
    B_ISBNLabel = Label(B_frame_1, text ="ISBN")
    B_ISBNLabel.grid(row=3,column=1,pady=10)

    # 'ISBN' 엔트리(텍스트박스) 생성
    # 'ISBN' 엔트리를 main에 부착
    B_ISBNEntry = Entry(B_frame_1, width=50)
    B_ISBNEntry.grid(row=3,column=2)

    # '관련링크' 이블 생성
    # '관련링크' 레이블을 main에 부착
    B_LinkLabel = Label(B_frame_1, text ="관련링크")
    B_LinkLabel.grid(row=4,column=1,pady=10)

    # '관련링크' 엔트리(텍스트박스) 생성
    # '관련링크' 엔트리를 main에 부착
    B_LinkEntry = Entry(B_frame_1, width=50)
    B_LinkEntry.grid(row=4,column=2)

    # '저자' 레이블 생성
    # '저자' 레이블을 main에 부착
    B_WirLabel = Label(B_frame_1, text ="저자")
    B_WirLabel.grid(row=5,column=1,pady=10)

    B_frame_2 = Frame(B_frame_1)
    B_frame_2.grid(row=5,column=2)

    # '저자' 엔트리(텍스트박스) 생성
    # '저자' 엔트리를 main에 부착
    B_WirEntry = Entry(B_frame_2, width=23)
    B_WirEntry.grid(row=1,column=1)

    # '가격' 레이블 생성
    # '가격' 레이블을 main에 부착
    B_PriLabel = Label(B_frame_2, text ="가격")
    B_PriLabel.grid(row=1,column=2,padx=10)

    # '가격' 엔트리(텍스트박스) 생성
    # '가격' 엔트리를 main에 부착
    B_PriEntry = Entry(B_frame_2, width=20)
    B_PriEntry.grid(row=1,column=3)

    # '도서소개' 레이블 생성
    # '도서소개' 레이블을 main에 부착
    B_IntrLabel = Label(frame, text ="도서소개")
    B_IntrLabel.grid(row=3,column=1,pady=10)

    # '도서소개' 스크롤텍스트(ScrolledText) 생성
    # '도서소개' 스크롤텍스트(ScrolledText) main에 부착
    B_Intrscr = scrolledtext.ScrolledText(frame, width=100, height=10, wrap=WORD)
    B_Intrscr.grid(row=4,column=1)

    # '추가'버튼 생성 (command = append)
    # 버튼을 main 부착
    B_AppButton = Button(frame,text="추가", width=8, command=append)
    B_AppButton.grid(row=5,column=1,pady=30)

    return frame