import numpy as np
import pandas as pd


class Main:
    def __init__(self, user): # self에 인스턴스 전달되어 있음. . 그래서 변수작성이나 참고 가능하고. . 자동 호출
        self.USER = pd.read_csv(user).sort_values(by=['이름'], axis=0) # 데이터 프레임


    def user_search(self, cho): # 회원 검색
        if cho == '이름':
            ins = input('이름을 입력하세요. : ')
            if (self.USER['이름'] == ins).any():
                search = np.array(self.USER.loc[self.USER['이름'].str.contains(ins), ['전화번호', '이름', '생년월일', '성별', '이메일', '탈퇴여부']]) # contains 특정단어검색 loc 행단위 출력
                return search
            else:
                print('등록되어 있지 않은 회원입니다.\n')
        elif cho == '전화번호':
            ins = input('전화번호를 입력하세요. : ')
            if (self.USER['전화번호'] == ins).any():
                search = np.array(self.USER.loc[self.USER['전화번호'].str.contains(ins), ['전화번호', '이름', '생년월일', '성별', '이메일', '탈퇴여부']])
                return search
            else:
                print('등록되어 있지 않은 회원입니다.\n')


    def user_append(self, phone, name, birth, sex, email): # 회원 등록
        ins = input('전화번호를 입력하세요. : ')
        if (self.USER['전화번호'] == ins).any(): # 전화번호 중복 검색
            print('중복된 전화번호입니다.\n')
        else:
            append = pd.DataFrame({'전화번호': phone, '이름': name, '생년월일': birth, '성별': sex, '이메일': email, '탈퇴여부':True})
            self.USER = pd.concat([self.USER, append]).sort_values(by='이름', axis=0)
            self.USER.to_csv('USER_list.csv', index=None)


    def user_modify(self, phone, name, birth, sex, email): # 회원 수정
        ins = input('전화번호를 입력하세요. : ')
        if (self.USER['전화번호'] == ins).any():  # 전화번호 검색
            self.USER.loc[self.USER['전화번호'].str.contains(ins), ('전화번호', '이름', '생년월일', '성별', '이메일')] = (phone, name, birth, sex, email)
            self.USER.to_csv('USER_list.csv', index=None)
        else:
            print('등록되지 않은 회원입니다.\n')


    def user_delete(self): # 회원 탈퇴
        ins = input('전화번호를 입력하세요. : ')
        if (self.USER['전화번호'] == ins).any():
            if (self.USER['대여여부'] == True).any(): # 대여여부 관련 물어보고 수정
                print('책을 대여 중인 회원입니다.\n')
            else:
                print('탈퇴되었습니다.\n')

        else:
            print('등록되지 않은 회원입니다.\n')
