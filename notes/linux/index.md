---
title: Climbing
author: aaditya prakash
layout: page
dsq_thread_id:
  - 
---

## Add time to the command execution
 
This allows me to see how long a process took. Generally, it is best to appent `time` command, which times the process, but generally I forget or that is an overkill.

If you are using ZSH you can use the function `preexec()`

    preexec () {
      DATE=`date +"%H:%M:%S on %Y-%m-%d"`
      C=$(($COLUMNS-24))
      echo -e "\033[1A\033[${C}C ${DATE} "
    }

## Autmatically rename Tmux window

If you use Tmux, would it not be nice, if the window were renamed based on currect directory ?

    function chpwd(){
      ll
      tmux rename-window ${PWD//*\//}
    }


## Search Wiki

Power of wikipedia, quick and from terminal


    wiki() {
    echo -n -e "\n============================================\n\tWelcome to WikiPedia Search"; 
    echo ""; 
    i=1 ; 
    for line in $(lynx --dump "http://en.wikipedia.org/w/index.php?title=Special%3ASearch&profile=default&search=$1&fulltext=Search" | grep http://en.wikipedia.org/wiki | cut -c7-); 
       do 
        echo $i $line; 
        lines[$i]=$line ;  
        i=$(($i+1)); 
      done ; 
    echo -n -e "\n============================================\n\tPlease select the link to open - "; 
    read answer; 
    w3m ${lines[$answer]}
    }

