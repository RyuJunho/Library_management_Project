from tkinter import *

#1주차 회의록을 참조하여 설계 할 것
#GUI 메인화면을 이 파일에서 설계
#이벤트 처리기 기능은 구현은 하지말고 주석으로 설명 달아놓을 것

# 이벤트 핸들러 ##################################################################################
def book_search():  #도서검색 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('도서검색 메뉴')

def book_signup():  #도서등록 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('도서등록 메뉴')

def book_correct():  #도서수정 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('도서수정 메뉴')

def book_drop():  #도서삭제 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('도서삭제 메뉴')


def user_search():  #회원검색 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('회원검색 메뉴')

def user_signup():  #회원등록 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('회원등록 메뉴')

def user_correct():  #회원수정 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('회원수정 메뉴')

def user_drop():  #회원탈퇴 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('회원탈퇴 메뉴')


def checkout_():  #대출하기 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('대출하기 메뉴')

def return_():  #반납하기 메뉴를 클릭하였을 때 호출될 이벤트 핸들러
    print('반납하기 메뉴')

# 이벤트 핸들러 -끝- ##############################################################################

main = Tk() #메인창 생성
main.title('도서 관리 프로그램') #메인창 타이틀 설정
sw = main.winfo_screenwidth()
sh = main.winfo_screenheight()
width = 1000
height = 600
x = (sw/2) - (width/2)
y = (sh/2) - (height/2)
main.geometry('%dx%d+%d+%d' % (width, height, x, y)) #메인창 크기 고정, 중앙에 출력되도록 설정


# 메뉴 ############################################################################################
menubar = Menu(main) #메뉴바 생성

book_menu = Menu(menubar, tearoff=0) #도서관리(상위메뉴) 생성
menubar.add_cascade(label='도서관리', menu=book_menu)
book_menu.add_command(label='도서검색', command=book_search()) #도서검색(하위메뉴) 생성  (각 하위메뉴 사이에는 구분선을 추가 할 것)
book_menu.add_command(label='도서등록', command=book_signup()) #도서등록(하위메뉴) 생성
book_menu.add_separator()
book_menu.add_command(label='도서수정', command=book_correct()) #도서수정(하위메뉴) 생성
book_menu.add_command(label='도서삭제', command=book_drop()) #도서삭제(하위메뉴) 생성

user_menu = Menu(menubar, tearoff=0) #회원관리(상위메뉴) 생성
menubar.add_cascade(label='회원관리', menu=user_menu)
user_menu.add_command(label='회원검색', command=user_search()) #회원검색(하위메뉴) 생성
user_menu.add_command(label='회원등록', command=user_signup()) #회원등록(하위메뉴) 생성
user_menu.add_separator()
user_menu.add_command(label='회원수정', command=user_correct()) #회원수정(하위메뉴) 생성
user_menu.add_command(label='회원탈퇴', command=user_drop()) #회원탈퇴(하위메뉴) 생성

checkout_menu = Menu(menubar, tearoff=0) #대출/반납(상위메뉴) 생성
menubar.add_cascade(label='대출/반납', menu=checkout_menu)
checkout_menu.add_command(label='대출하기', command=(checkout_())) #대출하기(하위메뉴) 생성
checkout_menu.add_command(label='반납하기', command=(return_()))#반납하기(하위메뉴) 생성

main.config(menu=menubar)   #메뉴바 부착

# 메뉴 -끝- #########################################################################################

main.mainloop() #실행

