names= ["윤나은","김현주","장현지","이지선","박선주"]


#문자열 비교
# 알파벳 순서상 뒤로 갈수록 크다.
# 첫 번째 문자가 같다면 두번째 문자를 비교한다.
# 비교하는 문자들이 모두 같다면, 하나라도 긴 문자열이 크다.
# 소문자가 대문자보다 크다.

#가나다순으로 뒤로 갈수록 크다
# 아야어여오요우유으이 순으로 뒤로 갈수록 크다.
# 첫 번째 문자가 같다면 두 번째 문자를 비교한다.
# 비교하는 문자들이 모두 같다면 하나라도 긴 문자열이 크다.

names.sort()


dnames = {}
i = 1

for n in names:
    dnames[i] = n 
    i += 1

##print(dnames)

#enumerate -> 정렬 번호와 정보를 튜플로 반환 
names= ["윤나은","김현주","장현지","이지선","박선주"]
names.sort()


dnames = { k:v for k,v in enumerate(names,1)}

print(dnames)