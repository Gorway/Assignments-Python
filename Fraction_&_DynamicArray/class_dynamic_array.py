import sys
from random import randint
from typing import List, Any, Iterator, Iterable

class DynamicArray:
  def __init__(self, capacity: int = 10) -> None:
    if capacity < 1:
      raise ValueError("Capacity must be positiv.")
    if capacity > sys.maxsize:
      raise ValueError(f"Capacity can't exceed sys.maxsize {sys.maxsize}")
    self.size: int = 0
    self.capacity: int = capacity 
    self.array: List[Any] = [None] * self.capacity

  def _size_change(self, new_capacity: int) -> None:
    resized_array: List[Any] = [None] * new_capacity
    for i in range(self.size):
      resized_array[i]  = self.array[i]
    self.array = resized_array
    self.capacity = new_capacity

  def append(self, value: Any) -> None:
    if self.size == self.capacity:
      self._size_change(self.capacity * 2)  
    self.array[self.size] = value
    self.size += 1

  def extend(self, iterable: Iterable[Any]) -> None:
    if not isinstance(iterable, Iterable):
      raise ValueError
    
    for value in iterable:
      self.append(value)

  def insert(self, index: int, value: Any) -> None:
    if not (0 <= index < self.size):
      raise IndexError("Index out of range.")
    if self.size == self.capacity:
      self._size_change(self.capacity * 2)
    self.array[index+1:self.size+1] = self.array[index:self.size]
    self.array[index] = value
    self.size += 1

  def remove(self, value: Any) -> None:
    for i in range(self.size):
      if self.array[i] == value:
        self.array[i:self.size -1] = self.array[i + 1:self.size]
        self.array[self.size - 1] = None
        self.size -= 1
        return
    raise ValueError(f"{value} not found.")

  def pop(self, index: int = -1) -> Any:
    if self.size == 0:
      raise IndexError("Array is empty.")
    
    if index < 0:
      index += self.size
    
    if not (0 <= index < self.size):
      raise IndexError("Index out of range.")
    
    value = self.array[index]

    if index != self.size - 1:
      self.array[index:self.size -1] = self.array[index +1: self.size]
    
    self.array[self.size - 1] = None
    self.size -= 1
    
    return value

  def index(self, value: int, start: int = 0, stop: int = sys.maxsize) -> int:
    if stop is None:
      stop = self.size
      
    if start < 0:
      start += self.size
    
    if stop < 0:
      stop += self.size
    
    if start < 0:
      start = 0
    
    if stop > 0:
      stop = self.size
    
    if start > stop:
      raise ValueError("Start can't be greater than stop index.")
      
    for i in range(self.size):
      if self.array[i] == value:
        return i
    
    raise ValueError(f"{value} not found.")

  def count(self, value: int) -> int:
    count = 0
    for i in range(self.size):
      if self.array[i] == value:
        count += 1
    return count

  def clear(self) -> None:
    self.array = [None] * self.capacity
    self.size = 0

  def copy(self) -> 'DynamicArray':
    copied_array = DynamicArray(self.capacity)
    copied_array.size = self.size
    copied_array.array = self.array[:]
    return copied_array

  def sort(self) -> None:
    self._quick_sort(0, self.size -1)

  def _quick_sort(self, low: int, high: int) -> None:
    if low < high:
      pivot = self._partition(low, high)
      self._quick_sort(low, pivot -1)
      self._quick_sort(pivot + 1, high)

  def _partition(self, low: int , high: int) -> int:
    random_pivot = randint(low, high)
    
    self.array[random_pivot], self.array[high] = self.array[high], self.array[random_pivot]
    
    pivot = self.array[high]
    i = low - 1
    
    for j in range(low, high):
      if self.array[j] <= pivot:
        i += 1
        self.array[i], self.array[j] = self.array[j], self.array[i]

    self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
    return i + 1

  def __repr__(self) -> str:
    return f"DynamicArray: {[self.array[i] for i in range(self.size)]}"

  def __str__(self) -> str:
    return '[' + ', '.join(str(self.array[i]) for i in range(self.size)) + ']'

  def __setitem__(self, index: int, value: int) -> Any:
    if  0 <= index < self.size:
      self.array[index] = value
    else:
      raise IndexError("Index out of range.")

  def __getitem__(self, index: int ) -> Any:
    if  0 <= index < self.size:
      return self.array[index]
    else:
      raise IndexError("Index out of range.")

  def __len__(self) -> int:
    return self.size

  def __iter__(self) -> Iterator[Any]:
    for i in range(self.size):
      yield self.array[i]

  def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
    if not isinstance(other, DynamicArray):
      raise TypeError("Operands must be DynamicArray instance.")
  
    concateneted_array = DynamicArray(self.size+ other.size)
  
    for i in range(self.size):
      concateneted_array.append(self.array[i])
  
    for i in range(other.size):
      concateneted_array.append(other.array[i])
  
    return concateneted_array

  def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
    if not isinstance(other, DynamicArray):
        raise TypeError("Operands must be DynamicArray instance.")
    if self.size + other.size > self.capacity:
      self._resize(max(self.capacity * 2, self.size + other.size))
    for i in range(other.size):
      self.append(other.array[i])
    return self

  def __eq__(self, other: 'DynamicArray') -> bool:
    if not isinstance(other, DynamicArray):
      return NotImplemented
    
    if self.size != other.size:
      return False
    
    for i in range(self.size):
      if self.array[i] != other.array[i]:
        return False
    
    return True

  def __ne__(self, other: 'DynamicArray') -> bool:
    if not isinstance(other, DynamicArray):
      return NotImplemented
    
    return not (self == other)

  def __lt__(self, other: 'DynamicArray') -> bool:
    if not isinstance(other, DynamicArray):
      return NotImplemented
    
    min_length = self.size if self.size < other.size else other.size

    for i in range(min_length):
      if self.array[i] < other.array[i]:
        return True
      elif self.array[i] > other.array[i]:
        return False
      
    return self.size < other.size

  def __le__(self, other: 'DynamicArray') -> bool:
    if not isinstance(other, DynamicArray):
      return NotImplemented
    min_length = self.size if self.size < other.size else other.size

    for i in range(min_length):
      if self.array[i] < other.array[i]:
        return True
      elif self.array[i] > other.array[i]:
        return False
      
    return self.size <= other.size

  def __gt__(self, other: 'DynamicArray') -> bool:
    if not isinstance(other, DynamicArray):
      return NotImplemented
    
    min_length = self.size if self.size < other.size else other.size

    for i in range(min_length):
      if self.array[i] > other.array[i]:
        return True
      elif self.array[i] < other.array[i]:
        return False
      
    return self.size > other.size

  def __ge__(self, other: 'DynamicArray') -> bool:
    if not isinstance(other, DynamicArray):
      return NotImplemented

    min_length = self.size if self.size < other.size else other.size

    for i in range(min_length):
      if self.array[i] > other.array[i]:
        return True
      elif self.array[i] < other.array[i]:
        return False

    return self.size >= other.size

  def __hash__(self) -> TypeError:
    raise TypeError("DynamicArray is muttable object and can't be hashed.")
  
# ob1 = DynamicArray()
# ob1.append(1)
# ob1.append(1)
# ob1.append(1)

# ob2 = DynamicArray()
# ob2.append(2)
# ob2.append(2)
# ob2.append(2)

# #ob1.extend([123,'asd',213])
# print(ob1)
# #ob1.remove('asd')
# print(ob1)
# ob1.pop()
# print(ob1)
# print(len(ob1))
# # print(ob1 == ob2)
# # print(ob1 > ob2)
# # print(ob1 < ob2)
# # print(ob1 <= ob2)
# # print(ob1 >= ob2)
# #print(ob1[2])
# #ob2[2] = 888
# #print(ob2[2])
# #print(ob1 + ob2)
# ob1 += ob2
# print(ob1)
# ob3 = DynamicArray()
# ob3.extend([9,7,6,5,4,4,3,21,3,46,7,90])
# ob3.sort()
# print(ob3)