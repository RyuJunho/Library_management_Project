from tkinter import *       
from tkinter.ttk import *
from user_Pandas_Class import*


def user_search(main) : #회원검색(매개변수 = 초기화면)

    def search(): # 검색 버튼을 클릭했을 때 호출되는 이벤트 핸들러
        user_pi = Main('user_list.csv', 'Book_rent.csv')
        us_list = user_pi.user_search(combox.get(), input_tx.get()) # 콤보박스, 엔트리 받아와서 저장
        for e in user_view.get_children():
            user_view.delete(e)
        for i in us_list.tolist():
            user_view.insert('', 'end', text=i, values=i)

    frame = Frame(main)

    label_user = Label(frame, text="회원검색") #'회원검색' 레이블 생성 글자크기 설정
    label_user.pack(pady=50) #세로 간격 설정 (유동적으로 설정할것)

    search_frame = Frame(frame) # 콤보박스, 엔트리, 버튼이 들어갈 프레임 생성

    combox = Combobox(search_frame, height=2, width=8, values=['이름', '전화번호']) #콤보박스 생성(이름,전화번호) (읽기전용으로 설정)
    combox.set('이름') #콤보박스 초기값을 '이름'으로 설정
    combox.grid(row=1, column=0, columnspan=2) #콤보박스를 search_frame에 부착

    input_tx = Entry(search_frame, width=20) #엔트리(텍스트박스) 생성
    input_tx.grid(row=1, column=2) #엔트리를 search_frame에 부착
    input_tx.focus()  # 키보드 입력 초점

    us_bt = Button(search_frame, text='검색', width=5, command=search) #'검색'버튼 생성
    us_bt.grid(row=1, column=3) #버튼을 search_frame에 부착

    search_frame.pack()

    user_view = Treeview(frame, columns=["name", "num", "sex", "del"], displaycolumns=["name", "num", "sex", "del"], show='headings') #트리뷰(표) 생성
    user_view.pack(pady=20) #표를 main에 부착


    #각 컬럼 설정
    user_view.column("name", width=80, anchor="center") #이름 컬럼
    user_view.heading("name", text="이름")

    user_view.column("num", width=200, anchor="center") #전화번호 컬럼
    user_view.heading("num", text="전화번호")

    user_view.column("sex", width=80, anchor="center") #성별 컬럼
    user_view.heading("sex", text="성별")

    user_view.column("del", width=80, anchor="center") #탈퇴여부 컬림
    user_view.heading("del", text="탈퇴여부")


    #표에 삽입될 데이터 (아직 구현 x)

    #표에 데이터 삽입 (아직 구현 x)


    return frame
