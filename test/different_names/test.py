import QmS5E9xwp1TkLXRu5RYEanraWPbrc2QiKXsy3i3Z8a36Zj as mod
assert(mod.member_container == [1, 2, 3])

import QmQgGbVVmrBWhTTwTPcXviy6CPivfabToqi3B7raPM4dUg as mod_member
assert(mod_member.container == [1, 2, 3])

mod.member_container.append(4)
assert(mod.member_container == [1, 2, 3, 4])
assert(mod_member.container == [1, 2, 3])
