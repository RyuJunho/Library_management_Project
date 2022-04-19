from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def book_return(main) :

    # 전화번호로 회원을 확인
    def Phone_input():
        print("전화번호 입력")
        if P_ShrEntry.get() == "1": # 전화번호가 동일한지(임시데이터)
            PhoneCheckBox = messagebox.askokcancel("본인확인", "'김길동'님이 맞으십니까?")
            if PhoneCheckBox == 1:
                phone_serch.destroy() # 확인을 누르면 창 닫기
        else:
            PhoneErBox = messagebox.showerror("확인불가", "존재하지 않는 회원입니다.")


    # 트리뷰 클릭 이벤트(트리뷰 데이터 삭제)
    def Return_tree_click(event):
        selected_item = Return_tree.focus() # 트리뷰 선택
        getValue = Return_tree.item(selected_item, 'values')
        if (selected_item != ""): # 선택한 트리뷰가 있을 경우
            ReCheckBox = messagebox.askokcancel("도서반납", "반납하시겠습니까?")
            if ReCheckBox == 1:
                ReYesBox = messagebox.showinfo("반납완료", "반납되었습니다.")
                if (selected_item != ""):
                    Return_tree.delete(selected_item) # 선택한 트리뷰 데이터 삭제


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

    # 표에 삽입될 데이터 (아직 구현 x)
    Return_treelist=[(1, "Tom", 80, "2022-04-18"), (1, "Bani", 71, "2022-04-18"), (1, "Boni", 90, "2022-04-18"), (1, "Dannel", 78, "2022-04-18"), (1, "Minho", 93, "2022-04-18")]
    # 표에 데이터 삽입 (아직 구현 x)
    for i in range(len(Return_treelist)):
        Return_tree.insert('', 'end', text="", values=Return_treelist[i], iid=i)

    # 트리뷰 이벤트 처리
    Return_tree.bind("<<TreeviewSelect>>", Return_tree_click)

    return frame