An update on visual studio code and pycom

25 january, 2022

TL;DR: vs code 1.63 + pymakr 1.17 seems to work fine.

background:
there are well-known ongoing version compatibility issues between
vs code and pycoms pymakr extension.
with every version upgrade, things tend to break.

should you need to roll back:
older versions of vs code and pymakr plugin are here:
https://code.visualstudio.com/updates/v1_63
https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr
(but pymakr can be rolled back from the vs code plugin menu)





but, let's check.
OS: Ubuntu 20

vs code - November 2021 (version 1.63)
Pymakr v1.1.12
==> There was an error with your serialport module, Pymakr will likely not work properly. Please try to install again or report an issue on our github (see developer console for details)

i update to pymakr 1.17

vs code - November 2021 (version 1.63)
Pymakr v1.1.17
==> works fine!

now upgrade vs code to latest:
