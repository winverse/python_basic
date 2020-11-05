# import pickle

# with open("./files/profile.pickle", "rb") as profile_file:
#   print(pickle.load(profile_file))
  
# with open('./files/study.txt', 'w', encoding="utf8") as study_file:
#   study_file.write("파이썬을 공부하고 있습니다.")

with open("./files/study.txt", "r", encoding="utf8") as study_file:
  print(study_file.read())