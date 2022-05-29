### Matplotlib

# 1. 그래프 기본

from cProfile import label
from turtle import color
from matplotlib import markers
from matplotlib.lines import *


import matplotlib.pyplot as plt 
# pip install matplot

# 한글 폰트 추가 line19
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
# 마이너스 기호 해결 line 23
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1,2,3]
y = [2,4,8]
# plt.plot(x,y)

# # 그래프 타이틀 설정
# plt.title("Line Graph 꺾은선 그래프") # 한글 인코딩 실패 (폰트가 없음)
# # plt.show()

# plt.plot([-1,0,1],[-5,-1,2]) ## minus 기호가 짤림(한글폰트 사용시)
# plt.show()


## 2. 축

# plt.xlabel('x축') # color 옵션으로 색상조절  ex) red or rgb value(#00aa00) / loc 옵션으로 위치 조절 (left center right , top center bottom)
# plt.ylabel('y축')

# # 축 간격 조절
# plt.xticks([1,2,3])
# plt.yticks([3,6,9,12])
# plt.show()


## 3. 범례(legend)

# plt.plot(x,y,label='데이터')
# plt.legend() # loc 옵션 upper/lower + right/left 등등 여러 옵션이 있음 tuple로 좌표 넘겨도됨
# plt.show() 


## 4. 스타일
# 시각화 스타일 하는법


#plt.plot(x,y ,linewidth = 10) # 라인두께
# plt.plot(x,y , marker = 'x', markersize(ms 같은 축약어 존재)=10 , linestyle(or ls)= 'None') # 데이터 마커 / 다양한 마커와 라인스타일 적용가능
# plt.plot(x,y, marker='o',markeredgecolor(or mec)='red', markerfacecolor(or mfc)='yellow') # 색상 적용
# plt.plot(x,y, color='pink') # 라인 색상 
# plt.plot(x,y ,'ro--') # 포멧으로 한번에 넘김 (컬러,마커,라인스타일)
# plt.plot(x,y , alpha=0.7) # 투명도
# plt.figure(figsize=(10, 5) , dpi=200) # 투명도 / 해상도
# plt.figure(facecolor='yellow') # 그래프 배경색
# plt.plot(x,y)
# plt.show()


## 5. 파일로 저장

# plt.plot(x,y)
# plt.savefig('graph.png',dpi=100) # figure에서 조정한 dpi는 화면에 보이는 해상도 이고 savefig에서 정의한 dpi는 저장할 파일의 dpi가 됨


## 6. 그래프 텍스트
# plt.plot(x,y, marker ='o')
# for idx, txt in enumerate(y):
#     plt.text(x[idx], y[idx]+0.3, txt, ha='center') ## 같은 좌표에 찍으면 텍스트가 잘안보임 + ha 속성(정렬)으로 x 좌표 어긋나는것도 맞춰주기 가능 + color도 가능
# plt.show()


## 7. 다수의 데이터
# days=[1,2,3]
# az=[2,4,8] #(단위 만명)
# pfizer=[5,3,1]
# moderna = [1,3,5]
# plt.plot(days,az , label='az')
# plt.plot(days,pfizer, label='pfizer')
# plt.plot(days,moderna, label='moderna')
# plt.legend(ncol=3) # 범례 칼럼수 옵션조정 가능
# plt.show()


## 8-9. 막대 그래프(bar chart)

labels= ['강백호', '서태웅', '정대만']
values =[190, 185, 177]
# colors =['r','g','b']
# bar = plt.bar(labels, values, color=['r','g','b'], width=0.5) 
# # color를 막대마다 적용가능 , 투명도 

# plt.ylim(175,195) # 축 변경
# # plt.xticks(rotation=45)
# plt.yticks(rotation=45) # 글자 회전 
# ticks = ['1번', '2번', '3번']
# plt.xticks(labels ,ticks) # 익명화 가능 
# plt.show()

barh =plt.barh(labels, values) # x,y 반전 
plt.xlim(175,195)

# barh[0].set_hatch('/')
# barh[1].set_hatch('X')
# barh[2].set_hatch('..')  ## 막대 패턴(다양한 패턴이 있음) 

# # 막대에 텍스트 넣기
# for idx, rect in enumerate(bar):
#     plt.text(idx, rect.get_height()+0.3, values[idx],ha='center',color='b')
# plt.show()

## x,y 반전이라 사각형 끝값을 먼저 넣어야함
# for idx, rect in enumerate(barh):
#     plt.text( rect.get_width()+0.5 , idx , values[idx],va='center',color='b')
# plt.show()