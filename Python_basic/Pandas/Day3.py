## 함수 적용

import pandas as pd

df = pd.read_excel('score.xlsx', index_col='지원 번호')

## 보통 타입에 다른 데이터 수정에 함수 사용

# def add_cm(height):
#     return str(height) +'cm'

# df['키'] = df['키'].apply(add_cm)

# def capitalize(lang):
#     if pd.notnull(lang):
#         return lang.capitalize()
#     return lang

# df['SW특기'] = df['SW특기'].apply(capitalize)
# ## df['SW특기'].str.capitalize() 
# ## 데이터 형변환이 없거나 복잡하지 않은 변환이라면
# ## 단순 처리 가능
# print(df)


### 그룹화 -> 보통 집계를 하기위해 사용

# school_group = df.groupby('학교')
# # print(df.groupby('학교').get_group('북산고'))

# # print(df.groupby('학교').mean())
# # print(df.groupby('학교').size())
# # print(df.groupby('학교').size()['능남고'])
# # print(df.groupby('학교')['키'].mean())


# # 새로운 칼럼 정의

# df['학년'] = [3,3,2,1,1,3,2,2]
# # ## 학교별 학년별
# # print(df.groupby(['학교','학년']).mean())
# # print(df.groupby('학년').mean().sort_values('키'))

# ## 비율
# #print(group_df['이름','SW특기'].count()) 

# ## 학년별 학생수 (value_counts -> nomarlize 옵션으로 정규화 가능(비율))
# print(school_group['학년'].value_counts(normalize=True).loc['북산고'])

