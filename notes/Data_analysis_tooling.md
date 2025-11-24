### Data plotting libraries for Python

MATPLOTLIB → the old dog, modeled after matlab, produces static images  
SEABORN → based on Matplotlib, creates nice looking statistical data vz  
PANDAS → also relies on Matplotlib, (and NumPy) mainly focuses on data analysis, also creates static plots  
PLOTLY → Creates interactive visualizations. libraries for R, Javascript, React, Python. Only, even though the plots are interactive, they are NOT real time updated (script needs to be re-run)  
DASHLY → creates interactive dashboards, full web applications lying on a IP address  

Extract an array from a dataset:  
`<arrayname>[:,<colnum>]` for a column  
`<arrayname>[<rownum>;:]` for a row  

To reshape an array as a matrix:  
`<arrayname>.reshape(2,5)` → this will produce a matrix of 2 rows and 5 columns



#### Pandas

It manipulates data structures named SERIES (based on numPy’s N-D arrays)  
When trying to do math on a column values, if failing it might be because the values are not converted into numeric format → do pd.to_numeric(df['normalized-losses'], errors='coerce')  


#### Some useful methods:  
HEAD and TAIL  
NUNIQUE (column’s method, returns the number of unique values)  
DESCRIBE (general info on the df)  
ISNA (or ISNULL: they return the number of missing values -> data.isna().sum()  )  
DTYPES returns the data type for each column  
QUERY extracts data based on a criteria (df.query('value_1 < value_2'))  
SAMPLE returns a random sample of the data  
ISIN allows filtering using lists as criteria  
years = ['2010','2014','2017']  
df[df.year.isin(years)]  
LOC/ILOC selects data based on label (loc) or position (iloc)  
PCT_CHANGE calculates the % change among the elements in a data series  
MELT : this can change the structure of the data, as it can convert wide dataframes to narrow ones  
EXPLODE : in case your data set includes multiple entries of a feature on a single observation (row) but you want to analyze them on separate rows. SUPER!!  
MEMORY_USAGE tells how much memory each column is using   
REPLACE replaces a string with another  
