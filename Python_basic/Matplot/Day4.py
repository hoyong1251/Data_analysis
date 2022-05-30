## Dataframe 활용

from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt 
# pip install matplot

# 한글 폰트 추가 line19
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
# 마이너스 기호 해결 line 23
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('score.xlsx')
# # print(df)
# # plt.plot(df['지원 번호'], df['키'])
# plt.plot(df['지원 번호'], df['영어'],label='영어')
# plt.plot(df['지원 번호'], df['수학'],label='수학')
# plt.legend()
# plt.grid(axis='y') ## 격자 생성 axis 옵션으로 선택가능
# 그리드 라인도 라인스타일 적용가능
# plt.show()


## 누적막대 그래프

# plt.bar(df['이름'], df['국어'],label='국어')
# plt.bar(df['이름'], df['영어'], bottom=df['국어'],label='영어')
# plt.bar(df['이름'], df['수학'], bottom=df['국어']+df['영어'],label='수학')
# ## 단순히 밑에 두고 쌓아올린것
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()


## 다중 막대 그래프

# numpy 기능활용 / 리스트와 비슷한 배열을 만들고 연산이 가능하게 해줌
# import numpy as np
# N = df.shape[0] ## (row , col)
# index =np.arange(N)
# index = [i for i in range(N)] ## list + int(float) 의 연산이 불가능함
# ## bar로 그릴때 x축 값을 이동시키면서 막대를 찍으면됨
# w = 0.25
# plt.bar(index-w, df['국어'],label='국어', width=w)
# plt.bar(index, df['영어'],label='영어', width=w)
# plt.bar(index+w, df['수학'],label='수학', width=w)
# plt.xticks(index, df['이름'], rotation=45)
# plt.legend()
# plt.show()


## 원 그래프 (비율을 나타낼때 주로사용) pie chart

# values = [30,25,20,13,10,2]
# labels = ['Python','Java','Js', 'C#', 'C++','ETC']
# # plt.pie(values, labels=labels, autopct='%.1f%%',startangle=90, counterclock=False, explode=[0.05]*6)
# # plt.legend(loc=(1.2,0.3), title='언어') ## 범례에도 제목이 생성됨 
# # plt.show()

# colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
# wedgeprops={'width':0.6 , 'edgecolor':'w','linewidth':2}
# # plt.pie(values, labels=labels, autopct='%.1f%%',startangle=90, counterclock=False , colors=colors ,wedgeprops=wedgeprops)

# # def custom_autopct(pct):
# #     return("{:.1f}%".format(pct)) if pct>=10 else ''

# # plt.pie(values, labels=labels, autopct=custom_autopct,startangle=90, counterclock=False , colors=colors ,wedgeprops=wedgeprops, pctdistance=0.7)
# # plt.show()

# group = df.groupby('학교')
# values = [group.size()['북산고'], group.size()['능남고']]
# plt.pie(values,labels=['북산고','능남고'])
# plt.show()


## 산점도 그래프 (두 변량의 상관관계)
# import numpy as np

# df['학년'] = [3,3,2,1,1,3,2,2]
# sizes = np.array(df['학년']) *100


# plt.scatter(df['영어'],df['수학'] ,s=sizes , c=df['학년'], cmap='viridis') ## s 옵션으로 점크기 조절 가능
# plt.xlabel("영어 점수")
# plt.ylabel("수학 점수")
# plt.colorbar(ticks=[1,2,3], label ='학년',shrink=0.3, orientation='horizontal')
# plt.show()


## 여러개 그래프 그리기

# fig , axs = plt.subplots(2,2, figsize=(10,7))
# fig.suptitle('그래프 여러개')

# axs[0,0].bar(df['이름'],df['국어'],label='국어점수')
# axs[0,0].set_title('첫번째 그래프')
# axs[0,0].set(xlabel='이름', ylabel='국어')
# axs[0,0].set_facecolor('lightyellow')
# axs[0,0].grid(linestyle='--', linewidth=2)
# axs[0,0].legend()  ## 하나의 그래프들을 스타일하는 것처럼 할수 있지만 명령어가 조금씩 다름 

# axs[0,1].plot(df['이름'],df['국어'],label='국어점수')
# axs[0,1].set_title('두번째 그래프')
# axs[0,1].set(xlabel='이름', ylabel='국어')
# axs[0,1].legend()

# axs[1,0].barh(df['이름'],df['국어'],label='국어점수')
# axs[1,0].set_title('세번째 그래프')
# axs[1,0].set(xlabel='이름', ylabel='국어')
# axs[1,0].legend()

# axs[1,1].pie(df['국어'], labels=df['이름'])
# axs[1,1].set_title('네번째 그래프')
# axs[1,1].legend(loc=(1.2,-0.3), title='이름')

# plt.show() 
