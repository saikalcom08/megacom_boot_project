# SET множества
# a = set()
# print(type(a))
# a = {"a", "4", 3, 5, 5, 3, "a"}
# print(a)
#========================================
# a = [12, 33, 44, 5, 44, 6, 6, 89]
# print(a)
# s = set(a)
# a = list(s)
# print(a)
# #=========================================
# ADD SET
# a = set()
# a.add(4)
# print(dir(a))
#============================================
# UNION SET
set1 = {1, 2, 3, 5, 6, 6}
set2 = {"a", "df", "c"}
#a = set1.union(set2) #this just unions 2 sets
#print(a)
# set1.update(set2) # this updates the set which was pointed before the update
# print(set1)
# print(set2)
#===========================================
# POP SET
# a = set1.pop()
# print(set1)
# print(a)
#===========================================
# ISDISJOINT
# print(set1.isdisjoint(set2)) #Two sets are said to be disjoint sets if they have no common elements
#==========================================
# COPY SET
# set1 = {1, 2, 3, 5, 6, 6}
# a = set1.copy()
# print("set1:", set1)
# print("seta:", a)
#==========================================
#INTERSECTION
set1 = {1, 2, 3, "a", "a",  5, 6, 6}
set2 = {"a", "df", "c", 3, 3}
#set1.intersection(set2) #method returns a new set with elements that are common to all sets.
#print(set1)
#set1.intersection_update(set2) #updates the set calling intersection_update() method with the intersection of sets.
#print(set1)
#========================================
#REMOVE SET
# set1.remove(3)
# set1.remove(5)
# print(set1)
#========================================
# SYMMETRIC DIFFERENCE
# print(set1.symmetric_difference(set2))
#=======================================
set1 = {1, 2, 3, 6}
set2 = {2, 3, 5, 1}
# set2.symmetric_difference_update(set1)
# print(set2)
#========================================
#DIFFERENCE
# print(set1.difference(set2))
# print(set2.difference(set1))
#
# print(set1.difference_update(set2))
#========================================
# FROZENSET
# a = frozenset()

# a = frozenset({1, 3, 5, 7})
# print(type(a))

#==========================================
a = [[12, 3], ["a", True]]
# print(a[1][1])
# for i in a:
#     #print(i)
#     for j in i:
#         print(j)
#=========================================