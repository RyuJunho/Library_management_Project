import pandas as pd
import numpy as np
from datetime import datetime, timedelta


class Panda:
    def __init__(self, data, user):   # 클래스 시작 항상 실행, 객체 생성 시 자동 호출
        self.Book_df = pd.read_csv(data).sort_values(by=['제목'], axis=0) # 데이터 프레임을 공유하기 위한 자신을 참조하는 매개변수 self로 데이터 프레임 생성
        self.User_df = pd.read_csv(user).sort_values(by=['이름'], axis=0)

    def book_search(self, combo):
        if combo == "제목":
            data_Tsearch = input("제목을 입력하세요 : ")   # 제목 데이터
            B_search_np = np.array(self.Book_df.loc[self.Book_df['제목'].str.contains(data_Tsearch), ['제목', '저자', 'ISBN', '대여여부']])   # 제목 데이터가 일부분이라도 포함되어 있으면 제목, 저자, ISBN, 대여여부 순으로 출력
            return B_search_np
        elif combo == "저자":
            data_Asearch = input("저자를 입력하세요 : ")    # 저자 데이터
            B_search_np = np.array(self.Book_df.loc[self.Book_df['저자'].str.contains(data_Asearch), ['제목', '저자', 'ISBN', '대여여부']])   # 저자 데이터가 일부분이라도 포함되어 있으면 제목, 저자, ISBN, 대여여부 순으로 출력
            return B_search_np
        
    def book_append(self):
        check_ISBN = int(input("ISBN을 입력하세요 : "))
        if (self.Book_df['ISBN'] == check_ISBN).any():    # 동일한 ISBN이 하나라도 있는지 판별
            print('중복된 ISBN입니다.')
        else:
            title = input("제목")
            author = input("저자")
            pub = input("출판사")
            price = int(input("가격"))
            link = input("관련링크")
            explanation = input("도서설명")
            
            data_to_insert = ([{'ISBN': check_ISBN, '제목': title, '저자': author, '출판사': pub, '가격': price, '관련링크': link, '도서설명': explanation, '대여여부': False}])
            df_to_insert = pd.DataFrame(data=data_to_insert)    # 새로운 데이터프레임에 등록하고자 하는 data_to_insert 데이터 저장
            self.Book_df = pd.concat([self.Book_df,df_to_insert]).sort_values(by=['제목'], axis=0)    # 기존의 데이터프레임 df와 새로운 데이터프레임 df_to_insert를 제목 기준 오름차순으로 병합
            self.Book_df.to_csv('Book_input.csv', encoding='utf-8', index=False) # 등록된 데이터프레임을 확인하는 csv 파일 생성

    def book_modify(self):
        check_ISBN = int(input("ISBN을 입력하세요 : "))
        if (self.Book_df['ISBN'] == check_ISBN).any():  # 동일한 ISBN 하나라도 있는지 확인
            title = input("제목")
            author = input("저자")
            pub = input("출판사")
            price = int(input("가격"))
            link = input("관련링크")
            explanation = input("도서설명")

            self.Book_df.loc[self.Book_df.ISBN == check_ISBN, ('제목', '저자', '출판사', '가격', '관련링크', '도서설명')] = \
                (title, author, pub, price, link, explanation)  # ISBN을 기준으로 수정하고자 하는 컬럼의 데이터 수정
            self.Book_df = self.Book_df.sort_values(by=['제목'], axis=0)
            self.Book_df.to_csv('Book_input.csv', encoding='utf-8', index=False)  # 수정된 데이터를 확인하기 위한 csv 파일 생성
        else:
            print('존재하지 않는 도서입니다.\n')

    def book_delete(self):
        del_ISBN = int(input("ISBN을 입력하세요 : "))
        del_df = self.Book_df[(self.Book_df["ISBN"] == del_ISBN)]  # ISBN이 동일한 도서의 데이터를 확인하기 위한 데이터 프레임 생성
        if (del_df['대여여부'] == False).any():  # 대여를 하고 있는 경우
            print('대여 중인 도서입니다.\n')
        elif (del_df['대여여부'] == True).any():  # 대여를 하지 않은 경우
            self.Book_df = self.Book_df.drop(index=self.Book_df.loc[self.Book_df.ISBN == del_ISBN].index)  # 해당 ISBN을 가진 데이터프레임의 인덱스(행)를 삭제
            self.Book_df.to_csv('Book_input.csv', encoding='utf-8', index=False)  # 삭제 후 데이터를 확인하기 위한 csv 파일 생성
        else:  # 해당하는 ISBN을 가진 데이터가 없는 경우
            print('존재하지 않는 도서입니다.\n')

'''
    def book_rent(self):
        rent_date = datetime.today()  # 대여일
        return_date = datetime.today() + timedelta(14)  # 대여 기간 계산

        user_to_insert = {'ISBN': [54832, 15485, 48514], '제목': ['동물농장', '수레바퀴 아래서', '데이터 과학을 위한 파이썬 머신러닝'],
                          '전화번호': ['010-1234-5678', '010-1478-5236', '010-8523-7413'],
                          '대여여부': [False, False, False],
                          '대여일': [rent_date.strftime("%Y-%m-%d"), rent_date.strftime("%Y-%m-%d"),
                                  rent_date.strftime("%Y-%m-%d")],
                          '반납예정일': [return_date.strftime("%Y-%m-%d"), return_date.strftime("%Y-%m-%d"),
                                    return_date.strftime("%Y-%m-%d")]}  # 대출관리 초기 데이터
        user_rent_df = pd.DataFrame(data=user_to_insert).sort_values(by=['제목'], axis=0)  # 대출관리 초기 데이터를 데이터 프레임으로 생성
        user_rent_df.to_csv('Book_BasicRent.csv', encoding='utf-8', index=False)  # 초기 데이터 csv 생성

        print("\n도서 대여")

        user_list_df = pd.DataFrame(data=user_list_csv)  # 이름을 기준으로 데이터 프레임 생성

        user_rent_csv = pd.read_csv('./Book_BasicRent.csv')  # 대출관리 csv 불러옴
        user_rent_df = pd.DataFrame(data=user_rent_csv).sort_values(by=['제목'], axis=0)  # 제목을 기준으로 데이터 프레임 생성

        check_Phone = '010-1234-5678'  # 대여하고자하는 회원이 존재하는 경우
        rent_ISBN = 56789  # 다른 회원이 대여하고 있지 않은 경우
        rent_df = df[(df["ISBN"] == rent_ISBN)]  # 다른 회원이 대여 하고 있지 않은 도서의 데이터 프레임 생성

        if (user_list_df['전화번호'] == check_Phone).any():  # 동일한 전화번호가 하나라도 있는지 확인
            if (user_rent_df['ISBN'] == rent_ISBN).any():  # 대여하고자 하는 도서가 대여 중인 경우
                print("대여 중인 도서입니다.\n")
            else:
                print("대여 완료 됐습니다.\n")
                rent_df_insert = {'ISBN': rent_df['ISBN'], '제목': rent_df['제목'], '전화번호': check_Phone,
                                  '대여여부': False, '대여일': rent_date.strftime("%Y-%m-%d"),
                                  '반납예정일': return_date.strftime("%Y-%m-%d")}  # 대출 관리 데이터 생성
                df.loc[df.ISBN == rent_ISBN, ('대여여부')] = (False)
                re_df_insert = pd.DataFrame(data=rent_df_insert)  # 새로운 데이터프레임에 등록하고자 하는 rent_df_insert 데이터 저장
                user_rent_df = pd.concat([user_rent_df, re_df_insert]).sort_values(by=['제목'],
                                                                                   axis=0)  # 기존에 있던 유저 데이터 프레임에 rent_df_insert 데이터 추가
                user_rent_df.to_csv('Book_rent.csv', encoding='utf-8', index=False)  # 대여한 데이터를 확인하기 위한 csv 파일 생성
        else:
            print("존재하지 않은 회원입니다.\n")  # 대여하고자하는 회원이 존재하지 않는 경우
'''


'''
book_Srh_Pan = Panda('Book_input.csv')
book_Srh_Pan.book_search("제목")

book_App_Pan = Panda('Book_input.csv')
book_App_Pan.book_append()

book_mod_Pan = Panda('Book_input.csv')
book_mod_Pan.book_modify()

book_delete = Panda('Book_input.csv', 'user_list.csv')
book_delete.book_delete()
'''

