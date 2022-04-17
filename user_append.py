from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


# 추가 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def append():
    print('추가 버튼 클릭')
    # 빈칸이 있으면
    if len(entry_name.get()) == 0 or len(entry_birth.get()) == 0 or len(entry_num1.get()) == 0 or len(entry_num2.get()) == 0 or len(entry_num3.get()) == 0 or len(entry_mail.get()) == 0:
        messagebox.showinfo('도서 관리 프로그램 메시지', '빈칸이 존재합니다.') # 메시지박스 출력 후 등록화면창으로 돌아감

    # elif (): # 전화번호가 중복 되면 (아직 구현 x)
        # messagebox.showinfo("도서 관리 프로그램 메시지", "중복된 전화번호입니다.") # 메시지박스 출력 후 등록화면창으로 돌아감

    else:
        check_yn = messagebox.askokcancel('도서 관리 프로그램 메시지', '회원을 등록하시겠습니까?') # 등록을 묻는 메시지박스 출력 (예, 아니오)
        if check_yn == 1: # '예'를 누를경우
            messagebox.showinfo('알림', '등록되었습니다.') # 등록되었다는 메시지박스 출력 (확인)
            # 엔트리와 텍스트의 내용을 비움
            entry_name.delete(0, 'end')
            entry_birth.delete(0, 'end')
            entry_num1.delete(0, 'end')
            entry_num2.delete(0, 'end')
            entry_num3.delete(0, 'end')
            entry_mail.delete(0, 'end')

        else: # '아니오'를 누를경우
            messagebox.showinfo('알림', '등록이 취소되었습니다.') # 메시지 박스를 뜨운 후 등록화면창으로 돌아감 (내용을 비우지 않음)


# 임시화면
main = Tk()
main.geometry("800x500")
main.title("도서 관리 프로그램")


#def user_append(main):    #회원등록(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임
def user_append(main):
    return main


label_append = Label(main, text='회원등록') # '회원등록' 레이블 생성 글자크기 설정
label_append.place(x=380, y=40) # '회원등록' 레이블을 main에 부착

label_name = Label(main, text='이름', width=10) # '이름' 레이블 생성
label_name.place(x=250, y=100) # '이름' 레이블을 main에 부착

entry_name = Entry(main, width=30) # '이름' 엔트리(텍스트박스) 생성
entry_name.place(x=310, y=100) # '이름' 엔트리를 main에 부착

label_birth = Label(main, text='생년월일', width=10) # '생년월일' 레이블 생성
label_birth.place(x=250, y=140) # '생년월일' 레이블을 main에 부착

entry_birth = Entry(main, width=30) # '생년월일' 엔트리(텍스트박스) 생성
entry_birth.place(x=310, y=140) # '생년월일' 엔트리를 main에 부착

radio_sex = IntVar() # 성별 라디오버튼 생성
Label(main, text='성별', width=10).place(x=250, y=180)
radio_wo = Radiobutton(main, text='여자', value=1, variable=radio_sex)
radio_man = Radiobutton(main, text='남자', value=2, variable=radio_sex)
radio_wo.place(x=310, y=180) # 성별 라디오버튼 부착
radio_man.place(x=380, y=180)

label_num = Label(main, text='전화번호', width=10) # '전화번호' 레이블 생성
label_num.place(x=250, y=220) # '전화번호' 레이블을 main에 부착

entry_num1 = Entry(main, width=7) # '전화번호' 첫번째 엔트리(텍스트박스) 생성
entry_num1.place(x=310, y=220) # '전화번호' 첫번째 엔트리를 main에 부착

label_num_ = Label(main, text='-')
label_num_.place(x=370, y=220)

entry_num2 = Entry(main, width=8) # '전화번호' 두번째 엔트리(텍스트박스) 생성
entry_num2.place(x=385, y=220) # '전화번호' 두번째 엔트리를 main에 부착

label_num_ = Label(main, text='-')
label_num_.place(x=450, y=220)

entry_num3 = Entry(main, width=8) # '전화번호' 세번째 엔트리(텍스트박스) 생성
entry_num3.place(x=465, y=220) # '전화번호' 세번째 엔트리를 main에 부착


label_mail = Label(main, text='이메일', width=10)# '이메일' 레이블 생성
label_mail.place(x=250, y=260) # '이메일' 레이블을 main에 부착

entry_mail = Entry(main, width=30) # '이메일' 엔트리(텍스트박스) 생성
entry_mail.place(x=310, y=260) # '이메일' 엔트리를 main에 부착


us_plus = Button(main, text='추가', width=5, command=append) # '추가'버튼 생성 (command = append)
us_plus.place(x=350, y=350)  # 버튼을 main 부착

us_del = Button(main, text='취소', width=5) # '추가'버튼 생성 (command = append)
us_del.place(x=430, y=350)  # 버튼을 main 부착

main.mainloop()

