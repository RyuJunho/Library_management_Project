import numpy as np
import pandas as pd
from tkinter import messagebox

class Main:
    def __init__(self, user, rent): # self에 인스턴스 전달되어 있음. 변수작성, 참고 가능. 자동 호출
        self.USER = pd.read_csv(user).sort_values(by=['이름'], axis=0) # 데이터 프레임
        self.RENT = pd.read_csv(rent).sort_values(by=['대여여부'], axis=0)

    def user_search(self, combox, in_nanum): # 회원 검색
        if combox == '이름':
            search = np.array(self.USER.loc[self.USER['이름'].str.contains(in_nanum), ['이름', '전화번호', '성별', '탈퇴여부']]) # contains 특정단어검색 loc 행단위 출력
            print('이름')
            return search
        elif combox == '전화번호':
            search = np.array(self.USER.loc[self.USER['전화번호'].str.contains(in_nanum), ['이름', '전화번호', '성별', '탈퇴여부']])
            return search
        else:
            messagebox.showerror('알림', '잘못 입력하셨습니다.')

    def user_append(self, name, birth, sex, phone, email): # 회원 등록
        if (self.USER['전화번호'] == phone).any(): # 전화번호 중복 검색
            return True
        else:
            if sex == 1: # 성별
                sex_ = False
                return sex_
            elif sex == 2:
                sex_ = True
                return sex_

            append = pd.DataFrame([{'이름': name, '생년월일': birth, '성별': sex_, '전화번호': phone, '이메일': email, '탈퇴여부': True}])
            self.USER = pd.concat([self.USER, append]).sort_values(by='이름', axis=0)
            self.USER.to_csv('user_list.csv', index=False)


    def user_modify(self, ins, phone, name, birth, sex, email): # 회원 수정
        if (self.USER['전화번호'] == ins).any():  # 전화번호 검색
            self.USER.loc[self.USER['전화번호'].str.contains(ins), ('전화번호', '이름', '생년월일', '성별', '이메일')] = (phone, name, birth, sex, email)
            self.USER.to_csv('user_list.csv', index=None)
        else:
            print('등록되지 않은 회원입니다.\n')

    def user_delete(self, rent): # 회원 탈퇴 - 회원 대여여부 검색
        if (self.RENT['전화번호'] == rent).any(): # 대여여부 관련 물어보고 수정
            print('책을 대여 중인 회원입니다.\n')
            return True
        else:
            return False

    def user_delete_check(self, phone): # 회원 탈퇴 - 회원 중복 검색
        if (self.USER['전화번호'] == phone).any():
            return True
        else:
            print('등록되지 않은 회원입니다.\n')
            return False

    def user_number(self, phone):
        data_in = np.array(self.USER[self.USER['전화번호'] == phone])
        return data_in
