import QmWuK8AhsMtsinX7DNzikAVXGfZnseE1665ttvVE3DSoUw as mod
assert(mod.container == ['a', 'b', 'c'])

from QmWuK8AhsMtsinX7DNzikAVXGfZnseE1665ttvVE3DSoUw import container
assert(container == ['a', 'b', 'c'])

container.append('d')
assert(container == ['a', 'b', 'c', 'd'])
assert(mod.container == ['a', 'b', 'c', 'd'])

import QmWuK8AhsMtsinX7DNzikAVXGfZnseE1665ttvVE3DSoUw as mod
assert(mod.container == ['a', 'b', 'c', 'd'])

from QmWuK8AhsMtsinX7DNzikAVXGfZnseE1665ttvVE3DSoUw import container
assert(container == ['a', 'b', 'c', 'd'])
