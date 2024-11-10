import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 데이터 열 이름 지정
x축 = '미세먼지농도(㎍/㎥)'
y축 = 'sagogunsu'

# 데이터 읽기 (encoding 옵션을 수정하여 한 번에 처리)
sagodata = pd.read_csv("Sagodata.csv", encoding='utf-8-sig', comment='#')
misedata = pd.read_csv("Misedata.csv", encoding='utf-8-sig', comment='#')

# 날짜 열을 datetime 형식으로 변환
sagodata['ilja'] = pd.to_datetime(sagodata['ilja'])
misedata['측정일시'] = pd.to_datetime(misedata['측정일시'])

# ilja와 측정일시 열을 기준으로 병합
merged_data = pd.merge(sagodata, misedata, left_on='ilja', right_on='측정일시')

# 사고건수와 미세먼지농도 간의 상관계수 계산
correlation = merged_data[y축].corr(merged_data[x축])
print(f"상관계수: {correlation}")

# x축과 y축을 반전하여 산점도 생성
plt.scatter(merged_data[x축], merged_data[y축], color='blue')

# 회귀선 추가 (x와 y를 반전하여 계산)
slope, intercept, r_value, p_value, std_err = stats.linregress(merged_data[x축], merged_data[y축])
plt.plot(merged_data[x축], slope * merged_data[x축] + intercept, color='red')

# 라벨과 제목 설정
plt.xlabel("미세먼지농도 (㎍/㎥)")
plt.ylabel("사고건수")
plt.title(f"미세먼지 농도와 사고건수의 관계\n상관계수: {correlation:.2f}")
plt.show()
