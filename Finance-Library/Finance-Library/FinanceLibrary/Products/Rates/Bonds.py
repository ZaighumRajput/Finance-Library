
class Bond(Product):
  """
  A basic bond
  """
  def __init__(self, principal, maturity, couponRate, numberOfPeriods, paymentPerPeriod):
    self._maturity = maturity
    self._principal = principal
    self._couponRate = couponRate
    self._numberOfPeriods = numberOfPeriods
  
  def Price(requiredYield):
    """
    The Handbook of Fixed Income Securities, Sevent Edition Pg 75
    """
    
  
  
class TreasuryBond(Bond):
  pass


class Inflation_Indexed_Bond(Bond):
  pass
  
class TIPS(Inflation_Indexed_Bond):
  pass
