# Methodology

## TODO

Define recall and precision?  Maybe very briefly if space needed.

Explain why Naive Bayes is good at precision and recall but shit at AUC.

## Discretization

Explain.

## Cross-Year Analysis

Our analysis method, regardless of underlying implementation, is at its core to be an aid in analyzing shifts in Canada's changing language demographics.

To explore the usefulness of our method, we extracted feature importance scores from both the 1991 and 2016 PUMF datasets in order to compare meaningful differences and similarities.  The choice of 1991 echoes our choice of 2016 as the two years were the earliest and latest census years respectively available in individuals file (PUMF) format.  Together the two years allow an analysis of demographic changes over a 25 year period, close to the definition length of one human generation (SOURCE).  

In order to reconcile the differences in feature name and representation types, we used the associated study documentation files for each census year to produce a mapping of similar features.  Although features were not necessarily one to one (e.g. NAME A FEATURE WHERE THIS IS NOT THE CASE), features mapped were sufficiently similar such that a discrepancy in relative feature importance scores between the two census years might be an indicator of some underlying difference.

In some features, such as AGEGRP/AGEP, the feature tracked the same aspect of individuals but with finer granularity in one year and loose categories in the other.  As our underlying algorithms are suited to categorical rather than continuous data, such differences were reconciled by bucketing granular data into deciles.

Other features were not reconcilable, as they did not possess tracked counterparts in the other census year or were split into multiple features, such as SHELCO (EXPLAIN WHY).  Such features were omitted from both census years in the cross-year analysis.

Although in practice either of the three algorithms analyzed might be applicable for cross-year analysis, we opted to use random forest due to its better performance metrics from the 2016 trials and its ease of interpretability compared to naive Bayesian.  Unlike in the 2016 trials, no non-offical home language (VERIFY THAT THIS IS WHAT WAS DROPPED) rows were not dropped, as the 1991 dataset provided additional granularity by differentiating "English single response", "French single response", and "English and French" responses.  By retaining these rows, additional language shifts between the official languages, of which we intuit might be more numerous due to the prevalence of official language speakers.

Post pre-processing, general methodology between the cross and single year experiments were identical save for differences in feature names.  In the 1991 dataset, WEIGHT, HLANO, MTNNO correspond to WEIGHTP, HLNP, and MTNP respectively.

The results of the feature importance scores for 1991 and 2016 were then compared in terms of cardinality, with first features corresponding to the highest scores, second features corresponding to the second highest scores, and so forth.  The results revealed similar orderings of features importance scores between the two census years, bar some potentially interesting differences as seen in NAME THE FIGURE WITH THE CROSS YEAR TABLE. 

# Analysis Findings

* http://www.davidsbatista.net/blog/2018/08/19/NLP_Metrics/
* https://stats.stackexchange.com/questions/41537/regarding-precision-and-recall-for-the-highly-unbalanced-validation-data-set
* https://blog.floydhub.com/a-pirates-guide-to-accuracy-precision-recall-and-other-scores/


# Feature Findings

Idea: Do a table exploration and just count trues/falses for certain columns

It will be neat to gain some insights and to find related work/corroborating studies and articles

Goal is not to show any conclusions, but to show that our methods can be used for analysis in the field of studying language shifts!

## 2016 Only Notes

Via Katie:

```
in analysis:
a comparison of langShift== true/langShift==False and ages of respondents [ theory: more young respondents in our data, leaving less time for language shift to occur, leaving imbalance in data towards languageShift == False]
a comparison of genstat and langShift [ theory: more genstat ==1 (ie. first gen immigrants) in sample, means more langshift == false]
```

Analyze generation status and age of immigration and age in general

Language shift correlates with many fields which correlate with wealth!
* E.g. Highest_Education_Location_vs_Residence

Immigration status and Aboriginal status matter little, but immigrant generation, group, Aboriginal group, etc. matter much more; this may be due to the dropping of certain fields, which was done in the plain 2016 but not the comparisons

Mother's place of birth matters much more than father's

## Over Time Comparison Notes

Canadian citizenship status matters much more in 1991

Property value matter much more in 2016

Highest degree and secondary degree matters more in 2016, while highest attended matters more in 1991

Field of study matters much more in 2016
