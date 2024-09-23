import dataclasses

#dataclasses.dataclass(frozen=True) 
class Fraction():
  def __init__(self, numerator: int, denominator: int = 1) -> None:
    if not isinstance(denominator, int) and denominator == 0:
      raise ValueError("Denominator must be integer and can't be zero.")  
    self.numerator = numerator
    self.denominator = denominator
    self.simplify()
  
  #--------------------------------Simplify-------------------------------------------------
  def _gcd(self, a: int, b: int) -> int:
    while b != 0:
      a, b = b, a % b
    return abs(a)
  
  def simplify(self) -> None:
    common_divisor = self._gcd(self.numerator, self.denominator)
    self.numerator //= common_divisor
    self.denominator //= common_divisor
  #--------------------------------Representation---------------------------------------------
  def __str__(self) -> str:
    return f"{self.numerator}/{self.denominator}"
  
  def __repr__(self) -> str:
    return f"{Fraction.__name__}({self.numerator},{self.denominator})"
  #-----------------------------Arithmetic Operations------------------------------------------
  def __add__(self, other: 'Fraction') -> 'Fraction':
    if isinstance(other, int):
      other = Fraction(other)
    new_numerator = (self.numerator * other.denominator +
                     other.numerator * self.denominator)
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)  
  
  def __radd__(self, other: 'Fraction') -> "Fraction":
    return self.__add__(other)
  
  def __sub__(self, other: 'Fraction') -> 'Fraction':
    if isinstance(other, int):
      other = Fraction(other)
    new_numerator = (self.numerator * other.denominator -
                     other.numerator * self.denominator)
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)
    
  def __rsub__(self, other: 'Fraction') -> "Fraction":
    return self.__sub__(other)
  
  def __mul__(self, other: 'Fraction') -> 'Fraction':
    if isinstance(other, int):
      other = Fraction(other)
    new_numerator = self.numerator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)    

  def __rmul__(self, other: 'Fraction') -> "Fraction":
    return self.__mul__(other)
  
  def __truediv__(self, other: 'Fraction') -> "Fraction":
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      if other.numerator == 0:
        raise ZeroDivisionError
      new_numerator = self.numerator * other.denominator
      new_denominator = self.denominator * other.numerator
      return Fraction(new_numerator, new_denominator)
    else:
      return NotImplemented
  
  def __rtruediv__(self, other: 'Fraction') -> 'Fraction':
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      if self.numerator == 0:
        raise ZeroDivisionError
      new_numerator = other.numerator * self.denominator
      new_denominator = other.denominator * self.numerator
      return Fraction(new_numerator, new_denominator)
    else:
      return NotImplemented
#---------In-place arithmetic methods----------------
  def __iadd__(self, other: 'Fraction') -> 'Fraction':
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      result = self + other
      self.numerator = result.numerator
      self.denominator = result.denominator
      return self
    else:
      return NotImplemented

  def __isub__(self, other: 'Fraction') -> 'Fraction':
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      result = self - other
      self.numerator = result.numerator
      self.denominator = result.denominator
      return self
    else:
      return NotImplemented
  
  #-------------------------Comprasion Methods---------------------------------------
  
  def __eq__(self, other: 'Fraction') -> bool:
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      return (self.numerator == other.numerator) and (self.denominator == other.denominator)
    else:
      return NotImplemented

  def __ne__(self, other: 'Fraction') -> bool:
    return not self.__eq__(other)
  
  def __lt__(self, other: 'Fraction') -> bool:
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      left_numerator = self.numerator * other.denominator
      right_numerator = other.numerator * self.denominator
      return left_numerator < right_numerator
    else:
      return NotImplemented
  
  def __le___(self, other: 'Fraction') -> bool:
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      left_numerator = self.numerator * other.denominator
      right_numerator = other.numerator * self.denominator
      return left_numerator <= right_numerator
    else:
      return NotImplemented

  def __gt__(self, other: 'Fraction') -> bool:
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
      left_numerator = self.numerator * other.denominator
      right_numerator = other.numerator * self.denominator
      return left_numerator > right_numerator
    else:
      return NotImplemented
  
  def __ge__(self, other: 'Fraction') -> bool:
    if isinstance(other, int):
      other = Fraction(other)
    if isinstance(other, Fraction):
     left_numerator = self.numerator * other.denominator
     right_numerator = other.numerator * other.denominator
     return left_numerator >= right_numerator
    else:
      return NotImplemented
    
  def __float__(self) -> float:
    return self.numerator / self.denominator
  
  def __int__(self) -> int:
    return self.numerator // self.denominator
  
  def __neg__(self) -> 'Fraction':
    return Fraction(-self.numerator, self.denominator)

  def mixed_numbers(self) -> str:
    whole_num = self.__int__()
    remainder = self.numerator % self.denominator
    if remainder == 0:
      return str(whole_num)
    else:
      return f"{whole_num} {remainder}/{self.denominator}"
  
  def __hash__(self) -> int:
    return hash((self.numerator, self.denominator))