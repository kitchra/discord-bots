yurious_bois = {
    "Mr. Mad": 2,
    "Miss Fury": 5,
    "WHO DUN IT": 200,
}

msg = "TESTING \n\n"

max_fury = 0
yurious = "Nobody"

for boi,count in yurious_bois.items():
    if count > max_fury:
        yurious = boi
    msg += "```{name:<20}: {num:<5}```\n".format(name=boi, num=count)

if count==0:
    msg += "Nobody's yurious? Lame :(\n"
else:
    msg += "MOST YURIOUS: {}!".format(yurious)

    
print(msg)