import math
import random
import numpy as np
import pandas as pd

def get_tree():
    '''
    manipulating the formula y = h+m/(exp(abs(x))) 
    using some random numbers and linear functions
    for h,m and the range of x (h->h(b),m->m(b),[x1,x2]->[x1,x(b)]),
    where b is a value representing a 'branch',
    we can re-create the shapeof a tree.
    '''

    # n leafs if the number of points in each branch
    nleafs= 1000
    max_leaf_size=3
    branch_step = 1/5
    nbranches = 10.0
    nballs = 70
    max_ball_size = 20

    # we create a series of 'master' lists with
    # x coordinates of the branch and the shade
    # y coordinate of the branch and the size of each point ('leaf')
    xtree,xshade,ytree,leaf_size = [],[],[],[]

    # we create a seriers of values used to "represent"
    # a branch of the tree. They will be used for 
    # furter calculations
    branch = np.arange(1.0,nbranches,branch_step)
    
    # we initialize the values 
    # x1,x2: bottom and top (of the three) maximum x coordinate of a branch
    # x3,x4: bottom and top (of the three) maximum x coordinate of the branch shade
    # m1,m2: bottom and top (of the three) slope of the branch
    x1,x2 = 0.3,0
    x3,x4 = 0.2,0
    m1,m2 = 0,20

    # shift is a parameter giving the vertical shift
    # of each branch. We can set it up to >1 if we want
    # a dynamic effect of superimposed branches.
    shift = 1
    for h in range(0,shift):
        
        # for each shift we create an empty list
        xs,xsh,ys,ls = [],[],[],[]

        for b in branch:

            # in order to create an effect of branches with length
            # that decreases along the tree (from top to bottom)
            # we linearly decrease the maximum x coordinate of the branch
            xtop = (b-branch[0])*(x2-x1)/(branch[-1]-branch[0])+x1
            
            # in order to have a less static cutoff we add to this max value
            # a random number that is a fraction of xtop. (A gaussian blurring
            # may also be applied, but I didn't test it).
            xtop = xtop+random.uniform(-abs(xtop),abs(xtop))/5

            # same procedure is applied to the shade
            shade = (b-branch[0])*(x4-x3)/(branch[-1]-branch[0])+x3
            shade = shade+random.uniform(-abs(shade),abs(shade))/5

            # also the slope of the branch is changed linearly along the tree.
            # this gives the effect of having a flat base to the tree
            # with more spiked top.
            m  = (b-branch[0])*(m2-m1)/(branch[-1]-branch[0])+m1

            for leaf in range(0,nleafs): 
                
                # draw a random number for each element x corrdinate
                x = random.uniform(-abs(xtop),abs(xtop))
                s = random.uniform(-abs(shade),abs(shade))
                # use our magic formula to obtain the y coordinate
                y = h+(m/math.exp(abs(x)))

                # append a list with the coordinates
                # assign also a variable size to each point
                xs.append(x)
                xsh.append(s)
                ys.append(y)
                ls.append(random.randint(1,max_leaf_size))

        # for each branch append the corresponding branch points
        # to the master list.
        xtree.append(xs)
        xshade.append(xsh)
        ytree.append(ys)
        leaf_size.append(ls)
    
    # we create the torso of the tree by
    # creating a series of vertical lines
    ytorso = list(np.arange(m1-1,m1,0.1))
    xrange,xstep,xtorso = 0.02,0.001,[]
    for t in np.arange(-xrange,xrange,xstep):
        x=[t for _ in ytorso]
        xtorso.append(x)

    # with the same procedure we can also
    # create a shade for the center of the tree
    ycenter = list(np.arange(m1,m2,0.1))
    xrange,xstep,xcenter = 0.004,0.0002,[]
    for t in np.arange(-xrange,xrange,xstep):
        x=[t for _ in ycenter]
        xcenter.append(x)
    
    # a list of plotly colors for the balls
    colors = ['firebrick','cornflowerblue','indigo','indigo','silver','gold','violet']
    
    ballsx,ballsy,size_ball,c = [],[],[],[]
    
    # we loop over the master list and for each set of 
    # coordinates and each we draw nballs random coordinate 
    for X,Y in zip(xtree,ytree):
        for i in range(0,nballs):
            b = random.randint(0,len(X))

            # if the coordinate is a little bit less than the top
            # (we want some space to put the star to the top)
            # we append the ball coordinate, the size and the
            # color (drawn randomly from the color list)
            if Y[b] < m-2:
                ballsx.append(X[b])
                ballsy.append(Y[b])
                size_ball.append(random.randint(5,max_ball_size))
                c.append(colors[random.randint(0,len(colors)-1)])

    # we define a dictionary to be returned. The format must be
    # json serializable for compatibility with Javascript.
    tree_dict = {
        'xtree':xtree,
        'xshade':xshade,
        'ytree':ytree,
        'xtorso':xtorso,
        'ytorso':ytorso,
        'xcenter':xcenter,
        'ycenter':ycenter,
        'xballs':ballsx,
        'yballs':ballsy,
        'leaf_size':leaf_size,
        'ball_size':size_ball,
        'ball_color':c
    }

    return tree_dict

def get_lights():
    'we represent the lights in the same way as we did for the tree'

    nbranches = 10
    branch_step = 1/5
    nlights = 200

    xlight,ylight,sizelist = [],[],[]

    # we create a seriers of values used to "represent"
    # a branch of the tree. They will be used for 
    # furter calculations
    branch = np.arange(1.0,nbranches,branch_step)

    # we initialize the values 
    # x1,x2: bottom and top (of the three) maximum x coordinate of a branch
    # m1,m2: bottom and top (of the three) slope of the branch
    x1,x2 = 0.3,0
    m1,m2 = 0,20

    # we aim in creating a set of 100 different light positions
    # and fill DatFrames with the information. We need a different
    # set to create the animation  
    for _ in range(0,100):
        # a dictionary is initialized for each set
        dict_light= {'x':[],'y':[] ,'size':[]}
        
        # we loop over the number of lights
        for _ in range(0,nlights):

            # draw a random branch and calculate the corresponding
            # coordinates and slope
            b = random.uniform(branch[0],branch[-1])
            xtop = (b-branch[0])*(x2-x1)/(branch[-1]-branch[0])+x1
            xtop = xtop+random.uniform(-abs(xtop),abs(xtop))/5
            m = (b-branch[0])*(m2-m1)/(branch[-1]-branch[0])+m1

            # use the magic formula to get the y coordinate
            x = random.uniform(-abs(xtop),abs(xtop))
            y = 1+(m/math.exp(abs(x)))

            # append the dict with the info
            # we fill only with the points that are not in the top
            # we want to live some space for the star 
            dict_light['x'].append(x)
            dict_light['y'].append(y)
            if y < (m2-3):
                dict_light['size'].append(random.randint(2,10))
            else:
                dict_light['size'].append(0)

        # append each set to the master list
        xlight.append(dict_light['x'])
        ylight.append(dict_light['y'])
        sizelist.append(dict_light['size'])

    # return 3 pandas DataFrames with x,y,size of the lights
    # each row represents a set 
    return pd.DataFrame(xlight),pd.DataFrame(ylight),pd.DataFrame(sizelist)