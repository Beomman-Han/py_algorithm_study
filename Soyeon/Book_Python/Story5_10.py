#!/usr/bin/env python
# coding: utf-8

# In[ ]:


######Story05


# In[1]:


ds=[1,2,3,4]
ir=iter(ds)


# In[2]:


next(ir)


# In[3]:


next(ir)


# In[4]:


next(ir)


# In[5]:


next(ir)


# In[6]:


dir([1,2])


# In[7]:


hasattr([1,2],'__iter__')


# In[8]:


for i in [1,2,3]:
    print(i, end = ' ')


# In[9]:


ir = iter([1,2,3])
for i in ir : print(i, end = ' ')


# In[ ]:





# In[ ]:


########Story06


# In[11]:


def func1(n) :
    return n
type(func1)


# In[32]:


def say1():
    print('hello')
def say2():
    print('hi~')
def caller(fct):
    fct()


# In[33]:


caller(say1)


# In[34]:


caller(say2)


# In[35]:


def fct_fac(n):
    def exp(x):
        return x**n
    return exp


# In[37]:


f2=fct_fac(2)
f3=fct_fac(3)


# In[38]:


f2(4)


# In[39]:


f3(4)


# In[40]:


ref=lambda s: print(s)


# In[41]:


ref('hi')


# In[42]:


f2=lambda s: len(s)
f2('simple')


# In[43]:


f3=lambda s: return len(s)
f3('simple')


# In[44]:


f3=lambda : print('yes')
f3()


# In[ ]:





# In[ ]:


############Story07


# In[45]:


def pow(n):
    return n**2


# In[46]:


st1=[1,2,3]
st2=list(map(pow,st1))
st2


# In[48]:


def dbl(e):
    return e*2
list(map(dbl,(1,3,4)))


# In[49]:


list(map(dbl,'hi'))


# In[55]:


def sum(n1,n2):
    return n1+n2
st3=list(map(sum,st1,st2))
st3


# In[56]:


def rev(s):
    return s[ : :-1]
st=['one','two','three']
rst=list(map(rev,st))
rst


# In[57]:


rst2=list(map(lambda s:s[ : :-1],st))
rst2


# In[58]:


def is_odd(n):
    return n%2
st=[1,2,3,4,5]
ost=list(filter(is_odd,st))
ost


# In[59]:


ost2=list(filter(lambda n: n%2,st))
ost2


# In[62]:


st=list(range(1,11))
fst=list(filter(lambda n: not(n%3),st))
fst


# In[63]:


fst2=list(filter(lambda n: not(n%3),map(lambda n: n**2,st)))
fst2


# In[ ]:





# In[ ]:


##############Story08


# In[64]:


st=list(range(1,11))
fst=[n**2 for n in st if n%2]
fst


# In[ ]:





# In[ ]:


############Story09


# In[65]:


def gen_num():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3


# In[66]:


gen=gen_num()


# In[67]:


next(gen)


# In[69]:


next(gen)


# In[70]:


next(gen)


# In[71]:


next(gen)


# In[76]:


def gpows(s):
    for i in s:
        yield i**2
st=gpows(range(1,10))


# In[77]:


for i in st:
    print(i,end=' ')


# In[78]:


import sys
sys.getsizeof(st)


# In[79]:


def get_nums():
    ns=[0,1,0,1,0,1]
    yield from ns
g=get_nums()


# In[80]:


next(g)


# In[81]:


next(g)


# In[82]:


next(g)


# In[83]:


next(g)


# In[84]:


next(g)


# In[85]:


next(g)


# In[86]:


next(g)


# In[ ]:





# In[ ]:


#############Story10


# In[92]:


def show_all(s):
    for i in s:
        print(i,end=' ')
st=[2*i for i in range(1,10)]
show_all(st)


# In[94]:


def times2():
    for i in range(1,10):
        yield 2*i
g=times2()
show_all(g)


# In[96]:


g=(2*i for i in range(1,10))
show_all(g)


# In[98]:


g=(2*i for i in range(1,10))
next(g)


# In[100]:


show_all((2*i for i in range(1,10)))


# In[102]:


show_all(2*i for i in range(1,10))


# In[ ]:




