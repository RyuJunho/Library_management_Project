from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from book_Pandas_Class import*

def book_return(main) :

    # 전화번호로 회원을 확인
    def Phone_input():
        if len(P_ShrEntry.get()) == 13: #전화번호 형식인지 확인
            try :
                user_data_list = book_Pandas.user_check(P_ShrEntry.get())[0].tolist()   #전화번호로 회원데이터 추출
            except :
                messagebox.showerror("도서 관리 프로그램", "존재하지 않는 회원입니다.")
                return False

            PhoneCheckBox = messagebox.askokcancel("도서 관리 프로그램", user_data_list[1]+"님이 맞으십니까?")
            if PhoneCheckBox == 1:
                rent_insert(user_data_list[0])

        else:
            messagebox.showerror("도서 관리 프로그램", "형식에 맞게 입력해주세요.")
        
    # 트리뷰 클릭 이벤트(트리뷰 데이터 삭제)
    def Return_tree_click(event):
        selected_item = Return_tree.focus() # 트리뷰 선택
        getValue = Return_tree.item(selected_item, 'values')
        
        if (selected_item != ""): # 선택한 트리뷰가 있을 경우
            ReCheckBox = messagebox.askokcancel("도서 관리 프로그램", "반납하시겠습니까?")
            if ReCheckBox == 1:
                messagebox.showinfo("도서 관리 프로그램", "반납되었습니다.")
                if (selected_item != ""):
                    book_Pandas.book_return(P_ShrEntry.get(), getValue[2])
                    Return_tree.delete(selected_item) # 선택한 트리뷰 데이터 삭제
                
    def rent_insert(phone_number):
        return_np = book_Pandas.return_data(phone_number)
        try :
            if not return_np.tolist() :
                messagebox.showinfo("도서 관리 프로그램", "대여한 도서가 없습니다.")
                return False

            for i in return_np.tolist():
                Return_tree.insert('', 'end', text=i, values=i)
        except :
            messagebox.showinfo("도서 관리 프로그램", "대여한 도서가 없습니다.")
            
    
    book_Pandas = Panda('Book_list.csv', 'user_list.csv','Book_rent.csv')
    
    phone_serch = Toplevel(main)
    phone_serch.geometry("360x120")

    # 전화번호 입력 창 레이블
    P_ShrLabel = Label(phone_serch, text ="전화번호")
    P_ShrLabel.pack(side=LEFT, padx=20)

    # 전화번호 입력 창 엔트리
    P_ShrEntry = Entry(phone_serch, width=20)
    P_ShrEntry.pack(side=LEFT)

    # 전화번호 입력 창 버튼
    P_ShrButton = Button(phone_serch,text="입력", width=8, command=Phone_input)
    P_ShrButton.pack(side=LEFT)

    frame = Frame(main)

    # '반납' 레이블 생성 글자크기 설정
    # 레이블을 main윈도우에 부착
    Rent_Label = Label(frame, text="반납",font=(None, 14))
    Rent_Label.pack(anchor=CENTER, pady=20)

    # 트리뷰 컬럼 설정
    Return_columns = ('B_name', 'writer', 'ISBN', 'returnday')
    Return_tree = Treeview(frame, columns=Return_columns, show='headings')
    Return_tree.pack(pady=10)

    # 각 컬럼 설정
    #'도서명'컬럼
    Return_tree.column("B_name", width=140)
    Return_tree.heading("B_name", text="도서명")
    #'저자'컬럼
    Return_tree.column("writer", width=120)
    Return_tree.heading("writer", text="저자")
    #'ISBN'컬럼
    Return_tree.column("ISBN", width=120)
    Return_tree.heading("ISBN", text="ISBN")
    #'반납예정일'컬럼
    Return_tree.column("returnday", width=120)
    Return_tree.heading("returnday", text="반납예정일")

    # 트리뷰 이벤트 처리
    Return_tree.bind("<<TreeviewSelect>>", Return_tree_click)

    return frame