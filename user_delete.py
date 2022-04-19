from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# 삭제 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def delete():
    print('추가 버튼 클릭')
    #대여중인 회원이면
    if ():
            # messagebox.showinfo('도서 관리 프로그램 메시지', '대여 중인 회원입니다.') #메시지출력 후 삭제화면창으로 돌아감

    else:
        check_yn = messagebox.askokcancel('도서 관리 프로그램 메시지', '삭제하시겠습니까?') #삭제를 묻는 메시지박스 출력 (예, 아니오)
        if check_yn == 1: #'예'를 누를경우
            # csv파일에서 데이터 탈퇴로 설정 (아직 구현 x)
            messagebox.showinfo('알림', '삭제되었습니다.')  #삭제되었다는 메시지박스 출력 (확인)
            #메인창으로 이동
        else: #'아니오'를 누를경우
            messagebox.showinfo('알림', '삭제가 취소되었습니다.')
            #삭제화면창으로 돌아감

# 임시화면
main = Tk()
main.geometry("800x500")
main.title("도서 관리 프로그램")

# def user_delete(main) :    #도서수정(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

frame = Frame(main)
frame.pack()

label_append = Label(frame, text='회원탈퇴') # '회원탈퇴' 레이블 생성 글자크기 설정
label_append.grid(row=1, column=1, pady=50) # '회원탈퇴' 레이블을 main에 부착

text_frame = Frame(frame)
text_frame.grid(row=2, column=1)

label_name = Label(text_frame, text='이름', width=10)  # '이름' 레이블 생성
label_name.grid(row=2, column=1, pady=10) # '이름' 레이블을 main에 부착

entry_name = Entry(text_frame, width=30) # '이름' 엔트리(텍스트박스) 생성
entry_name.configure(state='disabled') # '이름' 엔트리를 읽기전용으로 상태설정
entry_name.grid(row=2, column=2) # '이름' 엔트리를 main에 부착

label_birth = Label(text_frame, text='생년월일', width=10) # '생년월일' 레이블 생성

label_birth.grid(row=3, column=1, pady=10) # '생년월일' 레이블을 main에 부착

entry_birth = Entry(text_frame, width=30) # '생년월일' 엔트리(텍스트박스) 생성
entry_birth.configure(state='disabled') # '생년월일' 엔트리를 읽기전용으로 상태설정
entry_birth.grid(row=3, column=2) # '생년월일' 엔트리를 main에 부착

sex_frame = Frame(text_frame)
sex_frame.grid(row=4, column=2)

radio_sex = IntVar() # 성별 라디오버튼 생성
Label(text_frame, text='성별', width=10).grid(row=4, column=1, pady=10)
radio_wo = Radiobutton(sex_frame, text='여자', value=1, variable=radio_sex)
radio_man = Radiobutton(sex_frame, text='남자', value=2, variable=radio_sex)
radio_wo.configure(state='disabled')
radio_man.configure(state='disabled')
radio_wo.grid(row=1, column=1)
radio_man.grid(row=1, column=2, padx=60)

num_frame = Frame(text_frame)
num_frame.grid(row=5, column=2)

label_num = Label(text_frame, text='전화번호', width=10) # '전화번호' 레이블 생성
label_num.grid(row=5, column=1, pady=10) # '전화번호' 레이블을 main에 부착

entry_num1 = Entry(num_frame, width=6) # '전화번호' 첫번째 엔트리(텍스트박스) 생성
entry_num1.configure(state='disabled') # '전화번호' 엔트리를 읽기전용으로 상태설정
entry_num1.grid(row=1, column=1) # '전화번호' 첫번째 엔트리를 main에 부착

label_num_ = Label(num_frame, text='-')
label_num_.grid(row=1, column=2, padx=3)

entry_num2 = Entry(num_frame, width=9) # '전화번호' 두번째 엔트리(텍스트박스) 생성
entry_num2.configure(state='disabled') # '전화번호' 엔트리를 읽기전용으로 상태설정
entry_num2.grid(row=1, column=3) # '전화번호' 두번째 엔트리를 main에 부착

label_num_ = Label(num_frame, text='-')
label_num_.grid(row=1, column=4, padx=3)

entry_num3 = Entry(num_frame, width=9) # '전화번호' 세번째 엔트리(텍스트박스) 생성
entry_num3.configure(state='disabled') # '전화번호' 엔트리를 읽기전용으로 상태설정
entry_num3.grid(row=1, column=5) # '전화번호' 세번째 엔트리를 main에 부착

label_mail = Label(text_frame, text='이메일', width=10) # '이메일' 레이블 생성
label_mail.grid(row=6, column=1, pady=10) # '이메일' 레이블을 main에 부착

entry_mail = Entry(text_frame, width=30) # '이메일' 엔트리(텍스트박스) 생성
entry_mail.configure(state='disabled') # '이메일' 엔트리를 읽기전용으로 상태설정
entry_mail.grid(row=6, column=2) # '이메일' 엔트리를 main에 부착


treeview = Treeview(frame, columns=['#1'], displaycolumns=['#1'], height=1)
treeview.grid(row=3, column=1, pady=40)

treeview.column('#0', width=170, anchor="center")
treeview.heading('#0', text='대출 목록', anchor="center")

treeview.column('#1', width=120, anchor="center")
treeview.heading('#1', text='반납 예정일', anchor="center")

us_plus = Button(frame, text='탈퇴', width=5, command=delete) # '탈퇴'버튼 생성 (command = delete)
us_plus.grid(row=4, column=1, pady=5)   # 버튼을 main 부착


main.mainloop()

