'''
이미지가 컴퓨터에 저장될 때에도 디지털 데이터화 되어 저장된다.

가장 기본적인 방법으로는 그림을 구성하는 한 점(pixel, 픽셀)의 색상을
빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 따로 변환하여 저장하는 것인데,

예를 들어 r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면,

한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해서
총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것이다.

그렇게 저장하는 점을 모아 하나의 큰 이미지를 저장할 수 있게 되는데,
1024 * 768 사이즈에 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한
저장 용량을 계산할 수 있다.

이렇게 이미지의 원래(raw) 데이터를 압축하지 않고 그대로 저장하는 대표적인 이미지 파일이
*.bmp 파일이며, 비트로 그림을 구성한다고 하여 비트맵 방식 또는 래스터 방식이라고 한다.

이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.
'''

w, h, b = map(int, input().split())
size = w * h * b / 8 / 1024 / 1024
print("%.2f MB" % size)