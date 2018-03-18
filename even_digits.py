
# coding: utf-8

# In[261]:


def even_digit(num):
    n = len(num)
    #print('n: ',n)
    num = int(num)
    diff = 0
    for i in reversed(range(0,n)):
        digit = (num//(10**i))
        if digit % 2 == 1:
            #print (digit%10)
            upper_bound = ((digit%10) + 1)*(10**i)
            #print(upper_bound)
            lower_bound = (digit%10)*(10**i) - (lower_bound_digit(i))
            #print(lower_bound)
            #print('digit',digit)
            if digit%10 == 9:
                digit = num%(10**(i+1))
                diff = digit - lower_bound
            else:
                digit = num%(10**(i+1))
                diff = min(upper_bound - digit,digit - lower_bound)
            #print(diff)
            break
    return diff

def lower_bound_digit(n):
    bound = 1
    for i in reversed(range(n)):
        bound = bound + 10**i
    return bound


# In[265]:



def h():
    a_list = open("/Users/maitraikansal/Downloads/A-large-practice.in").read().strip().split("\n")
    test_cases = a_list.pop(0)
    output_file = open("output_large.txt","w+")
    for i in range(int(test_cases)):
        step_count = even_digit(a_list[i])
        print("Case #%s: %s"%(i+1,step_count))
        if i+1 == 100:
            output_file.write("Case #%s: %s"%(i+1,step_count))
        else:
            output_file.write("Case #%s: %s"%(i+1,step_count)+"\n")
            
if __name__ == '__main__':
    h()


# In[262]:


get_ipython().magic('timeit h(a_list, test_cases)')


# In[256]:




