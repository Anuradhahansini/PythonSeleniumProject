#Number -Integer,Float,ComplexNumber

print("#-Integer")
a=10
print(a)
b=-112
print(type(a))

print("#-Float")
f1=12.4
print(f1)

print("#-ComplexNumber")
com=12+2j
print(com)


print("#-dictionary") #we can get values in one ane one / both
dic={1:"Hello",2:"welcome"}
print(dic[1])

print("#-boolean") #true/False
boo=True
print(boo)
print("#-Set") #-duplicate
set1=set("Hello")
print(set1)

#Sequence,Strings,List,Tuple

print("#-Strings")
#len,Lower,Upper,Concat,find,replace,split,join
srt1="This is a first code"
srt2='This is a Second code'
srt3='''This is a third code
      "This is fourth line'''

print(srt1)# request line
print(srt1.upper())
print(len(srt1))
print(srt1+ srt2) #concat = two or more line collect in one line
print(srt1.find("a"))
print(srt1.replace("a","b"))
print('#'.join(srt1))
print(srt1.split("a"))




print("#-List")
#append,insert,index,remove,sort,reverse,pop,slices,extend
list1=[1,2,3,4,5] # මුලින්ම list1 නමින් list එකක් සාදනවා
print(len(list1))
list1.append(6) #append() method එකෙන් කරන්නේ list එකේ අගටම අලුත් අගයක් එකතු කරන එකයි.
print(list1)
list1.insert(2,3)  #insert(2, 3) කිරීම: අවසානයේ, list1.insert(2, 3) ක්‍රියාත්මක වෙනවා. insert() method එක වැඩ කරන්නේ මෙහෙමයි: list.insert(index, object).

මෙයින් object එක (එනම්, අංක 3), ලබා දී ඇති index එකට (එනම්, ස්ථාන අංක 2 ට) ඇතුළත් කරනවා.

එම ස්ථානයේ (index 2 හි) තිබූ අගය සහ ඉන් පසුව තිබූ සියලුම අගයන් එක ස්ථානයක් දකුණට යනවා.

Insert කිරීමට පෙර List එක: [1, 2, 3, 4, 5, 6]

Insert කළ පසු List එක: [1, 2, **3**, 3, 4, 5, 6]


























































print(list1)
print(list1.index(4))


print("#-Tuple")

