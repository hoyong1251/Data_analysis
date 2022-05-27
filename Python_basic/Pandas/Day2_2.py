### 결측치 처리
import pandas as pd

df = pd.read_excel('score.xlsx', index_col='지원 번호')
# NAN 같은 빈 데이터를 결측치라고 함

# # 직접 NAN 넣는 방법 
# import numpy as np
# df['학교'] = np.nan
# print(df)

# 1. 임의의 값으로 교체 > fillna (데이터프레임 전체를 대상으로 NAN값을 찾아서 바꿈)

#df.fillna(" ", inplace =True)

##일부 칼럼만 NA 처리
# df['SW특기'].fillna(' ' ,inplace=True)

# print(df)

# 2. 결측치 삭제 > dropna (na 가 포함된 row 전체 삭제)

# df.dropna(inplace=True)
# print(df)
# axis 옵션 : index > na가 포함된 row 삭제(default) / columns > na가 포함된 col 삭제
# how 옵션 : any > na가 한개라도 있으면 삭제(default) / all > 전부 na 일때 삭제 



## 데이터 정렬

# 1. sort_values
# print(df.sort_values('키',ascending=False))
# print(df.sort_values(['키', '수학'], ascending=[True,False])) # 각 칼럼에 다른 정렬순서를 부여할 수 있음

## df['키'] 로 Series의 정렬도 가능

# 2. sort_index / 인덱스 기준 정렬
# print(df.sort_index(ascending=False))



## 데이터 수정

# 1. col 수정 / replace 메소드에 dict를 활용해 수정
# df['학교'].replace({'북산고': '성북고', '능남고':'고봉고'}, inplace=True)
# print(df)

# 2. row 수정 / 대입연산자
# df['SW특기'] = df['SW특기'].str.upper()
# # print(df)

# df['학교'] = df['학교'] +'등학교'
# print(df)

# 1. col 추가
df['총합'] = df['국어']+ df['영어'] +df['수학']+df['과학']+df['사회']
# # print(df)
df['결과'] = 'Fail'

df.loc[df['총합']>400, '결과'] = 'Pass' # 조건 추가 
# print(df)

# 2. col 삭제
df.drop(columns='총합',inplace=True)
# print(df)

# # 3. row 삭제
# df.drop(index='4번',inplace=True)
# print(df)

# d_index = df.loc[df['수학']<80].index
# df.drop(index=d_index, inplace=True)
# print(df)

## 4. row 추가 / 대입연산
# df.loc['9번'] = ['이정환', '해망고', 184,90,90,90,90,90,'Kotlin','Pass']
# print(df)


# 5. col 순서 변경 / list 슬라이싱
# cols = list(df.columns)
# df = df[['결과']+cols[0:-1]]  / # df = df[[cols[-1]]+cols[0:-1]]
# print(df)

# 6. col 이름 변경
# df.columns = ['a','b','c','d','e','f','g','h','i','j'] # 칼럼수 안맞으면 에러
# print(df)

# Cell 수정
# df.loc['row', 'col'] 
# df.loc['4번', ['SW특기','학교']] = ['Python','능남고']
# print(df)