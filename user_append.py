from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox



def user_append(main):    #회원등록(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

    # 추가 버튼을 클릭했을 때 호출되는 이벤트 핸들러
    def append():
        print('추가 버튼 클릭')
        # 빈칸이 있으면
        if len(entry_name.get()) == 0 or len(entry_birth.get()) == 0 or len(entry_num1.get()) == 0 or len(
                entry_num2.get()) == 0 or len(entry_num3.get()) == 0 or len(entry_mail.get()) == 0:
            messagebox.showinfo('도서 관리 프로그램 메시지', '빈칸이 존재합니다.')  # 메시지박스 출력 후 등록화면창으로 돌아감

        # elif (): # 전화번호가 중복 되면 (아직 구현 x)
        # messagebox.showinfo("도서 관리 프로그램 메시지", "중복된 전화번호입니다.") # 메시지박스 출력 후 등록화면창으로 돌아감

        else:
            check_yn = messagebox.askokcancel('도서 관리 프로그램 메시지', '회원을 등록하시겠습니까?')  # 등록을 묻는 메시지박스 출력 (예, 아니오)
            if check_yn == 1:  # '예'를 누를경우
                messagebox.showinfo('알림', '등록되었습니다.')  # 등록되었다는 메시지박스 출력 (확인)
                # 엔트리와 텍스트의 내용을 비움
                entry_name.delete(0, 'end')
                entry_birth.delete(0, 'end')
                entry_num1.delete(0, 'end')
                entry_num2.delete(0, 'end')
                entry_num3.delete(0, 'end')
                entry_mail.delete(0, 'end')

            else:  # '아니오'를 누를경우
                messagebox.showinfo('알림', '등록이 취소되었습니다.')  # 메시지 박스를 뜨운 후 등록화면창으로 돌아감 (내용을 비우지 않음)


    frame = Frame(main)


    label_append = Label(frame, text='회원등록') # '회원등록' 레이블 생성 글자크기 설정
    label_append.grid(row=1, column=1, pady=50)

    text_frame = Frame(frame)
    text_frame.grid(row=2, column=1)

    label_name = Label(text_frame, text='이름', width=10) # '이름' 레이블 생성
    label_name.grid(row=2, column=1, pady=10)

    entry_name = Entry(text_frame, width=30) # '이름' 엔트리(텍스트박스) 생성
    entry_name.grid(row=2, column=2)


    label_birth = Label(text_frame, text='생년월일', width=10) # '생년월일' 레이블 생성
    label_birth.grid(row=3, column=1, pady=10)

    entry_birth = Entry(text_frame, width=30) # '생년월일' 엔트리(텍스트박스) 생성
    entry_birth.grid(row=3, column=2)


    sex_frame = Frame(text_frame)
    sex_frame.grid(row=4, column=2)

    radio_sex = IntVar() # 성별 라디오버튼 생성
    Label(text_frame, text='성별', width=10).grid(row=4, column=1, pady=10)
    radio_wo = Radiobutton(sex_frame, text='여자', value=1, variable=radio_sex)
    radio_man = Radiobutton(sex_frame, text='남자', value=2, variable=radio_sex)
    radio_wo.grid(row=1, column=1)
    radio_man.grid(row=1, column=2, padx=60)


    num_frame = Frame(text_frame)
    num_frame.grid(row=5, column=2)

    label_num = Label(text_frame, text='전화번호', width=10) # '전화번호' 레이블 생성
    label_num.grid(row=5, column=1, pady=10)

    entry_num1 = Entry(num_frame, width=6) # '전화번호' 첫번째 엔트리(텍스트박스) 생성
    entry_num1.grid(row=1, column=1) # '전화번호' 첫번째 엔트리를 main에 부착

    label_num_ = Label(num_frame, text='-')
    label_num_.grid(row=1, column=2, padx=3)

    entry_num2 = Entry(num_frame, width=9) # '전화번호' 두번째 엔트리(텍스트박스) 생성
    entry_num2.grid(row=1, column=3) # '전화번호' 두번째 엔트리를 main에 부착

    label_num_ = Label(num_frame, text='-')
    label_num_.grid(row=1, column=4, padx=3)

    entry_num3 = Entry(num_frame, width=9) # '전화번호' 세번째 엔트리(텍스트박스) 생성
    entry_num3.grid(row=1, column=5) # '전화번호' 세번째 엔트리를 main에 부착


    label_mail = Label(text_frame, text='이메일', width=10)# '이메일' 레이블 생성
    label_mail.grid(row=6, column=1, pady=10) # '이메일' 레이블을 main에 부착

    entry_mail = Entry(text_frame, width=30) # '이메일' 엔트리(텍스트박스) 생성
    entry_mail.grid(row=6, column=2) # '이메일' 엔트리를 main에 부착


    us_plus = Button(frame, text='추가', width=5, command=append) # '추가'버튼 생성 (command = append)
    us_plus.grid(row=3, column=1, pady=80)  # 버튼을 main 부착


    return frame
