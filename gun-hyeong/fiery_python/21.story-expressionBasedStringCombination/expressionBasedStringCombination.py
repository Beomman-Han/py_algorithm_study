#문자열 조합

#편집하듯 하나의 문자열을 구성해 내는 것

# formatting expression
s = "My name is %s" % 'GUN'

print(s)

s = "%(name)s : %(age)d" % {'name' : 'Yoon' , 'age': 23}

print(s)


# %[flags][width][.precision]f
#[flags]   : -또는 0 또는 + 를 넣어서 특별한 신호를 줌
#[width]   : 폭, 어느정도 넓이를 확보하고 출력할지 결정
#[.precision] : 정밀도, 소수 이하 몇째 자리까지 출력할지 결정


s = 'height : %.1f' % 0.1111
print(s)
s = 'height :%7.1f' % 0.1111
print(s)
s = 'height :%07.1f' % 0.1111
print(s)
s = 'height :%+7.1f' % 0.1111 # 부호 추가
print(s)
s = 'height :%+7.1f' % -0.1111 # 부호 추가
print(s)
s = 'height :%-7.1f' % 0.1111 #좌측정렬
print(s)



# formatting method calls

s = "{0} {1} {2}".format(1,2,3)
print(s)
s = "{} {} {}".format(1,2,3)
print(s)

#unpacking

my = ["robot","125","box"]

s = '{} {} {}'.format(*my)
print(s)
s = '{[1]} {} {}'.format(*my)
print(s)
s= '{:f}'.format(0.12)
print(s)
s= '{:.4f}'.format(0.12)
print(s)
s= '{:10.4f}'.format(0.12)
print(s)
s= '{:<10.4f}'.format(0.12)
print(s)
s= '{:>10.4f}'.format(0.12)
print(s)
s= '{:^10.4f}'.format(0.12)
print(s)


s= '{:1^10.4f}'.format(0.12) # :와 ^ 사이에 입력한 문자로 채우기 
print(s)