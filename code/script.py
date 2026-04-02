from ucimlrepo import fetch_ucirepo 
import os
  
# fetch dataset 
apartment_for_rent_classified = fetch_ucirepo(id=555) 
  
# data (as pandas dataframes) 
X = apartment_for_rent_classified.data.features 
y = apartment_for_rent_classified.data.targets 
  
# metadata 
print(apartment_for_rent_classified.metadata) 
  
# variable information 
print(apartment_for_rent_classified.variables) 

# print(X)

outname = 'apartment_data.csv'

outdir = './../data'
if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)    

X.to_csv(fullname, index=False)
