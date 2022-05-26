#pandas 기초

from operator import index
from numpy import true_divide
import pandas as pd
#1. Series

# 1차원 데이터
## Series 객체 생성
# temp = pd.Series([-20,-10,10,20])
# #print(temp)
# temp[0] # 1번째 데이터

# # Series 인덱스 지정
# temp = pd.Series([-20,-10,10,20] ,index =['J','F','M','A'])
# print(temp['J'])

## DataFrame / Series의 집합 / 2차원 데이터

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
# # print(data)
# #df = pd.DataFrame(data)
# #print(df)
# # print(df[['이름','키']]) # 2개이상 칼럼은 리스트 형태로 전달

# #df index 지정
# #df = pd.DataFrame(data, index=('1번','2번','3번','4번','5번','6번','7번','8번'))
# ## index 갯수 안맞으면 에러남
# #print(df)

# #df 에서 원하는 칼럼만 지정 or 칼럼 순서 변경
# # df = pd.DataFrame(data, columns=['이름','키','학교'])
# # print(df)

# ##index 심화

df = pd.DataFrame(data, index=('1번','2번','3번','4번','5번','6번','7번','8번'))
# #print(df.index)

# #index 이름 지정
df.index.name ='지원 번호'
# #print(df)

# #inplace 속성은 df객체에 결과를 바로 반영시킴 
# # df.reset_index(inplace=True)
# # print(df)

# # reset_index는 이전에 지정한 인덱스 이름과 인덱스 값을 새로운 칼럼으로 만들어줌
# ## drop 속성을 true로 하면 삭제가 됨
# df.reset_index(inplace=True, drop=True)
# # print(df)

# ## column 중 하나를 인덱스로 할 수 있음
# df.set_index('이름', inplace=True)
# #print(df)

# # 지정한 인덱스로 정렬도됨 -> 칼럼을 기준으로 정렬하는 효과
# df.sort_index(inplace=True,ascending=False ) ## ascending=False (내림차순)
# print(df) #이름으로 정렬됨


##DataFrame <> 파일저장 및 열기(excel, csv , txt)

## 저장하기
# 1.csv / comma로 데이터 구분
#df.to_csv('score.csv' ,encoding='utf-8-sig', index=False) 
#encodeing 옵션이 엑셀로 열었을때 한글이 안깨지게 해줌 , index 옵션으로 인덱스 저장여부 전달

# 2.txt / csv와 동일한 메소드 사용
#df.to_csv('score.txt', sep='\t')

# 3. excel / openpyxl 모듈설치 pip install openpyxl
# df.to_excel('score.xlsx')

## 읽어오기
# 1. csv
# df1 = pd.read_csv('score.csv', nrows=0) 
#print(df1)
# 특정 row 스킵가능(skiprows) , 정수 전달하면 해당 갯수만큼 스킵 or 리스트를 전달하면 해당 번째(index 0~)의 로우 스킵
#print(df1)
# 지정한 갯수만큼 가져오기도 가능(nrows) , 0을 주면 칼럼명만 가져옴 
#print(df1)
# 혼합해서 ex) 처음 2개 무시하고 4개 가져오기   // 주의점은 skiprow는 칼럼헤더를 포함하지만 nrows 는 포함하지 않음
# skiprow가 2개 로우 빼면서 헤더를 빼면 nrows가 데이터를 칼럼헤더로 인지하게 되면서 해당 로우 뒤로 4개를 더가져옴 

# 2. txt
# df2 = pd.read_csv('score.txt', sep='\t', index_col='지원 번호')
# #index_col 을 통해 인덱스 칼럼 지정가능 / 파일을 불러온 후 set_index와 동일함 단, inplace 옵션 필수
# print(df2)

# 3. excel
# df3 = pd.read_excel('score.xlsx' , index_col='지원 번호')
# # txt 불러올때랑 마찬가지로 불러오면서 인덱스 한줄이 자동생성됨 , index_col 을 통해 자동생성 방지 가능
# print(df3)