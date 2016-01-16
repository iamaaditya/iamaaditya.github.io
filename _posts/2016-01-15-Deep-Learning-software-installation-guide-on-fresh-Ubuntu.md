---
title: Deep Learning software installation guide on fresh Ubuntu 
author: aaditya prakash
layout: post
permalink: /2016/01/Deep-Learning-software-installation-guide-on-fresh-Ubuntu/
categories:
  - computer science
  - math
tags:
  - Linux
  - Theano
  - Tensorflow
  - deep learning
---

Recently, I assembled a machine with 4 GPU (Titan X), a clone of [NVIDIA DevBox](https://developer.nvidia.com/devbox). There are few other blog posts which describe the hardware guide, so I will not go into the same detail. Please refer [this](https://www.facebook.com/notes/chris-lengerich/build-your-own-nvidia-devbox/10152999419281541). 
Here are the actual list of parts I bought, [PCPart Picker](https://pcpartpicker.com/user/iamaaditya/saved/LPmZxr)

However this blog post is about the software guide. Although, most of the researchers or grad students like me will have their own custom requirement I thought I should share my software installation guide, for someone who might be new and would benefit from some of these. I have had to do this process couple of times now, and I have learned from my mistakes.

NOTE 1: If getting maximum performance is not a requirement, I would suggest the reader to download Docker Images for Deep Learning packages freely available online, [for e.g](https://hub.docker.com/r/kaixhin/cuda-theano/). Time required for all these standalone installation is justified only when these are going to be used over and again, for e.g in a research lab.

NOTE 2: Some of the commands can be combined to be done in a single line, especially installing libs from apt-get. But I prefer to run them one at a time, for more control and feedback on installation process.

NOTE 3: While most of the scientific community is moving on with Python 3, it seems Deep Learning communmmunty is happy with Python 2. Thus all instllations except where mentioned pertain to Python 2.7.

# Upgrade the Ubuntu
---
 Always, upgrade the ubuntu for security and sanity purposes !

  * `sudo apt-get update        `  # Fetches the list of available updates
  * `sudo apt-get upgrade       `   # Strictly upgrades the current packages
  * `sudo apt-get dist-upgrade  `   # Installs updates (new ones)

# RAID 1
---
## Partition and mount the harddrives
  Since my configuration has two HDD of 3 TB, I have configured them as RAID 1, this provides data redundancy. You do not want to lose weeks worth of training due to HDD crash ! If you do not want RAID 1, then skip this step.

  * `sudo apt-get install -y mdadm   `   # Install mdadm, tool to manage RAID 1
  * `sudo mdadm --assemble --scan    `   # check for existing raids ## found existing !! If not prepare, refer tutorial here <http://askubuntu.com/questions/526747/setting-up-raid-1-on-14-04-with-an-existing-drive>

## Mounting
  * `df -aTh                         `   # shows list of all mounts
  * `sudo mount /dev/md0 /media/hdd/ `   # (Manual) mount existing 
  * `blkid                           `   # shows uuid for drives to add to fstab
  Add the following line to /etc/fstab
    # the RAID 1 mount of two hdd
    UUID=06ad59d9-3176-4c16-95e9-77356cc572d7       /media/hdd      ext2    defaults    0    1
  * `sudo mount -a                   `   # (Permanent) mount using fstab

# Install Essentials, Extras, Git, Zsh 
---
  * `sudo apt-get install -y build-essential`
  * `sudo apt-get install -y ubuntu-restricted-extras`
  * `sudo apt-get install -y vim`
  * `sudo apt-get install -y git`
  * `sudo apt-get install -y git-core`
  * `sudo apt-get install -y zsh`
  * `sudo apt-get install -y tmux`
  * `sudo apt-get install -y CMake`
  * `sudo apt-get install -y libopenblas-dev`
  * `sudo apt-get install -y gcc-4.8 `   # because CUDA (7.0 & 7.5) works will less than 4.9.0
    * make soft link for gcc in /usr/bin
  * `sudo apt-get install -y g++-4.8 `   # because CUDA (7.0 & 7.5) works will less than 4.9.0
    * make soft link for g++ in /usr/bin
  * `sudo apt-get install -y apache2`
    * sudo /etc/init.d/apache2 start `   # start the Apache Server

# Python
---

## Python and Libs
  * `python get-pip.py `   # install pip
  * `sudo apt-get install python-dev `   # pythonLibs 
  * `sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran`
  * `sudo pip install numpy`
  * `sudo pip install cython git+https://github.com/scipy/scipy `   # Installs Cython and Scipy both (Cython is requirement for scipy)
  * `sudo pip install -U scikit-learn `   # Requires numpy and scipy
  * `sudo pip install nose`
  * `sudo pip install markupsafe`

## Python3 and Ipython (Jupyter)
  * `sudo apt-get install python3-pip`  # to install jupyter for python3, it needs pip3 and does not work using pip
  * `sudo pip install jupyter`
  * `sudo pip3 install jupyter `   # I don't know why it requires sepearate installation, especially when not done using Anaconda !
   
# NVIDIA
---

## Install NVIDIA Drivers
  I would highly advice against installing using apt-get as it always installs one version older, and with NVIDIA every generation of driver brings performance boosts.

  * `sudo service lightdm stop       `   # stop the X server before running the installation
    NOTE! Could not sign kernels, make a note of this. It might lead to problems with some libraries later on
  * Download AMD 64 bit Linux drivers from NVIDIA website (manual download and transfer and execute the provided script or binary)

## Install CUDA
  * `sudo ./cuda_7.0.28_linux.run --override  `   # for cuda 7.0
  * `sudo ln -s /usr/bin/g++-4.8 /usr/local/cuda/bin/g++ `   # this might be omitted if a symbolic link has been made from /usr/bin/g++ like mentioned above
  * `sudo ln -s /usr/bin/gcc-4.8 /usr/local/cuda/bin/gcc `   # this might be omitted if a symbolic link has been made from /usr/bin/gcc like mentioned above

# Install GPU Libraries
---

## Theano
  * `sudo pip install Theano`
  * `sudo apt-get install -y python-pycuda `   # also installs the dependencies, but it is best to have own installation of nvidia-cuda, to make sure the version is proper and to maintain multiple version installation

## Tensorflow
  * `sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl`
>  Tensorflow (as of Jan 15, 2016), works on Cuda 7.0 and CuDNN v2 ), thus change /usr/local/cuda softlink

## Keras
  * `sudo pip install keras`  # Could it get any easier !! Thanks people developer of Keras !

## Lasagne
  * `sudo pip install https://github.com/Lasagne/Lasagne/archive/master.zip`  # Preferred way to install Lasagne !

# Optional
---

## Remove unnecessary Ubuntu folders
 When working with only terminal via ssh, you do not need some of these folders //

 * `rm -rf ~/Desktop`
 * `rm -rf ~/Public ` # Is not persistent, after restart Ubuntu recreates this directory
 * `rm -rf ~/Pictures`
 * `rm -rf ~/Music`
 * `rm -rf ~/Videos`
 * `rm -rf ~/Downloads`
 * `rm -rf ~/Templates`
 * `rm -rf ~/Documents`
 * `rm -rf ~/examples.desktop`

## Customization
 These are my personal customization which I do on every machine I use. You may find them useful. They increase visual appeal and efficiency of working on Linux Machine.

  * `chsh -s which zsh`              # Change the shell to ZSH (which zsh should be inside backticks, but Github Markdown messes up the formatting)
  * `sudo reboot now                 `   # Requires restart
  * `git clone git@github.com:iamaaditya/dotfiles.git`
  * `~/dotfiles/install.sh           `   # Run the commands to make the shortcuts
  * `git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim `   # Install bundle
### Solarized Color for vim
  * `cd ~/.vim/colors/ `
  * `wget https://raw.githubusercontent.com/altercation/vim-colors-solarized/master/colors/solarized.vim`
### Powerline & associated fonts
  * `pip install powerline-status    `   # Powerline 
  * `wget https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf`
  * `mkdir -p ~/.fonts/ && mv PowerlineSymbols.otf ~/.fonts/`
  * `fc-cache -vf ~/.fonts`
  * `mkdir -p ~/.config/fontconfig/conf.d/ && mv 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/`
    Note - if some aspects of powerline does not show up, check <http://askubuntu.com/questions/283908/how-can-i-install-and-use-powerline-plugin>


  If you are curious on what this customization looks like, take a look at this screenshot. Here it shows Tmux session with multiple windows, and a multiple panes in the same window. Switching windows and panes in Tmux is very easy. Copy information across windows, sessions and servers is really at the tip of the finger. Also Solarized colors make it tolerable to use the screen for hours.
  ![screenshot](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/Screenshot.png)
