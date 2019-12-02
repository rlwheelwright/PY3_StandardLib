# Getting more control over formatting
from datetime import datetime

now = datetime.now()

# %a = Mon
# %A = Monday
# %d = 10
print(now.strftime("%a %A %d"))

# %b Jan
# %B January
# %m 01 (for January)
print(now.strftime("%b %B %m"))

# %H hours
# %M minutes
# %S seconds
# %p AM or PM
print(now.strftime("%H:%M.%S %p"))

# %y 2-digit year; 18
# %Y 4-digit year; 2018
print(now.strftime("%y %Y"))

# Putting it all together
print(now.strftime("%a %B %d %Y %H:%M.%S %p"))
