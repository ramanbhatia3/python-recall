# Set

marvel_heroes = {"Ironman","Spiderman","Hulk","Ryan"}

dc_heroes = {"Batman","Superman","Flash","Ryan"}

heroes = marvel_heroes | dc_heroes

print(f"All Heroes: {heroes}")

common_heroes = marvel_heroes & dc_heroes

print(f"Common Heroes: {common_heroes}")

only_marvel_heroes = marvel_heroes - dc_heroes

print(f"Only Marvel Heroes: {only_marvel_heroes}")



# membership testing

print(f"Is Batman a Marvel Hero? {'Batman' in marvel_heroes}")