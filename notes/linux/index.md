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
