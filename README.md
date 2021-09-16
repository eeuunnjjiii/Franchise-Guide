# Project | Franchise-Guide

## 1. 프로젝트 개요
제목 : 외식 프랜차이즈 창업 성공 가이드

가맹본부의 도움으로 보다 쉬운 창업을 위해 문을 두드리는 예비 가맹점주들. 하지만 6천개가 넘는 외식 프랜차이즈 브랜드 중 어떤 브랜드를 선택해야 창업에 성공할 수 있을까? 누구나 쉽게 확인할 수 있는 가맹 정보공개서 데이터를 이용해 외식 프랜차이즈 시장 현황을 분석하고 창업 성공 여부를 예측한다.

## 2. 프로젝트 진행 방법
### 1) 데이터 수집
- 공정거래위원회 정보공개서 데이터(2017-2020) selenium으로 크롤링

### 2) 데이터 전처리
- 형변환 등 기본적인 전처리 진행 후 모든 데이터 merge
- 전체 데이터 중 예비창업자가 비교적 쉽게 얻을 수 있는 특성만 데이터로 사용

### 3) 분석 및 시각화
- 기준연도별, 업종별 전체 시각화
- 2020년 평균매출액 Top 5, 신규개점 Top5 데이터 출력

### 4) 모델링
- 15개 업종별 평균 매출액을 기준으로 평균 매출액 이상인 브랜드에는 1, 미만인 브랜드에는 0을 부여하여 분류하는 모델 구축
- Random Forest 모델과 XGBoost 모델을 비교한 뒤, 성능이 더 좋은 XGBoost 모델의 하이퍼파라미터 조정
- 이후 PDP와 SHAP으로 특성 중요도 확인

### 5) 웹 어플리케이션 제작
- 항목별 가맹 본사 정보 조회 및 예측 모델을 담은 웹 어플리케이션을 Flask를 이용해 제작
- 각 데이터는 MySQL에 데이터 베이스를 연결하여 사용했으며, Heroku를 이용해 배포 시도

## 3. 프로젝트 결과
- 최종 선택된 XGBoost 모델의 테스트 데이터(전체 데이터의 20%) 입력시 Accuracy 0.76, ROC-AUC score 0.84

가맹 정보공개서 데이터로 외식 프랜차이즈 브랜드에 대한 최소한의 정보가 주어졌을 때, 브랜드 선택 가이드로 활용할 수 있다.
가장 중요한 특성은 투자비용합계로 확인되었다.

## 4. 프로젝트 개선사항
- 외국계는 포함되지 않은 한계 > 폭 넓은 데이터 수집 (2021.09)
- 브랜드 신뢰도나 인지도 특성이 있다면 브랜드별 가중치 부여 가능할 것으로 기대
- 웹 어플리케이션의 경우 오류로 인해 배포 실패
