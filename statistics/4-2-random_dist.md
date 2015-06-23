[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

###### Import Numpy, Pandas, Thinkstats2 and Thinkplot
    import numpy as np
    import pandas
    import thinkstats2

###### Generate 1000 random numbers
    sample = np.random.random(1000)

###### Create PMF and CDF distributions of the sample
    pmf = thinkstats2.Pmf(sample)
    cdf = thinkstats2.Cdf(sample)

###### In pmf, you can see that every number has prob of .001
    print pmf

###### In cdf, you can see that the cumulative prob increases by .001 for each number
    print cdf

###### Plot step function of each distribution
    thinkplot.Pmf(pmf)
    thinkplot.Show(xlabel='numbers',ylabel='probability')

    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel='numbers',ylabel='CDF')

###### Pmf graph shows equal probability for every number
<img src = "files/Images/Ex4-2_figure_1.png">

###### Cdf graph shows a linear line with slope 1
<img src = "files/Images/Ex4-2_figure_2.png">
