---
title: How math can help discretionary traders
author: aaditya prakash
layout: post
permalink: "/2012/07/advice-to-discretionary-scalpers/"
categories:
- math
tags:
- trading
date: 2012-07-25 00:00:00 +0000
---
## <span style="text-decoration: underline;">The Basics</span>

**1. ****Reduce the number of instruments you trade**

If you are doing discretionary trading you don’t want to trade on too many different instruments. It needs tremendous focus to concentrate on the flow of each tick. Choose a single instrument which has enough liquidity but is not among the most traded. Dangers of scalping say SPY or QQQQ or USDEUR is that they are traded by far too many traders and thus behavior is erratic.

**2. Fix your position size, spread size and loss size**

It comes without saying that in fast paced trading you don&#8217;t want to be dynamically changing Position Size. Based on your trading capital, appetite for risks, leverage and instrument&#8217;s volatility pre-determine how many ticks you can afford to lose, how many ticks you want to make and how long do you want to hold. These should be written in stone and adhered too.

**3. Analyse and Audit**

At the end of the day, do an audit of all the trades. See if all the trades were executed as it was planned, all intended Buys were Buys and not vice versa, Position size were what was planned to be. Plot and Graph the entries and exits, see if your mathematical knowledge could be exploited to make sense of what happened in the day.

&nbsp;

## <span style="text-decoration: underline;">The Intermediates</span>

**1. Multi-time frame Analysis**

When you watch the instrument, use different time frames. From &#8216;tick-plot&#8217;s, 1 sec, 5 sec, 15 sec, 30 sec, 1 min, 5 min and 10 min. Apart from these if your trading setup has multiple screens then it is not a bad idea to have longer time-frame charts, like 1 hr, 4 hr and 1-day and 3-day charts open for the longer term perspective. I must  apprise you of the caveat though, Multiple Time frame analysis will add more questions than answers, will probably make you skeptical of the current flow and direction as different time frames will be in discord among themselves. How you use it is your personal opinion, it all again boils down to two main different styles of trading viz. **Trend following vs Mean Reversion**. There is no scope here for the discussion on this subject, may be some other time. Interesting discussion on the <a title="trend vs mean reversion" href="http://www.traderslaboratory.com/forums/tech-analysis/10401-trend-following-vs-mean-reversion-trading.html" target="_blank">same is here</a>.

**2. The &#8216;hunch&#8217;/&#8217;feel&#8217; by logic and math**

Even with the risk of being ridiculed I am going to attempt to quantify and standardize what it means to be &#8216;**in-the-zone**&#8216;. For those of who are unaware of the trading faux pas which I am going to commit, it is that &#8216;the-zone&#8217; is considered to be the sacrosanct in the trading world. It is graciously accepted that with enough trading experience you will get there. As they say in redundant tautological statement &#8211; &#8220;you will get there when you will get there&#8221;.

Conjecture : **If you can distinguish your instrument from any other instrument with non-negligible accuracy, you are in the zone**

For my mathematical friends, it can be written as :

<img src='http://s0.wp.com/latex.php?latex=%5Cexists%5Cimath%3A%5Cforall%5Cjmath%5Cneq%5Cimath+Pr%5BQ%28i%29%3DQ%28j%29%5D%5Cleq%5Cfrac%7B1%7D%7B%5Cvarepsilon%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\exists\imath:\forall\jmath\neq\imath Pr[Q(i)=Q(j)]\leq\frac{1}{\varepsilon}' title='\exists\imath:\forall\jmath\neq\imath Pr[Q(i)=Q(j)]\leq\frac{1}{\varepsilon}' class='latex' /> 

where, <img src='http://s0.wp.com/latex.php?latex=Q%28.%29+&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='Q(.) ' title='Q(.) ' class='latex' /> is the function of predicting the given instrument&#8217;s time series and <img src='http://s0.wp.com/latex.php?latex=%5Cvarepsilon&#038;bg=ffffff&#038;fg=000000&#038;s=0' alt='\varepsilon' title='\varepsilon' class='latex' /> is the non-negligible factor (in the order of 10^-5)

So if by enough practice on any given day you can successfully break &#8220;<span style="text-decoration: underline;">The financial Turing test</span>&#8221; (see<a title="General read on Financial Turing Test" href="http://www.technologyreview.com/view/417818/scientists-develop-financial-turing-test/" target="_blank"> this for general read</a>, and <a title="Paper Financial Turing Test" href="http://arxiv.org/abs/1002.4592" target="_blank">this for the actual paper</a>) then you have gained the &#8216;**hunch**&#8216; or &#8216;**the feel**&#8216;.

## <span style="text-decoration: underline;">The Advanced</span>

**1. Quantification to achieve &#8216;the feel&#8217;**

Here are some of my mathematical tools you should be adept with to get &#8216;the feel&#8217;.

a) <span style="text-decoration: underline;">Volatility</span> pattern of the instrument.

b) <span style="text-decoration: underline;">De-trended</span> Chart of the same. (if instrument is Agri-product, remember to remove seasonal cycle influence too)

c) <span style="text-decoration: underline;">Co-integration</span> of the instrument with its peers, as in similar comatrix representation (*read Ganapathy on Pair Trading*)

d) <span style="text-decoration: underline;">Correlation</span> with all the influential instruments.

<p style="padding-left: 30px;">
  I find that novice traders read the correlation correctly but assimilate it incorrectly. Correlation doesn&#8217;t imply working &#8220;Pairs&#8221; (<em>for that you need Augumented Dickey Fuller Test</em>) and also correlation doesn&#8217;t guarantee cointegration and certainly doesn&#8217;t signify causation*. Correlation can (<em>with enough reliability</em>) only be used to determine the list of influential instruments.
</p>

*There may be some causation which implies correlation but assume otherwise until you know it to be true.

**2. Research to improve trading**

While understanding the instrument, its history, recent spikes, major players, major exchanges, underlying microeconomics etc cannot be under-emphasized there are enough work you can do to make your judgement sound.  In rare case where the instrument you scalp is not a universally traded high liquidity instrument, you can use techniques like probing (made popular by Richard Dennis), use of &#8216;Dark Pool&#8217; and certainly disguised orders *(if that is not illegal with your exchange). *There are other potential fundamental and sentimental research tools available (like social-mining etc). <a title="Social Science Research Network (SSRN)" href="http://www.ssrn.com/" target="_blank">SSRN is great repository for papers on financial mathematics.</a>

**3. Analysis of trades**

Your trades, PnL, and other 100 parameters associated with Trading stats are vital. Very vital when you are doing discretionary trading as those are the parameters which will guide you into optimizing your trades. Is there a pattern in losing trades, do you close trades too early or too late. How did you fare when X report was announced, what is the frequency of the trades which is optimal. Is there any emotional disadvantage with trading at higher leverage vs higher position size (with lower leverage). Are you always picking tops/bottom too early or may be too late ? With enough introspection and little of related literature study you will be able to ask more questions and answer them too.

## Conclusion

Even though discretionary trading is done more by the feel and hunch, you could surely augument your decision making by sound mathematical knowledge. Difference tools of mathematics can help you get that edge. Different people will have different results trading similar instrument while being exposed to equal information. Likes of Nassim Taleb would rather label it as being &#8216;Fooled by Randomness&#8217;, nonetheless there is enough evidence of failure of &#8216;Efficient Market Hypothesis&#8217;. Not all that comes from scalping but if done with enough discipline and adroit application of research it can be a profitable venture.