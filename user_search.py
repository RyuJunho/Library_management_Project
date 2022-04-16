from tkinter import *       
from tkinter.ttk import *


#검색 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def search():
    print('버튼클릭')
    #(아직 구현 x)


#임시화면
main = Tk()
main.title('도서 관리 프로그램') #메인창 타이틀 설정
main.geometry("800x500")


#def user_search(main) :    #회원검색(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임
def user_search(main):
    return main


label_user = Label(main, text="회원검색") #'회원검색' 레이블 생성 글자크기 설정
label_user.pack(pady=20) #세로 간격 설정 (유동적으로 설정할것)

search_frame = Frame(main)  #콤보박스, 엔트리, 버튼이 들어갈 프레임 생성

combox = Combobox(search_frame, height=2, width=4, values=['이름', '전화번호']) #콤보박스 생성(이름,전화번호) (읽기전용으로 설정)
combox.set('이름') #콤보박스 초기값을 '이름'으로 설정
combox.grid(row=1, column=0, columnspan=2) #콤보박스를 search_frame에 부착

input_tx = Entry(search_frame, width=20) #엔트리(텍스트박스) 생성
input_tx.grid(row=1, column=2) #엔트리를 search_frame에 부착

us_bt = Button(search_frame, text='검색', width=5) #'검색'버튼 생성
us_bt.grid(row=1, column=3) #버튼을 search_frame에 부착


search_frame.pack() #search_frame을 main윈도우에 부착

user_view = Treeview(main, columns=["#1", "#2", "#3"], displaycolumns=["#1", "#2", "#3"]) #트리뷰(표) 생성
user_view.pack(pady=50) #표를 main에 부착


#각 컬럼 설정
user_view.column("#0", width=80) #이름 컬럼
user_view.heading("#0", text="이름")

user_view.column("#1", width=200, anchor="center") #전화번호 컬럼
user_view.heading("#1", text="전화번호", anchor="center")

user_view.column("#2", width=80, anchor="center") #성별 컬럼
user_view.heading("#2", text="성별", anchor="center")

user_view.column("#3", width=80, anchor="center") #탈퇴여부 컬림
user_view.heading("#3", text="탈퇴여부", anchor="center")


#표에 삽입될 데이터 (아직 구현 x)

#표에 데이터 삽입 (아직 구현 x)


main.mainloop()
