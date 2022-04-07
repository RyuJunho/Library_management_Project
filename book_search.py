from tkinter import *
from tkinter.ttk import *


# 검색 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def search():
    print('버튼클릭')
    # (아직 구현 x)


# 임시윈도우(나중에는 메인화면의 윈도우를 이용할거임)
main = Tk()
main.geometry("700x500")    #크기 적당히 조절

# def book_search(main) :    #도서검색(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

# '도서검색' 레이블 생성 글자크기 설정
# 레이블을 main윈도우에 부착
B_SrhLabel = Label(main, text="도서검색",font=(None, 14))
B_SrhLabel.pack(pady=30)

search_frame = Frame(main)  # 콤보박스, 엔트리, 버튼이 들어갈 프레임 생성

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
B_SrhButton = Button(search_frame, text="검색", width=8)
B_SrhButton.pack(side=LEFT,padx=10, pady=10)

# search_frame을 main윈도우에 부착
search_frame.pack()

# 트리뷰(표) 생성
# 표를 main에 부착
B_SrhTreeV = Treeview(main, columns=["one","two","three"])
B_SrhTreeV.pack(pady=10)

# 각 컬럼 설정
#'도서명'컬럼
B_SrhTreeV.column("#0", width=140)
B_SrhTreeV.heading("#0", text="도서명")
#'저자'컬럼
B_SrhTreeV.column("#1", width=120)
B_SrhTreeV.heading("one", text="저자")
#'ISBN'컬럼
B_SrhTreeV.column("#2", width=120)
B_SrhTreeV.heading("two", text="ISBN")
#'대출가능여부'컬럼
B_SrhTreeV.column("#3", width=120)
B_SrhTreeV.heading("three", text="대출가능여부")

# 표에 삽입될 데이터 (아직 구현 x)

# 표에 데이터 삽입 (아직 구현 x)


main.mainloop()

