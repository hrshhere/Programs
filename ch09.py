# thisdict={
#     "brand": 'Ford',
#     "model": 'Mustang',
#     "year":  '1964'
# }

# print(type(thisdict))



# s1={3,4,5}
# s2=s1.add(1)
# print(s1)


s={30,50,90,10,80}
l=list(s)
su=0
for i in l:
    su+=l.index(i)*i
print(su)