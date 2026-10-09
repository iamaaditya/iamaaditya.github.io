---
title: Visual Question Answering Demo in Python Notebook
date: 2016-04-04
post: true
---
<p>This is an online demo with explanation and tutorial on Visual Question Answering. This is not a naive or hello-world model, this model returns close to state-of-the-art without using any attention models, memory networks (other than LSTM) and fine-tuning, which are essential recipe for current best results.</p> <br />
<p>I have tried to explain different parts, and reasoning behind their choices. This is meant to be an interactive tutorial, feel free to change the model parameters and experiment. If you have latest graphics card execution time should be within a minute.</p>
<br />
<p>All the files required to run this ipython notebook can be obtained from</p>
<h4 id="https://github.com/iamaaditya/VQA_Demo">
 * <a href="https://github.com/iamaaditya/VQA_Demo">https://github.com/iamaaditya/VQA_Demo</a> <br />
 * <a href="https://github.com/iamaaditya/VQA_Demo/blob/master/Visual_Question_Answering_Demo_in_python_notebook.ipynb"> Jupyter Notebook on Github </a></p></h4>

Table of Contents
=================

  * [Visual Question Answering Demo and Tutorial](#)
    * [Load the libraries](#Load-the-libraries)
    * [Load the models and weights files](#Load-the-models-and-weights-files)
    * [Model Idea](#Model-Idea)
  * [Image features](#Image-features)
    * [Pretrained VGG Net (VGG-16)](#Pretrained-VGG-Net-(VGG-16))
    * [Compile the model](#Compile-the-model)
    * [Plot the Model](#Plot-the-Model)
    * [Extract Image features](#Extract-Image-features)
  * [Word Embeddings](#Word-Embeddings)
    * [Try the embeddings](#Try-the-embeddings)
  * [VQA Model](#VQA-Model)
    * [Asketh Away !](#Asketh-Away-!)
    * [ What vehicle is in the picture ? ](#-What-vehicle-is-in-the-picture-?-)
    * [Results](#Results)
  * [Demo with image URL](#Demo-with-image-URL)
    * [ What are they playing? ](#-What-are-they-playing?-)
    * [ Are they playing soccer? ](#-Are-they-playing-soccer?-)


<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    
    <!-- MathJax configuration -->
    
    <!-- End of mathjax configuration --></head>

  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Load-the-libraries">Load the libraries<a class="anchor-link" href="#Load-the-libraries">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">argparse</span>
<span class="kn">import</span> <span class="nn">cv2</span><span class="o">,</span> <span class="nn">spacy</span><span class="o">,</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">keras.models</span> <span class="kn">import</span> <span class="n">model_from_json</span>
<span class="kn">from</span> <span class="nn">keras.optimizers</span> <span class="kn">import</span> <span class="n">SGD</span>
<span class="kn">from</span> <span class="nn">sklearn.externals</span> <span class="kn">import</span> <span class="n">joblib</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Load-the-models-and-weights-files">Load the models and weights files<a class="anchor-link" href="#Load-the-models-and-weights-files">&#182;</a></h2><p>This does not load the models yet, but we are providing the files</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="c"># File paths for the model, all of these except the CNN Weights are </span>
<span class="c"># provided in the repo, See the models/CNN/README.md to download VGG weights</span>
<span class="n">VQA_model_file_name</span>      <span class="o">=</span> <span class="s">&#39;models/VQA/VQA_MODEL.json&#39;</span>
<span class="n">VQA_weights_file_name</span>   <span class="o">=</span> <span class="s">&#39;models/VQA/VQA_MODEL_WEIGHTS.hdf5&#39;</span>
<span class="n">label_encoder_file_name</span>  <span class="o">=</span> <span class="s">&#39;models/VQA/FULL_labelencoder_trainval.pkl&#39;</span>
<span class="n">CNN_weights_file_name</span>   <span class="o">=</span> <span class="s">&#39;models/CNN/vgg16_weights.h5&#39;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Model-Idea">Model Idea<a class="anchor-link" href="#Model-Idea">&#182;</a></h2><p>This uses a classical CNN-LSTM  model like shown below, where Image features and language features are computed separately and combined together and a multi-layer perceptron is trained on the combined features.</p>
<p>Similar models have been presented at following links, this work takes ideas from them.</p>
<ol>
<li><a href="https://github.com/abhshkdz/neural-vqa">https://github.com/abhshkdz/neural-vqa</a></li>
<li><a href="https://github.com/avisingh599/visual-qa">https://github.com/avisingh599/visual-qa</a></li>
<li><a href="https://github.com/VT-vision-lab/VQA_LSTM_CNN">https://github.com/VT-vision-lab/VQA_LSTM_CNN</a></li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="http://i.imgur.com/Za5P1ZZ.png"><a href="http://arxiv.org/pdf/1505.00468v4.pdf">Source</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Image-features">Image features<a class="anchor-link" href="#Image-features">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Pretrained-VGG-Net-(VGG-16)">Pretrained VGG Net (VGG-16)<a class="anchor-link" href="#Pretrained-VGG-Net-(VGG-16)">&#182;</a></h2><p>While VGG Net is not the best CNN model for image features, GoogLeNet (winner 2014) and ResNet (winner 2015) have superior classification scores, but VGG Net is very versatile, simple, relatively small and more importantly portable to use.</p>
<p>For reference here is the VGG 16 performance on ILSVRC-2012
<img src="http://www.robots.ox.ac.uk/~vgg/research/very_deep/images/table_ILSVRC.png"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Compile-the-model">Compile the model<a class="anchor-link" href="#Compile-the-model">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">get_image_model</span><span class="p">(</span><span class="n">CNN_weights_file_name</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; Takes the CNN weights file, and returns the VGG model update </span>
<span class="sd">    with the weights. Requires the file VGG.py inside models/CNN &#39;&#39;&#39;</span>
    <span class="kn">from</span> <span class="nn">models.CNN.VGG</span> <span class="kn">import</span> <span class="n">VGG_16</span>
    <span class="n">image_model</span> <span class="o">=</span> <span class="n">VGG_16</span><span class="p">(</span><span class="n">CNN_weights_file_name</span><span class="p">)</span>

    <span class="c"># this is standard VGG 16 without the last two layers</span>
    <span class="n">sgd</span> <span class="o">=</span> <span class="n">SGD</span><span class="p">(</span><span class="n">lr</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span> <span class="n">decay</span><span class="o">=</span><span class="mf">1e-6</span><span class="p">,</span> <span class="n">momentum</span><span class="o">=</span><span class="mf">0.9</span><span class="p">,</span> <span class="n">nesterov</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="c"># one may experiment with &quot;adam&quot; optimizer, but the loss function for</span>
    <span class="c"># this kind of task is pretty standard</span>
    <span class="n">image_model</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">optimizer</span><span class="o">=</span><span class="n">sgd</span><span class="p">,</span> <span class="n">loss</span><span class="o">=</span><span class="s">&#39;categorical_crossentropy&#39;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">image_model</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Plot-the-Model">Plot the Model<a class="anchor-link" href="#Plot-the-Model">&#182;</a></h2><p>Keras has a function which allows you to visualize the model in block diagram. Let's do it !</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">keras.utils.visualize_util</span> <span class="kn">import</span> <span class="n">plot</span>
<span class="n">model_vgg</span> <span class="o">=</span> <span class="n">get_image_model</span><span class="p">(</span><span class="n">CNN_weights_file_name</span><span class="p">)</span>
<span class="n">plot</span><span class="p">(</span><span class="n">model_vgg</span><span class="p">,</span> <span class="n">to_file</span><span class="o">=</span><span class="s">&#39;model_vgg.png&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://raw.githubusercontent.com/iamaaditya/VQA_Demo/master/model_vgg.png"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Extract-Image-features">Extract Image features<a class="anchor-link" href="#Extract-Image-features">&#182;</a></h2><p>Extracting image features involves, taking a raw image, and running it through the model, until we reach the last layer. In this case our model is not 100% same as VGG Net, because we are not going to use the last two layer of the VGG. It is because the last layer of VGG Net is a 1000 way softmax and the second last layer is the Dropout.</p>
<p>Thus we are extracting the 4096 Dimension image features from VGG-16</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">get_image_features</span><span class="p">(</span><span class="n">image_file_name</span><span class="p">,</span> <span class="n">CNN_weights_file_name</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; Runs the given image_file to VGG 16 model and returns the </span>
<span class="sd">    weights (filters) as a 1, 4096 dimension vector &#39;&#39;&#39;</span>
    <span class="n">image_features</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4096</span><span class="p">))</span>
    <span class="c"># Magic_Number = 4096  &gt; Comes from last layer of VGG Model</span>

    <span class="c"># Since VGG was trained as a image of 224x224, every new image</span>
    <span class="c"># is required to go through the same transformation</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">cv2</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">image_file_name</span><span class="p">),</span> <span class="p">(</span><span class="mi">224</span><span class="p">,</span> <span class="mi">224</span><span class="p">))</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">im</span><span class="o">.</span><span class="n">transpose</span><span class="p">((</span><span class="mi">2</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="c"># convert the image to RGBA</span>

    
    <span class="c"># this axis dimension is required because VGG was trained on a dimension</span>
    <span class="c"># of 1, 3, 224, 224 (first axis is for the batch size</span>
    <span class="c"># even though we are using only one image, we have to keep the dimensions consistent</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">expand_dims</span><span class="p">(</span><span class="n">im</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span> 

    <span class="n">image_features</span><span class="p">[</span><span class="mi">0</span><span class="p">,:]</span> <span class="o">=</span> <span class="n">get_image_model</span><span class="p">(</span><span class="n">CNN_weights_file_name</span><span class="p">)</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">im</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">image_features</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Word-Embeddings">Word Embeddings<a class="anchor-link" href="#Word-Embeddings">&#182;</a></h1><p>The question has to be converted into some form of word embeddings. Most popular is Word2Vec whereas these days state of the art uses <a href="https://github.com/ryankiros/skip-thoughts">skip-thought vectors</a> or <a href="https://en.wikipedia.org/wiki/Encoding_(memory)#Sequence_memory">positional encodings.</a></p>
<p>We will use Word2Vec from Stanford called <a href="http://nlp.stanford.edu/projects/glove/">Glove</a>. Glove reduces a given token into a 300 dimensional representation.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">get_question_features</span><span class="p">(</span><span class="n">question</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; For a given question, a unicode string, returns the time series vector</span>
<span class="sd">    with each word (token) transformed into a 300 dimension representation</span>
<span class="sd">    calculated using Glove Vector &#39;&#39;&#39;</span>
    <span class="n">word_embeddings</span> <span class="o">=</span> <span class="n">spacy</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&#39;en&#39;</span><span class="p">,</span> <span class="n">vectors</span><span class="o">=</span><span class="s">&#39;en_glove_cc_300_1m_vectors&#39;</span><span class="p">)</span>
    <span class="n">tokens</span> <span class="o">=</span> <span class="n">word_embeddings</span><span class="p">(</span><span class="n">question</span><span class="p">)</span>
    <span class="n">question_tensor</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">tokens</span><span class="p">),</span> <span class="mi">300</span><span class="p">))</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">tokens</span><span class="p">)):</span>
            <span class="n">question_tensor</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="n">j</span><span class="p">,:]</span> <span class="o">=</span> <span class="n">tokens</span><span class="p">[</span><span class="n">j</span><span class="p">]</span><span class="o">.</span><span class="n">vector</span>
    <span class="k">return</span> <span class="n">question_tensor</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Try-the-embeddings">Try the embeddings<a class="anchor-link" href="#Try-the-embeddings">&#182;</a></h2><p>Let's see the embeddings, and their usage with sample words like this -</p>
<ol>
<li>Obama </li>
<li>Putin</li>
<li>Banana</li>
<li>Monkey</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">word_embeddings</span> <span class="o">=</span> <span class="n">spacy</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s">&#39;en&#39;</span><span class="p">,</span> <span class="n">vectors</span><span class="o">=</span><span class="s">&#39;en_glove_cc_300_1m_vectors&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">obama</span> <span class="o">=</span> <span class="n">word_embeddings</span><span class="p">(</span><span class="s">u&quot;obama&quot;</span><span class="p">)</span>
<span class="n">putin</span> <span class="o">=</span> <span class="n">word_embeddings</span><span class="p">(</span><span class="s">u&quot;putin&quot;</span><span class="p">)</span>
<span class="n">banana</span> <span class="o">=</span> <span class="n">word_embeddings</span><span class="p">(</span><span class="s">u&quot;banana&quot;</span><span class="p">)</span>
<span class="n">monkey</span> <span class="o">=</span> <span class="n">word_embeddings</span><span class="p">(</span><span class="s">u&quot;monkey&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">obama</span><span class="o">.</span><span class="n">similarity</span><span class="p">(</span><span class="n">putin</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[25]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.43514112534149385</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">obama</span><span class="o">.</span><span class="n">similarity</span><span class="p">(</span><span class="n">banana</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[26]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.17831375020636123</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">banana</span><span class="o">.</span><span class="n">similarity</span><span class="p">(</span><span class="n">monkey</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[27]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.45207779162154438</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As we can see, obama and putin are very similar in representation than obama and banana. This shows you there is some semantic knowledge of the tokens embedded in the 300 dimensional representation. We can do cool arithmetics with these word2vec like 'Queen' - 'King' + 'Boy' = 'Girl'. See <a href="http://multithreaded.stitchfix.com/blog/2015/03/11/word-is-worth-a-thousand-vectors/">this blog post</a> for more details.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="VQA-Model">VQA Model<a class="anchor-link" href="#VQA-Model">&#182;</a></h2><p>VQA is a simple model which combines features from Image and Word Embeddings and runs a multiple layer perceptron.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">get_VQA_model</span><span class="p">(</span><span class="n">VQA_model_file_name</span><span class="p">,</span> <span class="n">VQA_weights_file_name</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; Given the VQA model and its weights, compiles and returns the model &#39;&#39;&#39;</span>

    <span class="c"># thanks the keras function for loading a model from JSON, this becomes</span>
    <span class="c"># very easy to understand and work. Alternative would be to load model</span>
    <span class="c"># from binary like cPickle but then model would be obfuscated to users</span>
    <span class="n">vqa_model</span> <span class="o">=</span> <span class="n">model_from_json</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="n">VQA_model_file_name</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
    <span class="n">vqa_model</span><span class="o">.</span><span class="n">load_weights</span><span class="p">(</span><span class="n">VQA_weights_file_name</span><span class="p">)</span>
    <span class="n">vqa_model</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">loss</span><span class="o">=</span><span class="s">&#39;categorical_crossentropy&#39;</span><span class="p">,</span> <span class="n">optimizer</span><span class="o">=</span><span class="s">&#39;rmsprop&#39;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">vqa_model</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">keras.utils.visualize_util</span> <span class="kn">import</span> <span class="n">plot</span>
<span class="n">model_vqa</span> <span class="o">=</span> <span class="n">get_VQA_model</span><span class="p">(</span><span class="n">VQA_model_file_name</span><span class="p">,</span> <span class="n">VQA_weights_file_name</span><span class="p">)</span>
<span class="n">plot</span><span class="p">(</span><span class="n">model_vqa</span><span class="p">,</span> <span class="n">to_file</span><span class="o">=</span><span class="s">&#39;model_vqa.png&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://raw.githubusercontent.com/iamaaditya/VQA_Demo/master/model_vqa.png"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As it can be seen above the model also runs a 3 layered LSTM on the word embeddings. To get a naive result it is sufficient to feed the word embeddings directly to the merge layer, but as mentioned above the model gives close to the state-of-the-art results.</p>
<p>Also, four layers of fully connected layers might not be required to achieve a good enough results. But I settled on this model after some experimentation, and this model's results beat those obtained using only few layers.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Asketh-Away-!">Asketh Away !<a class="anchor-link" href="#Asketh-Away-!">&#182;</a></h2><p>Let's give a test image and a question</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[69]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">image_file_name</span> <span class="o">=</span> <span class="s">&#39;test.jpg&#39;</span>
<span class="n">question</span> <span class="o">=</span> <span class="s">u&quot;What vehicle is in the picture?&quot;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-What-vehicle-is-in-the-picture-?-"> What vehicle is in the picture ? <a class="anchor-link" href="#-What-vehicle-is-in-the-picture-?-">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://raw.githubusercontent.com/iamaaditya/VQA_Demo/master/test.jpg"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="c"># get the image features</span>
<span class="n">image_features</span> <span class="o">=</span> <span class="n">get_image_features</span><span class="p">(</span><span class="n">image_file_name</span><span class="p">,</span> <span class="n">CNN_weights_file_name</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="c"># get the question features</span>
<span class="n">question_features</span> <span class="o">=</span> <span class="n">get_question_features</span><span class="p">(</span><span class="n">question</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">y_output</span> <span class="o">=</span> <span class="n">model_vqa</span><span class="o">.</span><span class="n">predict</span><span class="p">([</span><span class="n">question_features</span><span class="p">,</span> <span class="n">image_features</span><span class="p">])</span>

<span class="c"># This task here is represented as a classification into a 1000 top answers</span>
<span class="c"># this means some of the answers were not part of training and thus would </span>
<span class="c"># not show up in the result.</span>
<span class="c"># These 1000 answers are stored in the sklearn Encoder class</span>
<span class="n">labelencoder</span> <span class="o">=</span> <span class="n">joblib</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">label_encoder_file_name</span><span class="p">)</span>
<span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">y_output</span><span class="p">)[</span><span class="mi">0</span><span class="p">,</span><span class="o">-</span><span class="mi">5</span><span class="p">:]):</span>
    <span class="k">print</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">y_output</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="n">label</span><span class="p">]</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">),</span> <span class="s">&quot;% &quot;</span><span class="p">,</span> <span class="n">labelencoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>78.32 %  train
01.11 %  truck
00.98 %  passenger
00.95 %  fire truck
00.68 %  bus
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Results">Results<a class="anchor-link" href="#Results">&#182;</a></h2><p>I am copying the output of the previous command, so that you can validate if your results are same as mine.</p>
<p><strong>78.32 %  train</strong> <br />
01.11 %  truck <br />
00.98 %  passenger <br />
00.95 %  fire truck <br />
00.68 %  bus <br /></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Demo-with-image-URL">Demo with image URL<a class="anchor-link" href="#Demo-with-image-URL">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Since cv2.imread cannot read an image from URL we will have to change our function <code>get_image_features</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">get_image_features</span><span class="p">(</span><span class="n">image_file_name</span><span class="p">,</span> <span class="n">CNN_weights_file_name</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; Runs the given image_file to VGG 16 model and returns the </span>
<span class="sd">    weights (filters) as a 1, 4096 dimension vector &#39;&#39;&#39;</span>
    <span class="n">image_features</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4096</span><span class="p">))</span>
        
    <span class="kn">from</span> <span class="nn">skimage</span> <span class="kn">import</span> <span class="n">io</span>
    <span class="c"># if you would rather not install skimage, then use cv2.VideoCapture which can read from URL</span>
    <span class="c"># see this http://answers.opencv.org/question/16385/cv2imread-a-url/?answer=16389#post-id-16389</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">io</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">image_file_name</span><span class="p">),</span> <span class="p">(</span><span class="mi">224</span><span class="p">,</span> <span class="mi">224</span><span class="p">))</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">im</span><span class="o">.</span><span class="n">transpose</span><span class="p">((</span><span class="mi">2</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="c"># convert the image to RGBA</span>

    
    <span class="c"># this axis dimension is required because VGG was trained on a dimension</span>
    <span class="c"># of 1, 3, 224, 224 (first axis is for the batch size</span>
    <span class="c"># even though we are using only one image, we have to keep the dimensions consistent</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">expand_dims</span><span class="p">(</span><span class="n">im</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span> 

    <span class="n">image_features</span><span class="p">[</span><span class="mi">0</span><span class="p">,:]</span> <span class="o">=</span> <span class="n">get_image_model</span><span class="p">(</span><span class="n">CNN_weights_file_name</span><span class="p">)</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">im</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">image_features</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[61]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">image_file_name</span> <span class="o">=</span> <span class="s">&quot;http://www.newarkhistory.com/indparksoccerkids.jpg&quot;</span>
<span class="c"># get the image features</span>
<span class="n">image_features</span> <span class="o">=</span> <span class="n">get_image_features</span><span class="p">(</span><span class="n">image_file_name</span><span class="p">,</span> <span class="n">CNN_weights_file_name</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Feel free to change that url to any valid image, it can be any image format. Also try to use websites which have higher bandwidth</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="http://www.newarkhistory.com/indparksoccerkids.jpg"></p>
<h1 id="-What-are-they-playing?-"> What are they playing? <a class="anchor-link" href="#-What-are-they-playing?-">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[62]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">question</span> <span class="o">=</span> <span class="s">u&quot;What are they playing?&quot;</span>

<span class="c"># get the question features</span>
<span class="n">question_features</span> <span class="o">=</span> <span class="n">get_question_features</span><span class="p">(</span><span class="n">question</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[63]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">y_output</span> <span class="o">=</span> <span class="n">model_vqa</span><span class="o">.</span><span class="n">predict</span><span class="p">([</span><span class="n">question_features</span><span class="p">,</span> <span class="n">image_features</span><span class="p">])</span>

<span class="n">labelencoder</span> <span class="o">=</span> <span class="n">joblib</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">label_encoder_file_name</span><span class="p">)</span>
<span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">y_output</span><span class="p">)[</span><span class="mi">0</span><span class="p">,</span><span class="o">-</span><span class="mi">5</span><span class="p">:]):</span>
    <span class="k">print</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">y_output</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="n">label</span><span class="p">]</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">),</span> <span class="s">&quot;% &quot;</span><span class="p">,</span> <span class="n">labelencoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>40.52 %  tennis
28.45 %  soccer
17.88 %  baseball
11.67 %  frisbee
00.15 %  football
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Result">Result<a class="anchor-link" href="#Result">&#182;</a></h2><p>Copying the result to validate your output.</p>
<p><strong>40.52 %  tennis </strong><br />
28.45 %  soccer <br />
17.88 %  baseball <br />
11.67 %  frisbee <br />
00.15 %  football <br /></p>
<p>As you can see, it got this wrong, but you can see why it could be harder to guess soccer and easier to guess tennis, lack of soccer ball and double lines at the edge.</p>
<p>Let's ask another question for the same image.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[67]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">question</span> <span class="o">=</span> <span class="s">u&quot;Are they playing soccer?&quot;</span>

<span class="c"># get the question features</span>
<span class="n">question_features</span> <span class="o">=</span> <span class="n">get_question_features</span><span class="p">(</span><span class="n">question</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="http://www.newarkhistory.com/indparksoccerkids.jpg"></p>
<h1 id="-Are-they-playing-soccer?-"> Are they playing soccer? <a class="anchor-link" href="#-Are-they-playing-soccer?-">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[68]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">y_output</span> <span class="o">=</span> <span class="n">model_vqa</span><span class="o">.</span><span class="n">predict</span><span class="p">([</span><span class="n">question_features</span><span class="p">,</span> <span class="n">image_features</span><span class="p">])</span>

<span class="n">labelencoder</span> <span class="o">=</span> <span class="n">joblib</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">label_encoder_file_name</span><span class="p">)</span>
<span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">y_output</span><span class="p">)[</span><span class="mi">0</span><span class="p">,</span><span class="o">-</span><span class="mi">5</span><span class="p">:]):</span>
    <span class="k">print</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">y_output</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="n">label</span><span class="p">]</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">),</span> <span class="s">&quot;% &quot;</span><span class="p">,</span> <span class="n">labelencoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>93.15 %  yes
06.42 %  no
00.02 %  right
00.01 %  left
000.0 %  man
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Result">Result<a class="anchor-link" href="#Result">&#182;</a></h2><p><strong>93.15 %  yes </strong><br />
06.42 %  no <br />
00.02 %  right <br />
00.01 %  left <br />
000.0 %  man <br /></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As you can see, similar information about a Yes/No question elicits different response, or should I say correct response. This is an impertinent problem with <code>classification</code> tasks.</p>
<p>Feel free to experiment with different types of questions, <code>count</code>, <code>color</code>, <code>location</code>.</p>
<p>More interesting results are obtained when one takes a different crop of a image, instead of just scaling it to 224x224. This is again because we extract only the top level features of CNN model which was trained to classify one object in the image.</p>

</div>
</div>
</div>
    </div>
  </div>

