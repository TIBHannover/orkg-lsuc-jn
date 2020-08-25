Iron-regulatory proteins secure iron availability in cardiomyocytes to prevent heart failure
=======================

Saba Haddad, Yong Wang, Bruno Galy, Mortimer Korf-Klingebiel, Valentin Hirsch, Abdul M. Baru, [![iD](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-0992-6227) Fatemeh Rostami, Marc R. Reboll, Jörg Heineke, Ulrich Flögel, Stephanie Groos, André Renner, Karl Toischer, Fabian Zimmermann, Stefan Engeli, Jens Jordan, Johann Bauersachs, Matthias W. Hentze, Kai C. Wollert, Tibor Kempf

*European Heart Journal*, Volume 38, Issue 5, 1 February 2017, Pages 362–372, [https://doi.org/10.1093/eurheartj/ehw333](https://doi.org/10.1093/eurheartj/ehw333)

## Results
---

### Reduced iron content, IRE binding activity, and transferrin receptor expression in the failing human heart

import math
import numpy as np
import pandas as pd
from myst_nb import glue
from scipy.stats import ttest_ind
from matplotlib import pyplot as plt

labels = ['non-failing heart (NF)', 'failing heart (F)']
data = [(99, 52), (96, 40), (100, 38), (105, 18), 
        (np.nan, 11), (np.nan, 5), (np.nan, 42), 
        (np.nan, 55), (np.nan, 53), (np.nan, 39),
        (np.nan, 42), (np.nan, 50)]

df = pd.DataFrame.from_records(data, columns=labels)
tt = ttest_ind(df['non-failing heart (NF)'], 
               df['failing heart (F)'], 
               equal_var=False, nan_policy='omit')

pvalue = tt.pvalue

glue('pvalue', math.ceil(pvalue * 1000.0) / 1000.0)

Consistent with previous reports {cite}`maeder2011,leszek2012` iron concentration was significantly lower in LV tissue samples from patients with advanced heart failure than in LV tissue samples from unused donor hearts. As shown by electrophoretic mobility shift assays, IRE binding activity was significantly (*p* < {glue:}`pvalue`) reduced in failing hearts (most pronounced in patients with ischemic cardiomyopathy) ({ref}`Figure 1<fig1>`). Protein expression levels of the transferrin receptor were significantly lower in failing hearts than in the controls. 

fig, ax = plt.subplots()

d = df.to_numpy()
f = [d[m] for d, m in zip(d.T, ~np.isnan(d).T)]

ax.boxplot(f)
ax.set_ylim([0, 150])
ax.set_ylabel('IRE binding activity (%)', fontsize=14)
ax.set_xticklabels(['NF', 'F'])
ax.tick_params(axis='x', labelsize=14, labelrotation=45)
ax.tick_params(axis='y', labelsize=14)

glue('fig1', fig)

```{glue:figure} fig1
:figwidth: 800px
:name: fig1

IRE binding activity for non-failing (NF) and failing (F) hearts.
```

## References

```{bibliography} references.bib
:filter: docname in docnames
```