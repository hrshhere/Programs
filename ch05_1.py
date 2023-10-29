
#-----------How append works-----------------------(adds the element at the end of the list)



'''

xyz = ["abc","bac","cbac","dabc","ebc"]

yz = ["def","ghi","fed"]

for a in yz:

    xyz.append(a)

print(xyz)


'''



#---------------HoW clear works--------------------(removes all the elements from the list)

'''

xyz = ["abc","bac","cbac","dabc","ebc"]

xyz.clear()

print(xyz)



'''



#----------------How copy works-----------------------(returns a copy of the list)



'''


xyz = ["abc","bac","cbac","dabc","ebc"]
yz = xyz.copy()


print(yz)




'''




#--------------How count works-----------------(returns the number of elements with thw specified value)



'''


xyz = ["abc","bac","cbac","dabc","ebc"]

a = xyz.count("bac")

print(a)



'''



#------------How extend works-----------(add the elements of a list [or any iterable] to the end of the current list)



'''

xyz = ["abc","bac","cbac","dabc","ebc"]
yz = ["efg","hij","klm"]

xyz.extend(yz) 

print(xyz)



'''




#-----------How works index----------(return the index of the first element with the specified value)



'''


plyrs = ["Kohli","Rohit","Hardik","Chahal","Yuvi"]

p = plyrs.index("Yuvi")

print(p)



'''



#----------How insert works----------(Adds an element at the specified position)



'''

bbq = ["choclate","stroberry","pista","american"]

bbq.insert(2,"nuts")

print(bbq)



'''


#---------How pop works---------(Removes the element at the specified position)



'''


games = ["cricket","football","hockey","basketball","kabadi"]

games.pop(3)

print(games)



'''


#----------How remove works--------(Remove the item with the specified values)



'''



sides = ["left","right","up","down"]

sides.remove("right")

print(sides)




'''




#---------How reverse works-------(Reverse the order of the list)




'''


speaker = ["jbl","boat","zebronics","noise","firebolt"]

speaker.reverse()

print(speaker)



'''


#--------How sort works------(sort the list)



'''


penclr = ["red","blue","black","green"]

penclr.sort()

print(penclr)



'''

