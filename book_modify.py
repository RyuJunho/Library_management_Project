from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

# 수정 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def modify():
    print('추가 버튼 클릭')
    #빈칸이 있으면
        #메시지박스 출력 후 수정화면창으로 돌아감
    if len(B_MnameEntry.get())==0 or len(B_MPubEntry.get())==0 or len(B_MISBNEntry.get())==0 or len(B_MLinkEntry.get())==0 or len(B_MPriEntry.get())==0 or len(B_MWirEntry.get())==0 or len(B_MIntrscr.get("1.0", "end-1c")) == 0:
        MobErBox = messagebox.showerror("미입력", "빈칸이 존재합니다.\n빈칸을 입력하세요.")
    
    #ISBN 중복 되면 (아직 구현 x)
        #메시지박스 출력 후 수정화면창으로 돌아감
    
    #대여중인 도서이면  (아직 구현 x)
        #메시지박스 출력 후 수정화면창으로 돌아감
        
    #수정을 묻는 메시지박스 출력 (예, 아니오)
    else:
        MobCheckBox = messagebox.askokcancel("도서수정", "도서를 수정하시겠습니까?")
      
    #'예'를 누를경우
        #csv파일 데이터 수정 (아직 구현 x)
        #수정되었다는 메시지박스 출력 (확인)
        #엔트리와 텍스트의 내용을 비움
        if MobCheckBox == 1:
            AppYesBox = messagebox.showinfo("수정완료", "수정되었습니다.")
            B_MnameEntry.delete(0,"end")
            B_MPubEntry.delete(0,"end")
            B_MISBNEntry.delete(0,"end")
            B_MLinkEntry.delete(0,"end")
            B_MWirEntry.delete(0,"end")
            B_MPriEntry.delete(0,"end")
            B_MIntrscr.delete("1.0", "end")
    #'아니오'를 누를경우
        #수정화면창으로 돌아감 (내용을 비우지 않음)
        else:
            ModNoBox = messagebox.showinfo("수정취소", "수정이 취소 되었습니다.")
    
# 임시화면
main = Tk()
main.geometry("800x500")

# def book_modify(main) :    #도서수정(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

# '도서 정보 수정' 레이블 생성 글자크기 설정
# '도서 정보 수정' 레이블을 main에 부착
B_ModLabel = Label(main, text ="도서 정보 수정", font=(None,12))
B_ModLabel.pack(side=TOP, ipadx=320, pady=20)

# '도서명' 레이블 생성
# '도서명' 레이블을 main에 부착
B_MnameLabel = Label(main, text="도서명")
B_MnameLabel.place(x = 180,y = 60)

# '도서명' 엔트리(텍스트박스) 생성
# '도서명' 엔트리를 main에 부착
B_MnameEntry = Entry(main, width=50)
B_MnameEntry.place(x = 240,y = 60)

# '출판사' 레이블 생성
# '출판사' 레이블을 main에 부착
B_MPubLabel = Label(main, text ="출판사")
B_MPubLabel.place(x = 180,y = 100)

# '출판사' 엔트리(텍스트박스) 생성
# '출판사' 엔트리를 main에 부착
B_MPubEntry = Entry(main, width=50)
B_MPubEntry.place(x = 240,y = 100)

# 'ISBN' 레이블 생성
# 'ISBN' 레이블을 main에 부착
B_MISBNLabel = Label(main, text ="ISBN")
B_MISBNLabel.place(x = 180,y = 140)

# 'ISBN' 엔트리(텍스트박스) 생성
# 'ISBN' 엔트리를 main에 부착
B_MISBNEntry = Entry(main, width=50)
B_MISBNEntry.place(x = 240,y = 140)

# '관련링크' 이블 생성
# '관련링크' 레이블을 main에 부착
B_MLinkLabel = Label(main, text ="관련링크")
B_MLinkLabel.place(x = 180,y = 180)

# '관련링크' 엔트리(텍스트박스) 생성
# '관련링크' 엔트리를 main에 부착
B_MLinkEntry = Entry(main, width=50)
B_MLinkEntry.place(x = 240,y = 180)

# '저자' 레이블 생성
# '저자' 레이블을 main에 부착
B_MWirLabel = Label(main, text ="저자")
B_MWirLabel.place(x = 180,y = 220)

# '저자' 엔트리(텍스트박스) 생성
# '저자' 엔트리를 main에 부착
B_MWirEntry = Entry(main, width=20)
B_MWirEntry.place(x = 240,y = 220)

# '저자' 레이블 생성
# '저자' 레이블을 main에 부착
B_MPriLabel = Label(main, text ="가격")
B_MPriLabel.place(x = 420,y = 220)

# '저자' 엔트리(텍스트박스) 생성
# '저자' 엔트리를 main에 부착
B_MPriEntry = Entry(main, width=16)
B_MPriEntry.place(x = 478,y = 220)

# '도서소개' 레이블 생성
# '도서소개' 레이블을 main에 부착
B_MIntrLabel = Label(main, text ="도서소개")
B_MIntrLabel.pack(side=LEFT, padx=40, pady=20)

# '도서소개' 스크롤텍스트(ScrolledText) 생성
# '도서소개' 스크롤텍스트(ScrolledText) main에 부착
B_MIntrscr = scrolledtext.ScrolledText(main, width=100, height=10, wrap=WORD)
B_MIntrscr.place(x = 40,y = 300)


# '수정'버튼 생성 (command = modify)
# 버튼을 main 부착
B_MAppButton = Button(main,text="수정", width=8, command=modify)
B_MAppButton.place(x = 320,y = 450)

B_MCancButton = Button(main,text="취소", width=8)
B_MCancButton.place(x = 420,y = 450)

main.mainloop()
