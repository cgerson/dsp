[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

'''
###### Code to find Cohen statistic between weight of first babies and others

###### First import packages necessary for manipulating data and calculations
import math
import thinkstats2
import thinkplot
import nsfg

###### Read data and clean
df = nsfg.ReadFemPreg()
nsfg.CleanFemPreg(df)

###### Subset data with only live births
live = df[df.outcome==1]

###### Divide data into two groups by birth order: first births and other births
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

###### Define function to calculate Cohen statistic
def CohenEffectSize(group1,group2):
    diff=group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1,n2 = len(group1),len(group2)
    pooled_var = (n1*var1 + n2*var2)/(n1+n2)
    d = diff / math.sqrt(pooled_var)
    return d

###### Calculate Cohen statistic for the two birth order groups
Cohen_first = CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb)
'''

####### Results 
The Cohen statistic to describe difference in weight of first babies vs others is -.089, whereas the Cohen statistic of difference in pregnancy length between first and other babies came to .029.

In conclusion, first babies weigh slightly less than other babies, while they are slightly longer than others.
