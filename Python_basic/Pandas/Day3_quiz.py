## pandas 퀴즈

import pandas as pd
data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)

## 1) 전체 데이터 중 영화 정보만 출력
# print(df['영화'])

# ## 2) 전체 데이터 중 영화 평점만 출력
# print(df[['영화','평점']])

## 3) 2015년 이후 개봉 중 영화 개봉연도 만 출력
# filt = df['개봉 연도'] >= 2015
# print(df.loc[filt, ['영화','개봉 연도']])

## 4) 추천점수 col 추가
## 추천점수 = (관객수 *평점) // 100
# def score(people):
#     return people*10000
# score_scalar = df['관객 수'].apply(score)
# star_points = df['평점']
# scores = []
# for i,j in zip(score_scalar,star_points):
#     scores.append((i*j) // 100)
# df['추천 점수'] = scores

#############
# df['추천 점수'] = (df['관객 수'] * df['평점'] // 100) 도 가능
#############
# print(df)


## 5) 전체 데이터를 개봉연도 기준 내림차순

# print(df.sort_values('개봉 연도' , ascending=False ,inplace=True))

# print(df[['영화','개봉 연도']])