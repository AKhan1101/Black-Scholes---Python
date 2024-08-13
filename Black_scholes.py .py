from yahoo_fin import options as op
import math
from scipy.stats import norm

#Ticker
Tick = 'msft'

S = 42 # Underlying price
k = 40 # Strike Price
t = 0.5 # Time to expiration [Years]
r = 0.03586 # US 10-year treasury yeild
vol = 0.2 # Volality

#Calculate d1
d1 = (math.log(S/k)+(r+0.5*vol**2)*t)/(vol*math.sqrt(t))
# Calculate d2
d2 = d1 - (vol*math.sqrt(t))

print ("d1 is:", d1)
print ("d2 is:", d2)

# Calculate call price 
Call_price = S*norm.cdf(d1) - k*math.exp(-r*t)*norm.cdf(d2)

# Calculate put price
Put_price = k*math.exp(-r*t)*norm.cdf(d2) - S*norm.cdf(d1)

print ("The call price is:", Call_price)
print ("The put price is:", Put_price)
# Get expiration dates

#exp_Dates = op.get_expiration_dates(Tick)


#print(exp_Dates)
#Retrieve data

#chain_data = op.get_options_chain(Tick,date)