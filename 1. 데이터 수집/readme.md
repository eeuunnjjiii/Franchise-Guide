# Data
정보공개서 데이터 수집
- 출처 : 공정거래위원회 가맹사업거래 홈페이지 (https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do)
- '가맹희망플러스' 탭에서 업종 '외식' 데이터 전부 수집 (2016년-2020년)

1. growth

|Feature|Type|
|------|---|
|상호|string|
|자산|string|
|매출액|string|
|영업이익|string|
|총자산증가율|string|
|매출액증가율|string|
|영업이익증가율|string|
|업종|string|
|기준년도|int|

2. stability

|Feature|Type|
|------|---|
|상호|string|
|자산|string|
|자본|string|
|부채|string|
|부채비율(부채/자본)|string|
|자기자본비율(자본/자산)|string|
|법위반횟수(최근3년)|int|
|업종|string|
|기준년도|int|

3. profit

|Feature|Type|
|------|---|
|상호|string|
|자산|string|
|매출액|string|
|영업이익|string|
|당기순이익|string|
|영업이익률(영업이익/매출액)|float|
|매출액순이익률(당기순이익/매출액)|float|
|자기자본순이익률(당기순이익/자본)|float|
|업종|string|
|기준년도|int|

4. overview

|Feature|Type|
|------|---|
|브랜드|string|
|상호|string|
|가맹사업 개시일|string|
|가맹사업 년수|string|
|가맹점수|int|
|가맹본부 임직원수|string|
|업종|string|
|기준년도|int|

5. info

|Feature|Type|
|------|---|
|브랜드|string|
|상호|string|
|가맹점수|int|
|신규개점|int|
|계약종료|int|
|계약해지|int|
|명의변경|int|
|계약해지|int|
|가맹점평균매출액(매출액지수)|string|
|가맹점면적(3.3㎡)당평균매출액(평균매출액지수)|string|
|업종|string|
|기준년도|int|

6. cost

|Feature|Type|
|------|---|
|브랜드|string|
|상호|string|
|가입비(가맹비)|string|
|교육비|string|
|보증금|string|
|기타비용(인테리어비용포함)|string|
|합계(창업비용지수)|string|
|인테리어비용(면적당(3.3㎡)비용)|string|
|인테리어비용(기준면적(㎡))|string|
|인테리어비용(총 비용)|string|
|업종|string|
|기준년도|int|
