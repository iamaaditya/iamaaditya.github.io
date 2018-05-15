---
title: Clipboard to Email &#8211; Python Code
author: aaditya prakash
layout: post
permalink: "/2012/08/clipboard-to-email-python-code/"
categories:
- computer science
tags:
- code
- python
date: 2012-08-25 00:00:00 +0000
---
## Why

Very often I have to send lot of stuff (links, texts, comments, notes) to a particular Email Address. Initially I started using www.emailtheweb.com , it has a nice bookmark button (when you press the same, the webpage in the background is emailed). This was not the swiftest method, since it had multiple clicks, few pages to visit, accept button and unfortunately too long pre-processing time.

Then I started using <a title="Evernote - Taking notes" href="http://evernote.com/" target="_blank">Evernote</a>. It is perfect, works like a charm, has an android app, chrome extension, standalone windows program, but unfortunately this one didn&#8217;t suit my exact need. My need was to have them in my email. You may ask, whats the difference, website repository is same as email, but not for me (since my workplace has strict policies of blocking note taking sites (*don&#8217;t ask*)).

## Use

So, I built a small tool, a python code which automatically sends the content of clipboard into the email address you specify. Ofcourse it works by using one of your email as the host, but even if you use the same email as To/From, it still works.

Parts of the code is due to help from <http://vreugdenhilresearch.nl/> and http://segfault.in

In minimal you only have to change line number <span style="text-decoration: underline;"><strong>59-60</strong></span> From-To Email address and <span style="text-decoration: underline;"><strong>66</strong></span> for password, i.e if you have a gmail account &#8211; From address only (To address need not be gmail). If you decide to use other email hosts, kindly update the line number <span style="text-decoration: underline;"><em>63</em></span> too (Google to find out the SMTP address and port for your email.

To use this, I copy the content (Ctrl+C), and press the shortcut (place the code in desktop, Right click->key in the keyboard shortcut (Ctrl+Alt+<some_character>).

*Note you will need Python installed for this to work. (Works with both Python 2x and 3x versions)

## Code

<div class="wp_syntax">
  <table>
    <tr>
      <td class="line_numbers">
        <pre>1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
</pre>
      </td>
      
      <td class="code">
        <pre class="python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> <span style="color: #dc143c;">sys</span>
<span style="color: #ff7700;font-weight:bold;">import</span> <span style="color: #dc143c;">smtplib</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">from</span> <span style="color: #dc143c;">email</span>.<span style="color: black;">mime</span>.<span style="color: black;">text</span> <span style="color: #ff7700;font-weight:bold;">import</span> MIMEText
<span style="color: #808080; font-style: italic;">#Required for email modules</span>
<span style="color: #ff7700;font-weight:bold;">import</span> ctypes
&nbsp;
<span style="color: #808080; font-style: italic;">#Get required functions, strcpy..</span>
strcpy <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">cdll</span>.<span style="color: #dc143c;">msvcrt</span>.<span style="color: black;">strcpy</span>
ocb <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">user32</span>.<span style="color: black;">OpenClipboard</span>    <span style="color: #808080; font-style: italic;">#Basic Clipboard functions</span>
ecb <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">user32</span>.<span style="color: black;">EmptyClipboard</span>
gcd <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">user32</span>.<span style="color: black;">GetClipboardData</span>
scd <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">user32</span>.<span style="color: black;">SetClipboardData</span>
ccb <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">user32</span>.<span style="color: black;">CloseClipboard</span>
ga <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">kernel32</span>.<span style="color: black;">GlobalAlloc</span>    <span style="color: #808080; font-style: italic;"># Global Memory allocation</span>
<span style="color: #dc143c;">gl</span> <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">kernel32</span>.<span style="color: black;">GlobalLock</span>     <span style="color: #808080; font-style: italic;"># Global Memory Locking</span>
gul <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">windll</span>.<span style="color: black;">kernel32</span>.<span style="color: black;">GlobalUnlock</span>
GMEM_DDESHARE <span style="color: #66cc66;">=</span> <span style="color: #ff4500;">0x2000</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">def</span> Get<span style="color: black;">&#40;</span> <span style="color: black;">&#41;</span>:
  ocb<span style="color: black;">&#40;</span><span style="color: #008000;">None</span><span style="color: black;">&#41;</span> <span style="color: #808080; font-style: italic;"># Open Clip, Default task</span>
&nbsp;
  pcontents <span style="color: #66cc66;">=</span> gcd<span style="color: black;">&#40;</span><span style="color: #ff4500;">1</span><span style="color: black;">&#41;</span>
&nbsp;
  data <span style="color: #66cc66;">=</span> ctypes.<span style="color: black;">c_char_p</span><span style="color: black;">&#40;</span>pcontents<span style="color: black;">&#41;</span>.<span style="color: black;">value</span>
&nbsp;
  <span style="color: #808080; font-style: italic;">#gul(pcontents) ?</span>
  ccb<span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
&nbsp;
  <span style="color: #ff7700;font-weight:bold;">return</span> data
&nbsp;
<span style="color: #ff7700;font-weight:bold;">def</span> Paste<span style="color: black;">&#40;</span> data <span style="color: black;">&#41;</span>:
  ocb<span style="color: black;">&#40;</span><span style="color: #008000;">None</span><span style="color: black;">&#41;</span> <span style="color: #808080; font-style: italic;"># Open Clip, Default task</span>
&nbsp;
  ecb<span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
&nbsp;
  hCd <span style="color: #66cc66;">=</span> ga<span style="color: black;">&#40;</span> GMEM_DDESHARE<span style="color: #66cc66;">,</span> <span style="color: #008000;">len</span><span style="color: black;">&#40;</span> <span style="color: #dc143c;">bytes</span><span style="color: black;">&#40;</span>data<span style="color: #66cc66;">,</span><span style="color: #483d8b;">"ascii"</span><span style="color: black;">&#41;</span> <span style="color: black;">&#41;</span>+<span style="color: #ff4500;">1</span> <span style="color: black;">&#41;</span>
&nbsp;
  pchData <span style="color: #66cc66;">=</span> <span style="color: #dc143c;">gl</span><span style="color: black;">&#40;</span>hCd<span style="color: black;">&#41;</span>
&nbsp;
  strcpy<span style="color: black;">&#40;</span>ctypes.<span style="color: black;">c_char_p</span><span style="color: black;">&#40;</span>pchData<span style="color: black;">&#41;</span><span style="color: #66cc66;">,</span><span style="color: #dc143c;">bytes</span><span style="color: black;">&#40;</span>data<span style="color: #66cc66;">,</span><span style="color: #483d8b;">"ascii"</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>
&nbsp;
  gul<span style="color: black;">&#40;</span>hCd<span style="color: black;">&#41;</span>
&nbsp;
  scd<span style="color: black;">&#40;</span><span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>hCd<span style="color: black;">&#41;</span>
&nbsp;
  ccb<span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
&nbsp;
clp <span style="color: #66cc66;">=</span> Get<span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
<span style="color: #ff7700;font-weight:bold;">print</span><span style="color: black;">&#40;</span>clp<span style="color: black;">&#41;</span>
&nbsp;
&nbsp;
<span style="color: #808080; font-style: italic;"># Create a text/plain message</span>
msg <span style="color: #66cc66;">=</span> MIMEText<span style="color: black;">&#40;</span><span style="color: #008000;">str</span><span style="color: black;">&#40;</span>clp<span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>
msg<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Subject'</span><span style="color: black;">&#93;</span> <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'put the subject you require, I keep it fix to some obsure word'</span>
<span style="color: #808080; font-style: italic;">#idea behind using obsure code is to help me arrange emails</span>
<span style="color: #808080; font-style: italic;">#you could also use sys.argv for subject but I want to keep the process minimal & quick</span>
&nbsp;
msg<span style="color: black;">&#91;</span><span style="color: #483d8b;">'From'</span><span style="color: black;">&#93;</span>	<span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"YourEmailAddress"</span>
msg<span style="color: black;">&#91;</span><span style="color: #483d8b;">'To'</span><span style="color: black;">&#93;</span> 	<span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"RecipientAddress"</span>
&nbsp;
s <span style="color: #66cc66;">=</span> <span style="color: #dc143c;">smtplib</span>.<span style="color: black;">SMTP</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'smtp.gmail.com'</span><span style="color: #66cc66;">,</span> <span style="color: #ff4500;">587</span><span style="color: black;">&#41;</span> 
<span style="color: #808080; font-style: italic;"># these values are for gmail, you may want to change it if others</span>
s.<span style="color: black;">ehlo</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
s.<span style="color: black;">starttls</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
passwordGl <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'your email password here'</span>
&nbsp;
s.<span style="color: black;">login</span><span style="color: black;">&#40;</span>msg<span style="color: black;">&#91;</span><span style="color: #483d8b;">'From'</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> passwordGl<span style="color: black;">&#41;</span>
<span style="color: #ff7700;font-weight:bold;">try</span>:
   <span style="color: #808080; font-style: italic;"># Python 3.2.1</span>
   <span style="color: #ff7700;font-weight:bold;">print</span><span style="color: black;">&#40;</span>s.<span style="color: black;">send_message</span><span style="color: black;">&#40;</span>msg<span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>
<span style="color: #ff7700;font-weight:bold;">except</span> <span style="color: #008000;">AttributeError</span>:
   <span style="color: #808080; font-style: italic;"># Python 2.7.2</span>
   s.<span style="color: black;">sendmail</span><span style="color: black;">&#40;</span>msg<span style="color: black;">&#91;</span><span style="color: #483d8b;">'From'</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> <span style="color: black;">&#91;</span>msg<span style="color: black;">&#91;</span><span style="color: #483d8b;">'To'</span><span style="color: black;">&#93;</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> msg.<span style="color: black;">as_string</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>
&nbsp;
s.<span style="color: black;">quit</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span></pre>
      </td>
    </tr>
  </table>
</div>