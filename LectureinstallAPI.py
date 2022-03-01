from forex_python.converter import CurrencyRates

c = CurrencyRates()
result = c.get_rates('USD')
#thaibath = c.get_rates('USD', 'THB')

print(result)
#print(thaibath)
