from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

# 수정 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def modify():
    print('추가 버튼 클릭')
    #빈칸이 있으면
        #메시지박스 출력 후 수정화면창으로 돌아감

    #ISBN 중복 되면 (아직 구현 x)
        #메시지박스 출력 후 수정화면창으로 돌아감
    
    #대여중인 도서이면  (아직 구현 x)
        #메시지박스 출력 후 수정화면창으로 돌아감
        
    #수정을 묻는 메시지박스 출력 (예, 아니오)
    #'예'를 누를경우
        #csv파일 데이터 수정 (아직 구현 x)
        #수정되었다는 메시지박스 출력 (확인)
        #엔트리와 텍스트의 내용을 비움
    #'아니오'를 누를경우
        #수정화면창으로 돌아감 (내용을 비우지 않음)

# 임시화면
main = Tk()
main.geometry("800x500")

# def book_modify(main) :    #도서수정(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

# '도서 정보 수정' 레이블 생성 글자크기 설정
# '도서 정보 수정' 레이블을 main에 부착

# '도서명' 레이블 생성
# '도서명' 레이블을 main에 부착

# '도서명' 엔트리(텍스트박스) 생성
# '도서명' 엔트리를 main에 부착

# '출판사' 레이블 생성
# '출판사' 레이블을 main에 부착

# '출판사' 엔트리(텍스트박스) 생성
# '출판사' 엔트리를 main에 부착

# 'ISBN' 레이블 생성
# 'ISBN' 레이블을 main에 부착

# 'ISBN' 엔트리(텍스트박스) 생성
# 'ISBN' 엔트리를 main에 부착

# '관련링크' 이블 생성
# '관련링크' 레이블을 main에 부착

# '관련링크' 엔트리(텍스트박스) 생성
# '관련링크' 엔트리를 main에 부착

# '저자' 레이블 생성
# '저자' 레이블을 main에 부착

# '저자' 엔트리(텍스트박스) 생성
# '저자' 엔트리를 main에 부착

# '저자' 레이블 생성
# '저자' 레이블을 main에 부착

# '저자' 엔트리(텍스트박스) 생성
# '저자' 엔트리를 main에 부착

# '도서소개' 레이블 생성
# '도서소개' 레이블을 main에 부착

# '도서소개' 스크롤텍스트(ScrolledText) 생성
# '도서소개' 스크롤텍스트(ScrolledText) main에 부착


# '수정'버튼 생성 (command = modify)
# 버튼을 main 부착

main.mainloop()
