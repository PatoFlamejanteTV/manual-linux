# help.md
Praticamente uma lista de comandos dentro do terminal, ele exibe os comandos utilizáveis no sistema, juntamente com `-argumentos e --flags` disponíveis na usagem dos comandos.

Extremamente útil caso você esteja em uma distro mais "hacker" (Arch, Gentoo, LFS, etc..), ou quando você faz algo errado no sistema e o seu computador inicia no GRUB bash (um dos meus traumas, particularmente).

```
╭─quack @ termux in ~
╰─❯ help
GNU bash, version 5.3.3(1)-release (aarch64-unknown-linux-android)
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
Use `info bash' to find out more about the shell in general.
Use `man -k' or `info' to find out more about commands not in this list.

A star (*) next to a name means that the command is disabled.

 ! PIPELINE                 history [-c] [-d offset>
 job_spec [&]               if COMMANDS; then COMMA>
 (( expression ))           jobs [-lnprs] [jobspec >
 . [-p path] filename [ar>  kill [-s sigspec | -n s>
 :                          let arg [arg ...]
 [ arg... ]                 local [option] name[=va>
 [[ expression ]]           logout [n]
 alias [-p] [name[=value]>  mapfile [-d delim] [-n >
 bg [job_spec ...]          popd [-n] [+N | -N]
 bind [-lpsvPSVX] [-m key>  printf [-v var] format >
 break [n]                  pushd [-n] [+N | -N | d>
 builtin [shell-builtin [>  pwd [-LP]
 caller [expr]              read [-Eers] [-a array]>
 case WORD in [PATTERN [|>  readarray [-d delim] [->
 cd [-L|[-P [-e]]] [-@] [>  readonly [-aAf] [name[=>
 command [-pVv] command [>  return [n]
 compgen [-V varname] [-a>  select NAME [in WORDS .>
 complete [-abcdefgjksuv]>  set [-abefhkmnptuvxBCEH>
 compopt [-o|+o option] [>  shift [n]
 continue [n]               shopt [-pqsu] [-o] [opt>
 coproc [NAME] command [r>  source [-p path] filena>
 declare [-aAfFgiIlnrtux]>  suspend [-f]
 dirs [-clpv] [+N] [-N]     test [expr]
 disown [-h] [-ar] [jobsp>  time [-p] pipeline
 echo [-neE] [arg ...]      times
 enable [-a] [-dnps] [-f >  trap [-Plp] [[action] s>
 eval [arg ...]             true
 exec [-cl] [-a name] [co>  type [-afptP] name [nam>
 exit [n]                   typeset [-aAfFgiIlnrtux>
 export [-fn] [name[=valu>  ulimit [-SHabcdefiklmnp>
 false                      umask [-p] [-S] [mode]
 fc [-e ename] [-lnr] [fi>  unalias [-a] name [name>
 fg [job_spec]              unset [-f] [-v] [-n] [n>
 for NAME [in WORDS ... ]>  until COMMANDS; do COMM>
 for (( exp1; exp2; exp3 >  variables - Names and m>
 function name { COMMANDS>  wait [-fn] [-p var] [id>
 getopts optstring name [>  while COMMANDS; do COMM>
 hash [-lr] [-p pathname]>  { COMMANDS ; }
 help [-dms] [pattern ...>
╭─quack @ termux in ~
╰─❯
```