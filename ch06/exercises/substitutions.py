import json

def main():

  myideasfile = open("news.txt")
  ideas = json.load(myideasfile)
  myideasfile.close()

  idea = input("betternews.txt")
  ideas.append(idea)
  print(ideas)

  #overwrite the entire file with the new data
  myideasfile = open("news.txt", "w")
  json.dump(ideas, myideasfile)

  myideasfile.close()

main()