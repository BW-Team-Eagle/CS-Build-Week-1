from django.contrib.auth.models import User
from adventure.models import Player, Room

r_grass = Room(title="Block of grass", description="Just a grass block")
r_grass1 = Room(title="Block of grass", description="Just another grass block")
r_grass2 = Room(title="Block of grass", description="Just YET a grass block")
r_grass3 = Room(title="Block of grass", description="Just a grass block")
r_grass4 = Room(title="Block of grass", description="Just a grass block")
r_grass5 = Room(title="Block of grass", description="Just a grass block, again you grow tired of grass blocks")

plzwork = [r_grass, r_grass1, r_grass2, r_grass3, r_grass4, r_grass5]

for x in plzwork:
    x.save()

