# Refering dictionary in question 3 add an item to this dict dictionary, and also delete the same item added to the dictionary.
d1={'name':"John",'age':30,'city':"delhi",'country':"India"}
a1=d1.copy()
print(a1)
print(len(d1))
d1.popitem()
print(d1)
print(len(d1))
del d1
# print(d1)
print()

l1={'key':'python'}
l2={'key1':{'key2':'python'}}
l3={'key1' : [{'nest_key':["let's learn",['python']]}]}

print(l1['key'])
# lll2.values([0,2]
print(l2['key1']['key2'])
print(l3['key1'][0]['nest_key'][1][0])