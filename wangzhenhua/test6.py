import sys
from affairs import affairs

index = int(sys.argv[1])
print(index)
print(type(index))
data = affairs.get_data()
print(data[index-1:index])
