import pandas as pd

favfruit = pd.Series(['apple', 'banana', 'orange', 'mango'], 
                     index = ["satya", "shivam", "sachin", "satyam"])

print(favfruit)
#output:
# satya     apple
# shivam    banana
# sachin    orange
# satyam    mango

print(favfruit['shivam'])
#output:
#banana