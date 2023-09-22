# import scorer
#
# s = scorer.Score()

from scorer import Score

s = Score()

print(s.score)


import sys

print(sys.path)

# sys.path.append("/home/igr")
#
# import scorer

import test_module

e = test_module.Extra()

tmm = test_module.TestModuleModule()

print(isinstance(tmm, test_module.Extra))
