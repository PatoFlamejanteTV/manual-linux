# BTop, `btop`

`[htop](htop)`, só que mais complexo, eu diria.

Por algum motivo ele precisa de Root caso você queira usar-lo no Termux.

```
╭─quack @ termux in ~
╰─❯ btop                                                                   ERROR: btop can't do anything useful on Termux without root. Quitting!
╭─quack @ termux in ~
╰─✗  sudo btop
The program sudo is not installed. Install it by executing:                 pkg install sudo
or
 pkg install tsu
╭─quack @ termux in ~
╰─✗  pkg install tsu
Checking availability of current mirror:
[*] https://packages-cf.termux.dev/apt/termux-main: ok
Reading package lists... Done                                              Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  tsu
0 upgraded, 1 newly installed, 0 to remove and 43 not upgraded.
Need to get 4376 B of archives.
After this operation, 53.2 kB of additional disk space will be used.
Get:1 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 tsu all 8.6.0-1 [4376 B]
Fetched 4376 B in 0s (19.6 kB/s)
Selecting previously unselected package tsu.
(Reading database ... 151357 files and directories currently installed.)
Preparing to unpack .../archives/tsu_8.6.0-1_all.deb ...
Unpacking tsu (8.6.0-1) ...
Setting up tsu (8.6.0-1) ...
╭─quack @ termux in ~ took 2s968ms
╰─❯ sudo btop
No superuser binary detected.
Are you rooted?
╭─quack @ termux in ~
╰─✗
```