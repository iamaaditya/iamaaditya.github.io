---
title: New machine instructions for GPU
author: aaditya prakash
layout: page
dsq_thread_id:
  - 
---

## Install the drivers

  * Download NVIDIA Drivers [from here](http://www.nvidia.com/Download/index.aspx)
    Do not use apt-get install nvidia-* for drivers. Generally they are few cycles older than those on the website.
  * You will get a file named something like this `NVIDIA-Linux-x86_64-375.39.run`
  * Give it executable permission
    `chmod +x NVIDIA-Linux-x86_64-375.39.run`
  * Run with sudo
    `sudo ./NVIDIA-Linux-x86_64-375.39.run`

   Possible issues:
   You might have to stop the X-server (the GUI) to install the drivers.
   Use the following command on Ubuntu
   `sudo service lightdm stop`


## Install CUDA
  
  * Download the latest CUDA drivers [from here](https://developer.nvidia.com/cuda-downloads)
    Download the 'runfile (local)'. This avoids issues of proxy while installing using network based debian file.
  * Use the following command to run the installer:
    `sudo sh cuda_8.0.61_375.26_linux.run`
    It will also prompt to install OpenCL and NVIDIA-Samples. It is not required but recommended to install those.
    If you install NVIDIA-Samples, use 1_Utilities/deviceQuery to check the GPU specs.
    It will ask you if you want to make soft-link to /usr/local/cuda - say YES

## Install CuDNN
  
  * Download the latest CuDNN [from here](https://developer.nvidia.com/cudnn)
  * Extract the tar file.
  * Copy all the files inside lib64/ to /usr/local/cuda/lib64/
  * Copy the file include/cudnn.h to /usr/local/cuda/include/
  * Some libraries will require LD_LIBRARY_PATH and LIBRARY_PATH to point to this lib64 directory:
  `export LD_LIBRARY_PATH=<path_to_lib64>:$LD_LIBRARY_PATH`
  `export LIBRARY_PATH=<path_to_lib64>:$LIBRARY_PATH`

## Install Tensorflow
  
   For stable release version:
   * sudo pip install --upgrade tensorflow_gpu
   For latest nightly release:
   * sudo pip install --upgrade <url>
   Get this <url> from https://github.com/tensorflow/tensorflow





