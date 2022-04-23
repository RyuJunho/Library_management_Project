import pandas as pd
import numpy as np
from datetime import datetime, timedelta



class Panda:
    def __init__(self, book, user, rent):  # 클래스 시작 항상 실행, 객체 생성 시 자동 호출
        self.Book_df = pd.read_csv(book).sort_values(by=['제목'],axis=0)  # 데이터 프레임을 공유하기 위해 self로 데이터 프레임 생성
        self.User_df = pd.read_csv(user).sort_values(by=['이름'], axis=0)  # 회원 존재 여부를 확인하기 위한 데이터 프레임 생성
        self.user_rent_df = pd.read_csv(rent).sort_values(by=['제목'], axis=0)  # 대출관리 초기 데이터를 데이터 프레임으로 생성
        
    def book_search(self, combo, data_search):  # 도서 검색
        if combo == "제목":  # 콤보 박스를 제목으로 선택했을 때
            self.T_search_np = np.array(self.Book_df.loc[self.Book_df['제목'].str.contains(data_search), ['제목', '저자', 'ISBN', '대여여부']])  # 제목 데이터가 일부분이라도 포함되어 있으면 제목, 저자, ISBN, 대여여부 순으로 출력
            print("제목")
            return self.T_search_np
        elif combo == "저자":  # 콤보 박스를 저자로 선택했을 때
            self.A_search_np = np.array(self.Book_df.loc[self.Book_df['저자'].str.contains(data_search), ['제목', '저자', 'ISBN', '대여여부']])  # 저자 데이터가 일부분이라도 포함되어 있으면 제목, 저자, ISBN, 대여여부 순으로 출력
            print("저자")
            return self.A_search_np
            

    def book_append(self, check_ISBN, title, author, pub, price, link, explanation):  # 도서 추가
        app_df = self.Book_df[(self.Book_df["ISBN"] == int(check_ISBN))]
        if (app_df['ISBN'] == int(check_ISBN)).any():  # 동일한 ISBN이 하나라도 있는지 판별
            print('중복된 ISBN입니다.')
            return True
        else:
            data_to_insert = ([{'ISBN': check_ISBN, '제목': title, '저자': author, '출판사': pub, '가격': price, '관련링크': link,
                                '도서설명': explanation, '대여여부': True}])  # 입력한 데이터를 딕셔너리로 생성
            df_to_insert = pd.DataFrame(data=data_to_insert)  # 새로운 데이터프레임에 등록하고자 하는 data_to_insert 데이터 저장
            self.Book_df = pd.concat([self.Book_df, df_to_insert]).sort_values(by=['제목'],
                                                                               axis=0)  # 기존의 데이터프레임 df와 새로운 데이터프레임 df_to_insert를 제목 기준 오름차순으로 병합
            self.Book_df.to_csv('Book_list.csv', encoding='utf-8', index=False)  # 등록된 데이터프레임을 확인하는 csv 파일 생성
            
    def book_modify(self, check_ISBN, title, author, pub, price, link, explanation):  # 도서 수정
        mod_df = self.Book_df[(self.Book_df["ISBN"] == int(check_ISBN))]
        if (mod_df['ISBN'] == int(check_ISBN)).any():  # 동일한 ISBN 하나라도 있는지 확인
            self.Book_df.loc[self.Book_df.ISBN == int(check_ISBN), ('제목', '저자', '출판사', '가격', '관련링크', '도서설명')] = (
            title, author, pub, price, link, explanation)  # ISBN을 기준으로 수정하고자 하는 컬럼의 데이터 수정
            self.Book_df = self.Book_df.sort_values(by=['제목'], axis=0)
            self.Book_df.to_csv('Book_list.csv', encoding='utf-8', index=False)  # 수정된 데이터를 확인하기 위한 csv 파일 생성
            return True
        else:
            print('존재하지 않는 도서입니다.\n')

    def book_delete(self, del_ISBN):  # 도서 삭제
        del_df = self.Book_df[(self.Book_df["ISBN"] == int(del_ISBN))]  # ISBN이 동일한 도서의 데이터를 확인하기 위한 데이터 프레임 생성
        if (del_df['ISBN'] == int(del_ISBN)).any(): 
            if (del_df['대여여부'] == False).any():  # 대여를 하고 있는 경우
                print('대여 중인 도서입니다.\n')
                return False
            elif (del_df['대여여부'] == True).any():  # 대여를 하지 않은 경우
                self.Book_df = self.Book_df.drop(index=self.Book_df.loc[self.Book_df.ISBN == int(del_ISBN)].index)  # 해당 ISBN을 가진 데이터프레임의 인덱스(행)를 삭제
                self.Book_df.to_csv('Book_list.csv', encoding='utf-8', index=False)  # 삭제 후 데이터를 확인하기 위한 csv 파일 생성
                return True
        else:  # 해당하는 ISBN을 가진 데이터가 없는 경우
            print('존재하지 않는 도서입니다.\n')
    
    def del_ISBN(self, del_ISBN):
            self.B_del_np = np.array(self.Book_df[(self.Book_df["ISBN"] == int(del_ISBN))])  # ISBN이 동일한 도서의 데이터를 확인하기 위한 데이터 프레임 생성
            return self.B_del_np
        
    def book_rent(self):  # 도서 대여
        rent_date = datetime.today()  # 대여일
        return_date = datetime.today() + timedelta(14)  # 대여 기간 계산

        check_Phone = input("전화번호")  # 대여하고자하는 회원이 존재하는 경우
        if (self.User_df['전화번호'] == check_Phone).any():  # 동일한 전화번호가 하나라도 있는지 확인
            rent_ISBN = int(input("ISBN"))
            rent_df = self.Book_df[(self.Book_df["ISBN"] == rent_ISBN)]
            if (self.user_rent_df['ISBN'] == rent_ISBN).any():  # 대여하고자 하는 도서가 대여 중인 경우
                print("대여 중인 도서입니다.\n")
            elif (rent_df['ISBN'] != rent_ISBN).all():
                print("존재하지 않는 도서입니다.\n")
            else:
                print("대여 완료 됐습니다.\n")
                rent_df_insert = {'ISBN': rent_ISBN, '제목': rent_df['제목'], '전화번호': check_Phone,
                                  '대여여부': False, '대여일': rent_date.strftime("%Y-%m-%d"),
                                  '반납예정일': return_date.strftime("%Y-%m-%d")}  # 대출 관리 데이터 생성

                self.Book_df.loc[self.Book_df.ISBN == rent_ISBN, ('대여여부')] = (False)  # 도서 데이터 프레임에 있는 데이터도 대여 불가로 변경
                #self.Book_df.to_csv('Book_input.csv', encoding='utf-8', index=False)  # 등록된 데이터프레임을 확인하는 csv 파일 생성
                rent_df_insert = pd.DataFrame(data=rent_df_insert)  # 새로운 데이터프레임에 등록하고자 하는 rent_df_insert 데이터 저장
                self.user_rent_df = pd.concat([self.user_rent_df, rent_df_insert]).sort_values(by=['제목'],
                                                                                               axis=0)  # 기존에 있던 유저 데이터 프레임에 rent_df_insert 데이터 추가
                self.user_rent_df.to_csv('Book_rent.csv', encoding='utf-8', index=False)  # 대여한 데이터를 확인하기 위한 csv 파일 생성
        else:
            print("존재하지 않는 회원입니다.\n")  # 대여하고자하는 회원이 존재하지 않는 경우

    def book_return(self):  # 도서 반납
        check_Phone = input("전화번호")  # 반납하고자하는 회원이 존재하는 경우
        phone_df = self.user_rent_df[(self.user_rent_df["전화번호"] == check_Phone)]  # 회원의 전화번호로 대여된 도서가 있는지 확인
        print(phone_df)
        if (phone_df['전화번호'] == check_Phone).any():  # 동일한 전화번호가 하나라도 있는지 확인
            return_ISBN = int(input("ISBN"))
            if (phone_df['ISBN'] == return_ISBN).any():  # 반납하고자 하는 도서 ISBN이 동일한 경우
                if (phone_df['대여여부'] == False).any():  # 대여 중인 경우
                    self.Book_df.loc[self.Book_df.ISBN == return_ISBN, ('대여여부')] = (True)
                    self.user_rent_df.loc[self.user_rent_df.ISBN == return_ISBN, ('대여여부', '대여일', '반납예정일')] = (
                    True, None, None)  # ISBN을 기준으로 수정하고자 하는 컬럼의 데이터 수정
                    
            else:
                print("대여중인 도서가 아닙니다.\n")
        else:
            print("존재하지 않은 회원입니다.\n")  # 반납하고자하는 회원이 존재하지 않는 경우

    
        
''' 클래스 코드 확인 용
book_Pandas = Panda('Book_list.csv', 'user_list.csv','User_rent.csv.csv')

book_Pandas.book_search("제목")
book_Pandas.book_append()
book_Pandas.book_modify()
book_Pandas.book_delete()
book_Pandas.book_rent()
book_Pandas..book_return()

'''

