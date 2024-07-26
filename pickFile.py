import os, random

if os.path.exists("IdontWant.txt") is False:
    open("IdontWant.txt", "x")
if os.path.exists("Watched.txt") is False:
    open("Watched.txt", "x")

movies_list = os.\
  popen("ls /home/homayoon/other_things/11t_homa/Other_things").read().split("\n")
#print(random.choice(movies_list))

while(Picked):
    movie_name = random.choice.(movies_list)
    print(movie_name)
    if 

