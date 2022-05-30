from optparse import Values
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)

## 1) x축에 영화 y축에 평점인 막대그래프
# x_data, y_data = df['영화'], df['평점']
# plt.bar(x_data,y_data)
# # plt.show()

## 2) 막대그래프에 세부사항 적용 제목: 국내 top8 영화 평점 정보 / x축 영화 제목(90도회전) y축 평점 텍스트 추가
# plt.title("국내 top 8 영화 평점 정보")
# plt.xlabel("영화")
# plt.xticks(rotation=90)
# plt.ylabel("평점")
# plt.show()

## 3) 개봉연도별 평점 변화 추이를 꺾은선 그래프
# df_grp = df.groupby('개봉 연도').mean()
# # plt.plot(df_grp['평점'])  ## 개봉 연도 자체가 인덱스화 됨 

# # ## 4) 꺾은선 그래프에 세부사항 적용 마커: o , x축 눈금 5년단위 y축 범위 7~10
# plt.plot(df_grp['평점'], marker= 'o')
# plt.xticks([2000+(i*5) for i in range(1,5)])
# plt.ylim((7,10))  ## not (7,11)
# plt.show()

## 5) 평점 9 이상 영화 비율 원그래프 / 세부사항 label 9점 이상/ 미만 , 퍼센트 : 소수첫째 자리 , 범례 그래프 우측

# filt = df['평점'] >= 9.0
# # # vals = [df.groupby(filt).size()[0], df.groupby(filt).size()[1]]
# # vals = [len(df[~filt]), len(df[filt])]  ## 좀더 편리
# labels = ['9점 미만','9점 이상']
# plt.pie(vals,labels=labels, autopct='%.1f')
# plt.legend(loc=(1.0,0.5))
# plt.show()
