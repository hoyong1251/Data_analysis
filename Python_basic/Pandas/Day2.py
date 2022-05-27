## Data confirm 

import pandas as pd

df = pd.read_excel('score.xlsx', index_col='지원 번호')
# print(df)

# Dataframe 확인
# print(df.describe())
## 계산 가능 데이터들에 칼럼별로 대해 기본 통계정보를 계산해줌 - count 평균 표준편차 최대,최소,4분위 
# print(df.info())
# 데이터들의 타입을 보여줌 / 메모리도 보여줌

## 데이터가 많으면 , 추출할 수 있음
# print(df.head(7)) # 데이터 처음부터 갯수만큼만 추출 default로 5개
# print(df.tail(4)) # 뒤에서 부터 추출

# print(df.values) # 2차원 리스트로 반환 
# print(df.index)
# print(df.columns)
# print(df.shape) # (row, column) 수


# Series 확인 / col 값하나를 이용해 2차원을 1차원으로 변형
# print(df['키'].describe()) 
# print(df['키'].max())
# print(df['키'].nlargest(3))
# print(df['키'].mean())
# print(df['키'].sum())
# print(df['키'].count())
# print(df['학교'].unique()) ## distinct 
# print(df['학교'].nunique()) ## distinct count



## 데이터 선택(기본) - 자주 활용

# 1. col 선택 (label)
# print(df['키']) # 복수 col은 리스트 형태로 전달

# 2. col 선택 (index)
# print(df.columns[0])
# print(df[df.columns[-1]]) # col이 많거나 이름을 모를때 유용 / columns 리스트 슬라이싱 가능
# print(df['키'][0:5]) # row도 슬라이싱 가능
# print(df[['영어','키']][:3]) # 혼합 가능
# print(df[3:]) # col 정보 없이 row만 가능

# 3. row 선택 (loc)
# print(df.loc['1번']) # index에 해당하는 row 데이터 전체
# print(df.loc['1번', '국어']) # row 데이터 중 가져올 col 선택가능
# print(df.loc[['1번','2번'],['국어','영어']]) # 복수 선택 가능
# print(df.loc['1번':'6번' , '국어':'사회']) # 슬라이스로 가져올때는 복수 선택처럼 한번더 리스트로 감싸지 않아도 됨
## 심지어 슬라이스 원래 규칙과 좀 다르게 오른쪽 끝을 포함


# 4. row 선택 (iloc) - 정수기반 선택
# print(df.iloc[0]) # 0이 header가 아님 / col header는 row로 생각하지 않음 
# print(df.iloc[0:5]) # 정수기반 슬라이싱하면 원래 규칙을 따라서 오른쪽 끝 포함x
# print(df.iloc[0,1]) # 다른 문법 동일 
# print(df.iloc[lambda x: x.index=='1번']) ## df.iloc[lambda x: x.index % 2 == 0] 람다식도 가능 

# 5. 조건 기준 선택
# print(df['키']>=185) # 각 row에 대해 조건의 T/F 반환 
# filt = (df['키'] >= 185) & (df['학교'] == '능남고')
# print(df[~filt]) # boolean mask가 적용 가능 / not연산자(~ , -) 사용가능

# filter를 사용해 sql 처럼 사용가능 / 조건 연산자(& , |) 를 결합해 다양한 조건 생성 가능
# print(df.loc[filt , '이름'])

# 6. str 함수 활용 / 문자열 필터를 말함(와일드카드 역할)
# filt2 = df['이름'].str.startswith('송')
# filt2 = df['이름'].str.contains('태')     ### contains 는 NAN 정보에 대해 T/F 필터링이 안됨 

# in 활용
# langs = ['python', 'c#']  # 대소문자 구분
# filt2 = df['SW특기'].str.lower().isin(langs)
# print(df[filt2])

# filt3 = df['SW특기'].str.contains('Java', na=False) ## contains 결과중 필터링하지못한 NA 값 처리 방법 > na= 옵션 적용
# print(df[filt3])

####
## 그외 다양한 pands 문자열 처리 함수 : https://pandas.pydata.org/docs/user_guide/text.html