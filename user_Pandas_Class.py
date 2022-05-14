import numpy as np
import pandas as pd
from tkinter import messagebox


class Main:
    def __init__(self, user, rent): # self에 인스턴스 전달되어 있음. 변수작성, 참고 가능. 자동 호출
        self.USER = pd.read_csv(user).sort_values(by=['이름'], axis=0) # 데이터 프레임
        self.RENT = pd.read_csv(rent).sort_values(by=['대여여부'], axis=0)

    def user_search(self, combox, in_nanum): # 회원 검색
        if combox == '이름':
            search = np.array(self.USER.loc[self.USER['이름'].str.contains(in_nanum), ['이름', '전화번호', '성별', '탈퇴여부']])  # contains 특정단어검색 loc 행단위 출력
            for index, value in enumerate(search[:, 2]):
                if value:
                    search[index, 2] = '남자'
                elif not value:
                    search[index, 2] = '여자'
            for index, value in enumerate(search[:, 3]):
                if value:
                    search[index, 3] = 'X'
                elif not value:
                    search[index, 3] = 'O'
            return search
        elif combox == '전화번호':
            search = np.array(self.USER.loc[self.USER['전화번호'].str.contains(in_nanum), ['이름', '전화번호', '성별', '탈퇴여부']])
            for index, value in enumerate(search[:, 2]):
                if value:
                    search[index, 2] = '남자'
                elif not value:
                    search[index, 2] = '여자'
            for index, value in enumerate(search[:, 3]):
                if value:
                    search[index, 3] = 'O'
                elif not value:
                    search[index, 3] = 'X'
            return search
        else:
            messagebox.showerror('알림', '잘못 입력하셨습니다.')

    def user_append(self, name, birth, sex, phone, email):  # 회원 등록
        if (self.USER['전화번호'] == phone).any():  # 전화번호 중복 검색
            return True
        else:
            append = pd.DataFrame([{'이름': name, '생년월일': birth, '성별': sex, '전화번호': phone, '이메일': email, '탈퇴여부': True}])
            self.USER = pd.concat([self.USER, append]).sort_values(by='이름', axis=0)
            self.USER.to_csv('user_list.csv', index=False)

    def user_modify(self, ph_in, name, birth, sex, phone, email):  # 회원 수정
        del_us = self.USER[(self.USER['전화번호'] == phone)]
        if (del_us['전화번호'] == phone).any():
            print('등록되지 않은 회원입니다.\n')
            return False
        else:
            self.USER.loc[self.USER.전화번호 == ph_in, ('이름', '생년월일', '성별', '전화번호', '이메일', '탈퇴여부')] = (
                name, birth, sex, phone, email, True)
            self.USER = self.USER.sort_values(by=['이름'], axis=0)
            self.USER.to_csv('user_list.csv', index=False)
            return True

    def user_modi(self, ph_in, name, birth, sex, phone, email):
        if ph_in == phone:
            self.USER.loc[self.USER.전화번호 == ph_in, ('이름', '생년월일', '성별', '전화번호', '이메일', '탈퇴여부')] = (
                name, birth, sex, phone, email, True)
            self.USER = self.USER.sort_values(by=['이름'], axis=0)
            self.USER.to_csv('user_list.csv', index=False)
            return True
        else:
            return False


    def user_delete(self, rent):  # 회원 탈퇴 - 회원 대여여부 검색
        if (self.RENT['전화번호'] == rent).any():
            print('책을 대여 중인 회원입니다.\n')
            return True
        else:
            self.USER.loc[self.USER['전화번호'].str.contains(rent), ('탈퇴여부')] = (False)
            self.USER.to_csv('user_list.csv', index=None)
            return False

    def user_check(self, phone):  # 회원 탈퇴 - 회원 중복 검색
        del_us = self.USER[(self.USER['전화번호'] == phone)]
        if (del_us['전화번호'] == phone).any():
            if (del_us['탈퇴여부'] == False).any():
                print('이미 탈퇴한 회원입니다.\n')
                return False
            else:
                return True
        else:
            print('존재하지 않은 회원입니다.\n')
            return False

    def user_number(self, phone):  # 해당 회원 상세정보 저장
        data_in = np.array(self.USER[self.USER['전화번호'] == phone])
        return data_in

    def user_rent(self, phone):  # 회원 탈퇴 - 도서 트리뷰 추가
        del_tree = self.RENT[(self.RENT['전화번호'] == phone)]
        #if (del_tree['전화번호'] == phone).any():
        search = np.array(self.RENT.loc[self.RENT['전화번호'].str.contains(phone), ['제목', '반납예정일']])
        return search
        #else:
        #    print('대여중인 도서가 없습니다.')
        #    search = np.array([None, None])
        #    return search

    def phone_cut(self, phone):
        phone1 = phone[0:3]
        phone2 = phone[4:8]
        phone3 = phone[9:13]
        return phone1, phone2, phone3

    def sex_change(self, sex):
        if sex == 1:
            sex = False
            return sex
        elif sex == 2:
            sex = True
            return sex

    def user_ren(self, rent):  # 회원 수정 - 대여여부 검색
        if (self.RENT['전화번호'] == rent).any():
            print('책을 대여 중인 회원입니다.\n')
            return True
        else:
            return False
