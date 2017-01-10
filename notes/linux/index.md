---
title: Linux Hacks
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


## Fail2Ban unban (unblock) IP Address

First of all, if you do not have Fail2Ban installed, install it ! It is a lifesave !

But sooner or later, one of your colleage or friend will try the passowrd incorrectly three times (or as many you have setup in your config file. When that happens, follow the steps to unban their IP address.

1. See the list of Banned IPs
`sudo iptables -L -n`

2. Get the name of the jail. This is what confused me for sometime. Do not use the name you see the Iptables. I kept seeing f2bsshd and tried using that. Correct jail name is given by the following command.
`sudo fail2ban-client status`

3. Unban the IP
`fail2ban-client set <jail_name> unbanip <ip_address>`
for e.g
`fail2ban-client set ssh unbanip 123.123.123.123`

<pre>
    Errors:

    Message
        ERROR  NOK: ('ssh-iptables',)
        Sorry but the jail 'ssh-iptables' does not exist

        ERROR  NOK: ('f2b-sshd',)
        Sorry but the jail 'f2b-sshd' does not exist

    Issue 
        Incorrect jail name
    Solution 
       
        See point 2 above
</pre>


## Different ways to redirect STDOUT and STDERR to screen or file

    CREDIT: http://stackoverflow.com/a/19279694


    #!/bin/bash

    STATUSFILE=x.out
    LOGFILE=x.log

    ### All output to screen
    ### Do nothing, this is the default


    ### All Output to one file, nothing to the screen
    #exec > ${LOGFILE} 2>&1


    ### All output to one file and all output to the screen
    #exec > >(tee ${LOGFILE}) 2>&1


    ### All output to one file, STDOUT to the screen
    #exec > >(tee -a ${LOGFILE}) 2> >(tee -a ${LOGFILE} >/dev/null)


    ### All output to one file, STDERR to the screen
    ### Note you need both of these lines for this to work
    #exec 3>&1
    #exec > >(tee -a ${LOGFILE} >/dev/null) 2> >(tee -a ${LOGFILE} >&3)


    ### STDOUT to STATUSFILE, stderr to LOGFILE, nothing to the screen
    #exec > ${STATUSFILE} 2>${LOGFILE}


    ### STDOUT to STATUSFILE, stderr to LOGFILE and all output to the screen
    #exec > >(tee ${STATUSFILE}) 2> >(tee ${LOGFILE} >&2)


    ### STDOUT to STATUSFILE and screen, STDERR to LOGFILE
    #exec > >(tee ${STATUSFILE}) 2>${LOGFILE}


    ### STDOUT to STATUSFILE, STDERR to LOGFILE and screen
    #exec > ${STATUSFILE} 2> >(tee ${LOGFILE} >&2)


    echo "This is a test"
    ls -l sdgshgswogswghthb_this_file_will_not_exist_so_we_get_output_to_stderr_aronkjegralhfaff
    ls -l ${0}

## Redhat (RHEL) and CentOS
    Installling a library without sudo

    1. Download the pre-compiled binary ".rpm". [See this](http://rpmfind.net/linux/rpm2html/search.php)
    2. conver rpm to cpio using
    `rpm2cpio to-install.rpm | cpio -idv`

## Rsync [See this](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)


## Sort by column in Vim

    First make the columsn (separate them so that you know exactly how many columns and which ones)
    `:%!column -t`

    Now to sort by second (2)  column, and treat it as number (n) and in reverse (r)
    `:%!sort -k2nr`

    More examples
    `:%!sort -k4 -bk3g`
    Sort by 4th column (k4), followed by 3rd column (k3), ignore blank spaces (b), general numeric sort (g)

[Credit](https://jordanelver.co.uk/blog/2014/03/12/sorting-columnds-of-text-in-vim-using-sort/)


## Delete leading and trailing lines from files

    sed -i 's/^[ \t]*//;s/[ \t]*$//' <filename.txt>
    * -i option in sed makes the changes inplace to the given file

## Count a character for every line in a file

    sed 's/,//g' output_reuters_first_layer.txt| awk '{print length }'

## Find list of users who have sudo 

    grep -Po '^sudo.+:\K.*$' /etc/group

## Split file by percentage (line number)

    split -l $[ $(wc -l filename|cut -d" " -f1) * 70 / 100 ] filename 
