
from konlpy.tag import Okt

okt = Okt()

okt.morphs  # 형태소 분석
okt.nouns  # 명사 분석
okt.phrases  # 구(Phrase) 분석
okt.pos  # 형태소 분석 태깅

# 사용예시
string = {}
print(okt.nouns(u'근처에 빵집 알려줘'))
print(okt.nouns(u'앙버터 파는곳 알려줘'))
print(okt.nouns(u'마카롱 맛집 알려줘'))
print(okt.nouns(u'전망 좋은 식당 찾아줘'))
print(okt.nouns(u'야경 볼 수 있는 장소 알려줘'))
print(okt.nouns(u'부모님이랑 같이 갈 만한 식당 알려줘'))
print(okt.nouns(u'홍대에서 반려동물 출입 가능한 카페 알려줘'))
print(okt.nouns(u'열시 넘어서 하는 미용실 찾아줘'))
print(okt.nouns(u'여기 주위에 핸드폰 액세서리 파는곳 알려줘 '))
print(okt.nouns(u'성수에 편집샵 괜찮은데 알려줘'))
print(okt.nouns(u'주변의 조용한 카페 추천해줘'))
print(okt.nouns(u'주위에 공부하기 좋은 카페 좀 추천해줘'))
print(okt.nouns(u'배고픈데 주변의 맛집 좀 추천해줘 '))
print(okt.nouns(u'급한데 간단하게 먹을 수 있는 곳 좀 추천해줘'))
print(okt.nouns(u'주말에 홍대 갈 건데 홍대 맛집 좀 추천해줘'))
print(okt.nouns(u'건대 주위에 시간 떼울만한 곳 추천해줘'))
print(okt.nouns(u'가족들이랑 갈 맛집 좀 추천해줘 '))
print(okt.nouns(u'지금 시간에 문 여는 주변 술집 좀 추천해줘'))
print(okt.nouns(u'주변에 갈 만한 곳 추천해줘'))
print(okt.nouns(u'주변에 볼링장 추천해줘'))
print(okt.nouns(u'팔보채랑 탕수육 잘하는 집 알려줘'))
print(okt.nouns(u'주변에 매운 음식점 추천해줘'))
print(okt.nouns(u'주변에 영화관 알려줘'))
print(okt.nouns(u'떡볶이랑 오뎅이랑 순대 맛집 알려줘'))
print(okt.nouns(u'근처에 사양좋은 PC방 알려줘'))
print(okt.nouns(u'식사동 근처에 스타벅스 있는지 알려줘'))
print(okt.nouns(u'배고픈데 양많고 싼 음식점 알려줘'))
print(okt.nouns(u'가까운 이비인후과 알려줘'))
print(okt.nouns(u'오늘 볼 수 있는 공연 알려줘'))
print(okt.nouns(u'근처에 연인과 가기 좋은 곳 추천해줘'))
print(okt.nouns(u'밥 먹을곳 추천해줘'))
print(okt.nouns(u'데이트 할 곳 추천해줘'))
print(okt.nouns(u'근처에 한식 추천해줘'))
print(okt.nouns(u'건대(지역명)에 술먹기 괜찮은 곳 알려줘'))
print(okt.nouns(u'사진찍기 좋은 카페 추천해줘'))
print(okt.nouns(u'조용한 카페 추천해줘'))
print(okt.nouns(u'맛집 추천해줘'))
print(okt.nouns(u'쇼핑할 곳 추천해줘'))
print(okt.nouns(u'친구랑 놀만한거 추천해줘'))
print(okt.nouns(u'스트레스 풀 만한곳 추천해줘'))
print(okt.nouns(u'고깃집 좀 추천해줭'))
print(okt.nouns(u'산책하기 좋은 곳 추천해줘'))
print(okt.nouns(u'피자 맛집 추천해줭'))
print(okt.nouns(u'파스타 맛집 추천해줭'))
print(okt.nouns(u'중국집 좀 추천해줭'))
print(okt.nouns(u'공연 볼 만한거 추천해줭'))
print(okt.nouns(u'주변에 카페 추천해줭 '))
print(okt.nouns(u'순대국 집 추천해줭 '))
print(okt.nouns(u'맛집좀'))
print(okt.nouns(u'운동할 곳 추천해줭'))


