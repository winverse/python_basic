# score_file=open('./files/score.txt', 'w', encoding='utf8'); # 새로 쓰기
# print('수학: 0', file=score_file)
# print('영어: 50', file=score_file)
# score_file.close()

# score_file=open("./files/score.txt", "a", encoding="utf8") # 이어서 쓰기
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100')
# score_file.close()

# score_file = open('./files/score.txt', 'r', encoding='utf8') # 파일 읽기
# print(score_file.read())
# score_file.close()

# score_file = open("./files/score.txt", "r", encoding='utf8')
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 (줄바꿈 포함)
# print(score_file.readline(), end="") # 줄바꿈 제거
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("./files/score.txt", "r", encoding='utf8')
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line, end="")
# score_file.close()

score_file = open("./files/score.txt", "r", encoding='utf8')
lines = score_file.readlines() # list 형태로 저장
for line in lines:
  print(line, end="")
score_file.close()


