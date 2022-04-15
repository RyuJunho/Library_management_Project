from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

# 추가 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def append():
    print('추가 버튼 클릭')
    #빈칸이 있으면
        #메시지박스 출력 후 등록화면창으로 돌아감
    if len(B_nameEntry.get())==0 or len(B_PubEntry.get())==0 or len(B_ISBNEntry.get())==0 or len(B_LinkEntry.get())==0 or len(B_PriEntry.get())==0 or len(B_WirEntry.get())==0 or len(B_Intrscr.get("1.0", "end-1c")) == 0:
        AppErBox = messagebox.showerror("미입력", "빈칸이 존재합니다.\n빈칸을 입력하세요.")
    
    #ISBN 중복 되면 (아직 구현 x)
        #메시지박스 출력 후 등록화면창으로 돌아감

    #등록을 묻는 메시지박스 출력 (예, 아니오)
    else:
        AppCheckBox = messagebox.askokcancel("도서등록", "도서를 등록하시겠습니까?")
    #'예'를 누를경우
        #등록되었다는 메시지박스 출력 (확인)
        #엔트리와 텍스트의 내용을 비움
        if AppCheckBox == 1:
            AppYesBox = messagebox.showinfo("등록완료", "등록되었습니다.")
            B_nameEntry.delete(0,"end")
            B_PubEntry.delete(0,"end")
            B_ISBNEntry.delete(0,"end")
            B_LinkEntry.delete(0,"end")
            B_WirEntry.delete(0,"end")
            B_PriEntry.delete(0,"end")
            B_Intrscr.delete("1.0", "end")
        #'아니오'를 누를경우
            #등록화면창으로 돌아감 (내용을 비우지 않음)
        else:
            AppNoBox = messagebox.showinfo("등록취소", "등록이 취소 되었습니다.")


# 임시화면
main = Tk()
main.geometry("800x500")
# def book_append(main) :    #도서등록(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

# '도서등록' 레이블 생성 글자크기 설정
# '도서등록' 레이블을 main에 부착
B_ApeLabel = Label(main, text ="도서등록", font=(None,12))
B_ApeLabel.pack(side=TOP, ipadx=320, pady=20)

# '도서명' 레이블 생성
# '도서명' 레이블을 main에 부착
B_nameLabel = Label(main, text="도서명")
B_nameLabel.place(x = 180,y = 60)

# '도서명' 엔트리(텍스트박스) 생성
# '도서명' 엔트리를 main에 부착
B_nameEntry = Entry(main, width=50)
B_nameEntry.place(x = 240,y = 60)

# '출판사' 레이블 생성
# '출판사' 레이블을 main에 부착
B_PubLabel = Label(main, text ="출판사")
B_PubLabel.place(x = 180,y = 100)

# '출판사' 엔트리(텍스트박스) 생성
# '출판사' 엔트리를 main에 부착
B_PubEntry = Entry(main, width=50)
B_PubEntry.place(x = 240,y = 100)

# 'ISBN' 레이블 생성
# 'ISBN' 레이블을 main에 부착
B_ISBNLabel = Label(main, text ="ISBN")
B_ISBNLabel.place(x = 180,y = 140)

# 'ISBN' 엔트리(텍스트박스) 생성
# 'ISBN' 엔트리를 main에 부착
B_ISBNEntry = Entry(main, width=50)
B_ISBNEntry.place(x = 240,y = 140)

# '관련링크' 이블 생성
# '관련링크' 레이블을 main에 부착
B_LinkLabel = Label(main, text ="관련링크")
B_LinkLabel.place(x = 180,y = 180)

# '관련링크' 엔트리(텍스트박스) 생성
# '관련링크' 엔트리를 main에 부착
B_LinkEntry = Entry(main, width=50)
B_LinkEntry.place(x = 240,y = 180)

# '저자' 레이블 생성
# '저자' 레이블을 main에 부착
B_WirLabel = Label(main, text ="저자")
B_WirLabel.place(x = 180,y = 220)

# '저자' 엔트리(텍스트박스) 생성
# '저자' 엔트리를 main에 부착
B_WirEntry = Entry(main, width=20)
B_WirEntry.place(x = 240,y = 220)

# '가격' 레이블 생성
# '가격' 레이블을 main에 부착
B_PriLabel = Label(main, text ="가격")
B_PriLabel.place(x = 420,y = 220)

# '가격' 엔트리(텍스트박스) 생성
# '가격' 엔트리를 main에 부착
B_PriEntry = Entry(main, width=16)
B_PriEntry.place(x = 478,y = 220)

# '도서소개' 레이블 생성
# '도서소개' 레이블을 main에 부착
B_IntrLabel = Label(main, text ="도서소개")
B_IntrLabel.pack(side=LEFT, padx=40, pady=20)

# '도서소개' 스크롤텍스트(ScrolledText) 생성
# '도서소개' 스크롤텍스트(ScrolledText) main에 부착
B_Intrscr = scrolledtext.ScrolledText(main, width=100, height=10, wrap=WORD)
B_Intrscr.place(x = 40,y = 300)

# '추가'버튼 생성 (command = append)
# 버튼을 main 부착
B_AppButton = Button(main,text="추가", width=8, command=append)
B_AppButton.place(x = 320,y = 450)

B_CancButton = Button(main,text="취소", width=8)
B_CancButton.place(x = 420,y = 450)

main.mainloop()
