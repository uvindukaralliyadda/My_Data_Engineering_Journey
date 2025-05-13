import convertors
from convertors import kg_to_lbs
from convertors import lbs_to_kgs

import utils


print(lbs_to_kgs(500))
print(kg_to_lbs(100))

print(convertors.kg_to_lbs(70))

numbers=[10,3,6,2]
max=utils.find_max(numbers)
print(max)
