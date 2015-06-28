[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

##### Create class DiffMeansResample inheriting from DiffMeansPermute
    import hypothesis
    import thinkstats2
    import numpy as np
    import nsfg
    import first

    class DiffMeansResample(hypothesis.DiffMeansPermute):
        
        def RunModel(self):
            """Run the model of the null hypothesis.
            
            returns random sample from distribution with same length
            """
            group1,group2 = data
            data = thinkstats2.Resample(group1),thinkstats2.Resample(group2)
            return data

##### Read NSFG data and separate into groups by first and other births
    live, first, others = first.MakeFrames()

##### Test difference in pregnancy length between first babies and others
    data = first.prglngth.values, others.prglngth.values
    ht = hypothesis.DiffMeansResample(data)
    pvalue_lngth = ht.PValue()

##### Test difference in birth weight between first babies and others
    data = first.totalwgt_lb.values, others.totalwgt_lb.values
    ht = hypothesis.DiffMeansResample(data)
    pvalue_weight = ht.PValue()
            
##### Print results
    print('P-value for pregnancy length: ',pvalue_lngth)
    print('P-value for birth weight: ',pvalue_weight)

According to the results, the p-value for the difference in lengths is not statistically significant (at 0.5), while the p-value for the difference in birth weight is statistically significant (at 0.0). 