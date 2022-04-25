from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from book_Pandas_Class import*

def book_modify(main) :    #도서수정(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임
    # 수정 버튼을 클릭했을 때 호출되는 이벤트 핸들러
    def ISBN_input():
        if P_ShrEntry.get().isdigit: #숫자 형식인지 확인
            try :
                ISBN_check = book_Pandas.ISBN_check(int(P_ShrEntry.get()))   #ISBN로 도서데이터 추출
                print(ISBN_check)
            except :
                messagebox.showerror("도서 관리 프로그램", "존재하지 않는 ISBN입니다.")
                return False
            ISBNCheckBox = messagebox.askokcancel("도서 관리 프로그램", ISBN_check[0][1]+"도서가 맞으십니까?")
            if ISBNCheckBox == 1:
                df_insert(B_MISBNEntry, 0, ISBN_check[0][0])
                df_insert(B_MnameEntry, 0, ISBN_check[0][1])
                df_insert(B_MWirEntry, 0, ISBN_check[0][2])
                df_insert(B_MPubEntry, 0, ISBN_check[0][3])
                df_insert(B_MPriEntry, 0, ISBN_check[0][4])
                df_insert(B_MLinkEntry, 0, ISBN_check[0][5])
                df_insert(B_MIntrscr, "1.0", ISBN_check[0][6])
                pass
        else:
            messagebox.showerror("도서 관리 프로그램", "형식에 맞게 입력해주세요.")
    
    # 엔트리에 데이터 삽입
    def df_insert(rent_entry, num, data):
        rent_entry.insert(num, data)
              
    def modify():
        print('수정 버튼 클릭')
        # 빈칸이 있으면
        # 메시지박스 출력 후 수정화면창으로 돌아감
        if len(B_MnameEntry.get()) == 0 or len(B_MPubEntry.get()) == 0 or len(B_MISBNEntry.get()) == 0 or len(
                B_MLinkEntry.get()) == 0 or len(B_MPriEntry.get()) == 0 or len(B_MWirEntry.get()) == 0 or len(
                B_MIntrscr.get("1.0", "end")) == 0:
                    messagebox.showerror("도서 관리 프로그램", "빈칸이 존재합니다.\n빈칸을 입력하세요.")

        # ISBN 중복 되면 (아직 구현 x)
        # 메시지박스 출력 후 수정화면창으로 돌아감

        # 대여중인 도서이면  (아직 구현 x)
        # 메시지박스 출력 후 수정화면창으로 돌아감

        # 수정을 묻는 메시지박스 출력 (예, 아니오)
        else:
            MobCheckBox = messagebox.askokcancel("도서 관리 프로그램", "도서를 수정하시겠습니까?")

            # '예'를 누를경우
            # csv파일 데이터 수정
            if MobCheckBox == 1:
                if B_MISBNEntry.get().isdigit() and B_MPriEntry.get().isdigit(): # 가격과 ISBN이 숫자인 경우
                    book_modify_p = book_Pandas.book_modify(B_MISBNEntry.get(),B_MnameEntry.get(), B_MWirEntry.get(), B_MPubEntry.get(), 
                                                            B_MPriEntry.get(), B_MLinkEntry.get(), B_MIntrscr.get("1.0", "end"))
                    if book_modify_p == True:
                        # 수정되었다는 메시지박스 출력 (확인)
                        messagebox.showinfo("도서 관리 프로그램", "수정되었습니다.")
                        # 엔트리와 텍스트의 내용을 비움
                        B_MnameEntry.delete(0, "end")
                        B_MPubEntry.delete(0, "end")
                        B_MISBNEntry.delete(0, "end")
                        B_MLinkEntry.delete(0, "end")
                        B_MWirEntry.delete(0, "end")
                        B_MPriEntry.delete(0, "end")
                        B_MIntrscr.delete("1.0", "end")
                    else:
                        messagebox.showerror("도서 관리 프로그램", "등록되지 않은 도서입니다.")
                else:
                    messagebox.showerror("도서 관리 프로그램", "ISBN과 가격은 숫자를 입력해주세요.")
                
            # '아니오'를 누를경우
            # 수정화면창으로 돌아감 (내용을 비우지 않음)
            else:
                messagebox.showinfo("도서 관리 프로그램", "수정이 취소 되었습니다.")


    book_Pandas = Panda('Book_list.csv', 'user_list.csv','Book_rent.csv')
    
    ISBN_serch = Toplevel(main)
    ISBN_serch.geometry("350x120")

    # ISBN 입력 창 레이블
    ShrLabel = Label(ISBN_serch)
    ShrLabel.pack(padx=24)
    P_ShrLabel = Label(ISBN_serch, text="ISBN")
    P_ShrLabel.pack(side=LEFT, padx=22)

    # ISBN 입력 창 엔트리
    P_ShrEntry = Entry(ISBN_serch, width=20)
    P_ShrEntry.pack(side=LEFT)

    # ISBN 입력 창 버튼
    P_ShrButton = Button(ISBN_serch, text="입력", width=8, command=ISBN_input)
    P_ShrButton.pack(side=LEFT)
    
    frame = Frame(main)
    
    # '도서 정보 수정' 레이블 생성 글자크기 설정
    # '도서 정보 수정' 레이블을 main에 부착
    B_ModLabel = Label(frame, text ="도서 정보 수정", font=(None,12))
    B_ModLabel.grid(row=1,column=1,pady=10)

    BMod_frame_1 = Frame(frame)
    BMod_frame_1.grid(row=2,column=1)

    # '도서명' 레이블 생성
    # '도서명' 레이블을 main에 부착
    B_MnameLabel = Label(BMod_frame_1, text="도서명")
    B_MnameLabel.grid(row=1,column=1,padx=10 ,pady=10)

    # '도서명' 엔트리(텍스트박스) 생성
    # '도서명' 엔트리를 main에 부착
    B_MnameEntry = Entry(BMod_frame_1, width=50)
    B_MnameEntry.grid(row=1,column=2)

    # '출판사' 레이블 생성
    # '출판사' 레이블을 main에 부착
    B_MPubLabel = Label(BMod_frame_1, text ="출판사")
    B_MPubLabel.grid(row=2,column=1,pady=10)

    # '출판사' 엔트리(텍스트박스) 생성
    # '출판사' 엔트리를 main에 부착
    B_MPubEntry = Entry(BMod_frame_1, width=50)
    B_MPubEntry.grid(row=2,column=2)

    # 'ISBN' 레이블 생성
    # 'ISBN' 레이블을 main에 부착
    B_MISBNLabel = Label(BMod_frame_1, text ="ISBN")
    B_MISBNLabel.grid(row=3,column=1,pady=10)

    # 'ISBN' 엔트리(텍스트박스) 생성
    # 'ISBN' 엔트리를 main에 부착
    B_MISBNEntry = Entry(BMod_frame_1, width=50)
    B_MISBNEntry.grid(row=3,column=2)

    # '관련링크' 이블 생성
    # '관련링크' 레이블을 main에 부착
    B_MLinkLabel = Label(BMod_frame_1, text ="관련링크")
    B_MLinkLabel.grid(row=4,column=1,pady=10)

    # '관련링크' 엔트리(텍스트박스) 생성
    # '관련링크' 엔트리를 main에 부착
    B_MLinkEntry = Entry(BMod_frame_1, width=50)
    B_MLinkEntry.grid(row=4,column=2)

    # '저자' 레이블 생성
    # '저자' 레이블을 main에 부착
    B_MWirLabel = Label(BMod_frame_1, text ="저자")
    B_MWirLabel.grid(row=5,column=1,pady=10)

    BMod_frame_2 = Frame(BMod_frame_1)
    BMod_frame_2.grid(row=5,column=2)

    # '저자' 엔트리(텍스트박스) 생성
    # '저자' 엔트리를 main에 부착
    B_MWirEntry = Entry(BMod_frame_2, width=23)
    B_MWirEntry.grid(row=1,column=1)

    # '가격' 레이블 생성
    # '가격' 레이블을 main에 부착
    B_MPriLabel = Label(BMod_frame_2, text ="가격")
    B_MPriLabel.grid(row=1,column=2,padx=10)

    # '가격' 엔트리(텍스트박스) 생성
    # '가격' 엔트리를 main에 부착
    B_MPriEntry = Entry(BMod_frame_2, width=20)
    B_MPriEntry.grid(row=1,column=3)

    # '도서소개' 레이블 생성
    # '도서소개' 레이블을 main에 부착
    B_MIntrLabel = Label(frame, text ="도서소개")
    B_MIntrLabel.grid(row=3,column=1,pady=10)

    # '도서소개' 스크롤텍스트(ScrolledText) 생성
    # '도서소개' 스크롤텍스트(ScrolledText) main에 부착
    B_MIntrscr = scrolledtext.ScrolledText(frame, width=100, height=10, wrap=WORD)
    B_MIntrscr.grid(row=4,column=1)


    # '수정'버튼 생성 (command = modify)
    # 버튼을 main 부착
    B_MAppButton = Button(frame,text="수정", width=8, command=modify)
    B_MAppButton.grid(row=5,column=1,pady=30)

    return frame
