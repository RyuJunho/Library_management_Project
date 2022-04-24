from tkinter import *
from tkinter.ttk import *
from book_Pandas_Class import*

def book_search(main) :    #도서검색(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

    # 버튼 클릭 시 트리뷰 데이터 초기화
    def re(Treeview):
        for row in Treeview.get_children():
            Treeview.delete(row)
            
    # 검색 버튼을 클릭했을 때 호출되는 이벤트 핸들러
    def search():
        srh_np = book_Pandas.book_search(B_SrhBox.get(), B_SrhEntry.get()) 
        re(B_SrhTreeV)
        for i in srh_np.tolist():
            B_SrhTreeV.insert('', 'end', text=i, values=i)
        
    frame = Frame(main)

    book_Pandas = Panda('Book_list.csv', 'user_list.csv','Book_rent.csv')
        
    # '도서검색' 레이블 생성 글자크기 설정
    # 레이블을 main윈도우에 부착
    B_SrhLabel = Label(frame, text="도서검색",font=(None, 14))
    B_SrhLabel.pack(pady=30)

    search_frame = Frame(frame)  # 콤보박스, 엔트리, 버튼이 들어갈 프레임 생성

    # 콤보박스 생성(제목,저자) (읽기전용으로 설정)
    # 콤보박스 초기값을 '제목'으로 설정
    # 콤보박스를 search_frame에 부착
    B_SrhBox = Combobox(search_frame, width=6, values=["제목", "저자"])
    B_SrhBox.current(0)
    B_SrhBox.pack(side=LEFT, padx=10, pady=10)

    # 엔트리(텍스트박스) 생성
    # 엔트리를 search_frame에 부착
    B_SrhEntry = Entry(search_frame, width=40)
    B_SrhEntry.pack(side=LEFT, pady=10)

    # '검색'버튼 생성
    # 버튼을 search_frame에 부착
    B_SrhButton = Button(search_frame, text="검색", width=8, command=search)
    B_SrhButton.pack(side=LEFT,padx=10, pady=10)

    # search_frame을 main윈도우에 부착
    search_frame.pack()

    # 트리뷰(표) 생성
    # 표를 main에 부착
    Search_columns = ('B_name', 'writer', 'ISBN', 'RentPossi')
    B_SrhTreeV = Treeview(frame, columns=Search_columns, show='headings')
    B_SrhTreeV.pack(pady=10)
    
    # 각 컬럼 설정
    #'도서명'컬럼
    B_SrhTreeV.column("B_name", width=140)
    B_SrhTreeV.heading("B_name", text="도서명", anchor="center")
    #'저자'컬럼
    B_SrhTreeV.column("writer", width=120)
    B_SrhTreeV.heading("writer", text="저자", anchor="center")
    #'ISBN'컬럼
    B_SrhTreeV.column("ISBN", width=120)
    B_SrhTreeV.heading("ISBN", text="ISBN", anchor="center")
    #'대출가능여부'컬럼
    B_SrhTreeV.column("RentPossi", width=120)
    B_SrhTreeV.heading("RentPossi", text="대출가능여부", anchor="center")

    # 표에 삽입될 데이터 (아직 구현 x)

    # 표에 데이터 삽입 (아직 구현 x)

    return frame

