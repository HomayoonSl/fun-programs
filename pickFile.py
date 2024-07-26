import os, random

if os.path.exists("IdontWant.txt") is False:
    open("IdontWant.txt", "x")
if os.path.exists("Watched.txt") is False:
    open("Watched.txt", "x")

movies_list = os.\
  popen("ls").read().split("\n")
#print(random.choice(movies_list))
Picked = False
while(Picked == False):
    movie_name = random.choice(movies_list)
    #print(movie_name)
    with open("IdontWant.txt", "r") as idw, open("Watched.txt", "r") as watched:
        idontwant_content = set(line.strip() for line in idw)
        watched_content = set(line.strip() for line in watched)
    if movie_name in idontwant_content or watched_content:
        Picked = False
    else:
        print(movie_name)
        Picked = True


