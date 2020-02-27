'''
문제 3-1

2015년 9월 초의 네이버 종가는 표 3.2와 같습니다. 09/07의 종가를 리스트의
첫 번째 항목으로 입력해서 naver_closing_price라는 이름의 리스트를 만들어보세요.

표 3.2 네이버 종가

날짜	요일	종가
09/11	금	488,500
09/10	목	500,500
09/09	수	501,000
09/08	화	461,500
09/07	월	474,500
'''

naver_closing_price = [488500, 500500, 501000, 461500, 474500]
print(naver_closing_price)

'''
문제 3-4

문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에서
가장 종가가 높았던 요일과 가장 종가가 낮았던 요일의 가격 차를 화면에 출력하세요.
'''

dif = max(naver_closing_price) - min(naver_closing_price)
print("가장 종가가 높았던 요일과 가장 종가가 낮았던 요일의 가격 차는", dif)

'''
문제 3-5

문제 3-1에서 만든 naver_closing_price를 이용해
수요일의 종가를 화면에 출력하세요.
'''

print("수요일의 종가는", naver_closing_price[2])
