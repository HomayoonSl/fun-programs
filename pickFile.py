import os, random, re

try:
    open("IdontWant.txt", "x")
    open("Watched.txt", "x")
except:
    pass

movies_list = os.popen("ls -I \"*.txt\"").read().split("\n")
#for i in range(len(movies_list)):
#    movies_list[i] = re.sub(r"[^a-zA-Z0-9 ]", " ", movies_list[i].strip()).lower()


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
            movie_name_re = re.sub(r"[^a-zA-Z0-9 ]", " ", movie_name.strip()).lower()
            print(f"Do you want to watch \"{movie_name_re}\"? [y/n]")
            ans = input()
            if ans == "y":
                watched.write(movie_name + '\n')
            else:
                idw.write(movie_name + '\n')

            Picked = True


