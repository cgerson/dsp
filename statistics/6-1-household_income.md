[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

##### Import packages
    import hinc
    import hinc2
    import thinkstats2
    
##### Read data 
    df = hinc.ReadData()

##### Generate pseudo-sample to yield same number of respondents in each range as the actual data
    df_sample = hinc2.InterpolateSample(df)
    
##### Compute size (number of elements) of dataframe. Yields 122458
    print "Size: "+ str(df_sample.size)

##### Compute median. Yields 4.71
    print "Median: " + str(np.around(df_sample[122458/2],2))
    
##### Compute mean. Yields 4.66
##### Mean is less than median, indicating a left-skewed distribution
    print "Mean: " + str(np.around(df_sample.mean(),2))
    
##### Compute skewness measure. Yields -0.64
##### Negative value indicates left-skewed distribution
    print "Skewness measure: " + str(np.around(thinkstats2.Skewness(df_sample),2))

##### Compute Pearson Median Skewness. Yields -0.34
##### Negative value confirms left-skewed distribution
    print "Pearson Median Skewness coefficient: " + str(np.around(thinkstats2.PearsonMedianSkewness(df_sample),2))
    
##### Fraction of households below the mean: 45%
    cdf = thinkstats2.Cdf(df_sample)
    print "Fraction of households below the mean:" + str(np.around(cdf[df_sample.mean()],2))

##### Conclusion:
Assumed upper-bound is positively correlated with the mean, skewness measure, and Pearon Median Skewness coefficient. Median remains constant. 
