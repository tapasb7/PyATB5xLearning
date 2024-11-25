#tuples are non-mutable
from idlelib.squeezer import count_lines_with_wrapping

hero_1 = ("BatMan", "Bruce Wayne")
hero_2 = ("Wonder-Woman", "Diana Prince")
hero_3 = ("Super-Man", "Clerk Kent")

new_tuple = (hero_1, hero_2, hero_3)
print(hero_1)
print(hero_2)
print(new_tuple)

print(new_tuple[2][1])

#convert tuple to list
new_tuple = list(new_tuple)
print(new_tuple)
print(len(new_tuple))