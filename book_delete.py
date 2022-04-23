from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from book_Pandas_Class import*

def book_delete(main) :    #도서수정(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

    # 삭제 버튼을 클릭했을 때 호출되는 이벤트 핸들러
    def delete():
        print('삭제 버튼 클릭')
        # 대여중인 도서이면
        # 메시지출력 후 삭제화면창으로 돌아감
        book_Pandas = Panda('Book_list.csv', 'user_list.csv','Book_rent.csv')
        book_delete_p = book_Pandas.book_delete(ISBN_Entry.get())
        if book_delete_p == False: # ISBN이 동일한지(임시데이터)
            messagebox.showerror('도서 관리 프로그램', "대여중인 도서입니다.")
        else:
        # 삭제를 묻는 메시지박스 출력 (예, 아니오)
            DelCheckBox = messagebox.askokcancel('도서 관리 프로그램', "도서를 삭제하시겠습니까?")
            # '예'를 누를경우
            # csv파일에서 데이터 삭제 (아직 구현 x)
            # 삭제되었다는 메시지박스 출력 (확인)
            # 메인창으로 이동
            if DelCheckBox == 1:
                messagebox.showinfo('도서 관리 프로그램', "삭제되었습니다.")
                ISBN_serch.destroy() # 확인을 누르면 창 닫기
            # '아니오'를 누를경우
            # 삭제화면창으로 돌아감
            else:
                messagebox.showinfo('도서 관리 프로그램', "삭제가 취소 되었습니다.")

    def ISBN_input():
            print("ISBN 입력")
            book_Pandas = Panda('Book_list.csv', 'user_list.csv','Book_rent.csv')
            ISBN_np = book_Pandas.del_ISBN(ISBN_Entry.get())    # 클래스에서 반환된 넘파이 불러옴
            if ISBN_np[0][0] == int(ISBN_Entry.get()): # ISBN이 동일한지(임시데이터)
                df_insert(B_DISBNEntry, 0, ISBN_np[0][0])
                df_insert(B_nameEntry, 0, ISBN_np[0][1])
                df_insert(B_DWirEntry, 0, ISBN_np[0][2])
                df_insert(B_DPubEntry, 0, ISBN_np[0][3])
                df_insert(B_DPriEntry, 0, ISBN_np[0][4])
                df_insert(B_DLinkEntry, 0, ISBN_np[0][5])
                df_insert(B_DIntrscr, "1.0", ISBN_np[0][6])
            else:
                messagebox.showerror('도서 관리 프로그램', "존재하지 않는 회원입니다.")
    
    def df_insert(del_entry,num, ISBN):
        del_entry.insert(num,ISBN)
        del_entry.config(state='disabled')
    
    ISBN_serch = Toplevel(main)
    ISBN_serch.geometry("340x120")

    # 전화번호 입력 창 레이블
    ISBN_Label = Label(ISBN_serch, text ="ISBN")
    ISBN_Label.pack(side=LEFT, padx=20)

    # 전화번호 입력 창 엔트리
    ISBN_Entry = Entry(ISBN_serch, width=20)
    ISBN_Entry.pack(side=LEFT)

    # 전화번호 입력 창 버튼
    ISBN_Button = Button(ISBN_serch,text="입력", width=8, command=ISBN_input)
    ISBN_Button.pack(side=LEFT)            

    frame = Frame(main)

    # 엔트리, 스크롤텍스트의 데이터 값은 csv파일에서 읽어옴 (아직 구현 x)
    # 데이터가 비어있는 상태로 임시구현

    # '도서 삭제' 레이블 생성 글자크기 설정
    # '도서 삭제' 레이블을 main에 부착
    B_delLabel = Label(frame, text ="도서 삭제", font=(None,12))
    B_delLabel.grid(row=1,column=1,pady=10)

    B_Delframe_1 = Frame(frame)
    B_Delframe_1.grid(row=2,column=1)

    # '도서명' 레이블 생성
    # '도서명' 레이블을 main에 부착
    B_DnameLabel = Label(B_Delframe_1, text="도서명")
    B_DnameLabel.grid(row=1,column=1,padx=10 ,pady=10)

    # '도서명' 엔트리(텍스트박스) 생성
    # '도서명' 엔트리를 읽기전용으로 상태설정
    # '도서명' 엔트리를 main에 부착
    B_nameEntry = Entry(B_Delframe_1, width=50)
    B_nameEntry.grid(row=1,column=2)

    # '출판사' 레이블 생성
    # '출판사' 레이블을 main에 부착
    B_DPubLabel = Label(B_Delframe_1, text ="출판사")
    B_DPubLabel.grid(row=2,column=1,pady=10)

    # '출판사' 엔트리(텍스트박스) 생성
    # '출판사' 엔트리를 읽기전용으로 상태설정
    # '출판사' 엔트리를 main에 부착
    B_DPubEntry = Entry(B_Delframe_1, width=50)
    B_DPubEntry.grid(row=2,column=2)

    # 'ISBN' 레이블 생성
    # 'ISBN' 레이블을 main에 부착
    B_DISBNLabel = Label(B_Delframe_1, text ="ISBN")
    B_DISBNLabel.grid(row=3,column=1,pady=10)

    # 'ISBN' 엔트리(텍스트박스) 생성
    # 'ISBN' 엔트리를 읽기전용으로 상태설정
    # 'ISBN' 엔트리를 main에 부착
    B_DISBNEntry = Entry(B_Delframe_1, width=50)
    B_DISBNEntry.grid(row=3,column=2)

    # '관련링크' 이블 생성
    # '관련링크' 레이블을 main에 부착
    B_DLinkLabel = Label(B_Delframe_1, text ="관련링크")
    B_DLinkLabel.grid(row=4,column=1,pady=10)

    # '관련링크' 엔트리(텍스트박스) 생성
    # '관련링크' 엔트리를 읽기전용으로 상태설정
    # '관련링크' 엔트리를 main에 부착
    B_DLinkEntry = Entry(B_Delframe_1, width=50)
    B_DLinkEntry.grid(row=4,column=2)

    # '저자' 레이블 생성
    # '저자' 레이블을 main에 부착
    B_DWirLabel = Label(B_Delframe_1, text ="저자")
    B_DWirLabel.grid(row=5,column=1,pady=10)

    B_Delframe_2 = Frame(B_Delframe_1)
    B_Delframe_2.grid(row=5,column=2)

    # '저자' 엔트리(텍스트박스) 생성
    # '저자' 엔트리를 읽기전용으로 상태설정
    # '저자' 엔트리를 main에 부착
    B_DWirEntry = Entry(B_Delframe_2, width=23)
    B_DWirEntry.grid(row=1,column=1)

    # '가격' 레이블 생성
    # '가격' 레이블을 main에 부착
    B_DPriLabel = Label(B_Delframe_2, text ="가격")
    B_DPriLabel.grid(row=1,column=2,padx=10)

    # '가격' 엔트리(텍스트박스) 생성
    # '가격' 엔트리를 읽기전용으로 상태설정
    # '가격' 엔트리를 main에 부착
    B_DPriEntry = Entry(B_Delframe_2, width=20)
    B_DPriEntry.grid(row=1,column=3)

    # '도서소개' 레이블 생성
    # '도서소개' 레이블을 main에 부착
    B_DIntrLabel = Label(frame, text ="도서소개")
    B_DIntrLabel.grid(row=3,column=1,pady=10)

    # '도서소개' 스크롤텍스트(ScrolledText) 생성
    # '도서소개' 스크롤텍스트 읽기전용으로 상태설정
    # '도서소개' 스크롤텍스트(ScrolledText) main에 부착
    B_DIntrscr = scrolledtext.ScrolledText(frame, width=100, height=10, wrap=WORD)
    B_DIntrscr.grid(row=4,column=1)

    # '삭제'버튼 생성 (command = delete)
    # 버튼을 main 부착
    B_DelButton = Button(frame,text="삭제", width=8, command=delete)
    B_DelButton.grid(row=5,column=1,pady=30)

    return frame
