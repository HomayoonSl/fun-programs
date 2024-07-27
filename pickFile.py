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
    with open("IdontWant.txt", "r+") as idw, open("Watched.txt", "r+") as watched:
        movie_name = random.choice(movies_list)
        #print(movie_name)
        idontwant_content = list(l1.strip() for l1 in idw)
        watched_content = list(l2.strip() for l2 in watched)
        #print(idontwant_content)
        if movie_name in (idontwant_content or watched_content):
           # print("first")
            Picked = False
        else:
            print(f"Do you want to watch {movie_name}? [y/n]")
            ans = input()
            if ans == "y":
                watched.write(movie_name + '\n')
            else:
                idw.write(movie_name + '\n')

            Picked = True


