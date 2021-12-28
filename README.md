<img src="static/xmas_tree_cover.png">

# How to Draw a Christmas Tree with Python and Plotly
[![](https://img.shields.io/static/v1?label=%20&message=Jupyter%20Notebook&color=gray&logo=Jupyter)](https://github.com/gcgrossi/xmas_tree/blob/main/xmas_tree.ipynb)
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WskeMfLA8P0xbzzQwvrdapp3Z4YB89GW?usp=sharing)

The Christmas version of the episodes regarding my advendtures in the world of Data Science and Tech is focused on art: the Art of drawing something using some basic math, some for loops and a pinch of creativity. Today I'm going to draw a Christmas tree.

If I was a very cool Data Scientist or a Computer Vision specialist I would have probably trained a GAN and tried to generate some aproximation of thousand of example images of trees (something similar to 'this person does not exist').

But I'm a simple phyisicist coming from the old school of solving differential equations with pen and paper. So my version will be a mathematical version of a Christmas tree. 

I will use the function

$y = h+\frac{m}{e^{\lvert x \rvert}}$

Let's have a look at this function.

<img src="static/desmos-graph.png" width="30%">

Different values of $m$ will give different slope to the exponential function. It will also set the intersection with the y-axis equal to $m$. The parameter $h$ will shift the entire distribution by the same factor. 

Playing with these parameters will help us drawing our tree. Moreover, we can add some animations by using a Flask server that will serve a front-end html page. A Javascript AJAX call to the server will power the updates of the plot by using the Javascript version of the famous drawing library plotly.

Let's start! But before:

## Disclaimers

1. The following is just a visualisation game, useful to teach some math and basic python. It is not meant to be used outside these scopes.

2. Running the script is costly and not optimized. I didn't much care about time optmisation here. The resulting experience may therefore be slow/resource consuming.

