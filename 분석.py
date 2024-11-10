import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 데이터 읽기
sagodata = pd.read_csv("Sagodata.csv", encoding='utf-8-sig', comment='#')
misedata = pd.read_csv("Misedata.csv", encoding='utf-8-sig', comment='#')

# 날짜 열을 datetime 형식으로 변환
sagodata['ilja'] = pd.to_datetime(sagodata['ilja'])
misedata['측정일시'] = pd.to_datetime(misedata['측정일시'])

# ilja와 측정일시 열을 기준으로 병합
merged_data = pd.merge(sagodata, misedata, left_on='ilja', right_on='측정일시')

# 변수 설정
x축 = '초미세먼지농도(㎍/㎥)'  # 독립 변수 (미세먼지 농도)
y축 = 'sagogunsu'  # 종속 변수 (사고건수)

# 사고건수와 미세먼지 농도의 상관계수 계산
correlation = merged_data[x축].corr(merged_data[y축])
print(f"상관계수: {correlation}")

# 선형 회귀 분석 (scipy 사용)
slope, intercept, r_value, p_value, std_err = stats.linregress(merged_data[x축], merged_data[y축])

# 회귀선 함수 정의 (미세먼지 농도 -> 사고건수 예측)
def predict_accidents(dust_concentration):
    return slope * dust_concentration + intercept

# 예시: 미세먼지 농도 50 ㎍/㎥일 때 사고 건수 예측
dust_concentration_input = float(input("미세먼지 농도를 입력하세요 (단위: ㎍/㎥): "))
predicted_accidents = predict_accidents(dust_concentration_input)

print(f"입력한 미세먼지 농도 ({dust_concentration_input} ㎍/㎥)에 대한 예측 사고 건수: {predicted_accidents:.2f}")

# 산점도 및 회귀선 시각화
plt.figure(figsize=(10, 6))

# 산점도 생성 (사고건수 대 미세먼지 농도)
plt.scatter(merged_data[x축], merged_data[y축], color='blue', label='실제값')

# 회귀선 추가
plt.plot(merged_data[x축], slope * merged_data[x축] + intercept, color='red', label='회귀선')

# 제목, 축 레이블 설정
plt.title(f"미세먼지 농도와 사고건수의 관계\n상관계수: {correlation:.2f}")
plt.xlabel('미세먼지 농도 (㎍/㎥)')
plt.ylabel('사고건수')
plt.legend()

# 그래프 출력
plt.show()
