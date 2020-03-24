import netaddr
import pandas as pd
df = pd.read_csv('ip.csv', skipinitialspace=True)
ipslen = len(df)
cidrslist=[]
for i in range(ipslen):
    startip = df.iloc[i][0]
    #print(startip)
    endip = df.iloc[i][1]
    #print(endip)
    cidrs = str(netaddr.iprange_to_cidrs(startip, endip)[0])
    print(cidrs)
    cidrslist.append(cidrs)
print(cidrslist)
