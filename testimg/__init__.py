import pylab as pl
import os
import sys

def grayscale(img):
    if len(img.shape) == 2 or img.shape[2] == 1:
        # already grayscale
        return img
    else:
        # lifted from MATLAB
        return    img[:,:,0] * .2989 \
                + img[:,:,1] * .5770 \
                + img[:,:,2] * .1140;

def getimg(name, force_gray = False):
    mypath = os.path.dirname(sys.modules['testimg'].__file__)
    path = os.path.join(mypath, 'misc', '%s.tiff' % name)
    tr = pl.imread(path)
    if force_gray:
        return grayscale(tr)
    else:
        return tr

def house(force_gray = False): return getimg('4.1.05', force_gray)
def couple(force_gray = False): return getimg('4.1.02', force_gray)
def jellybeans(force_gray = False): return getimg('4.1.07', force_gray)
def splash(force_gray = False): return getimg('4.2.01', force_gray)
def mandrill(force_gray = False): return getimg('4.2.03', force_gray)
def lena(force_gray = False): return getimg('4.2.04', force_gray)
def airplane(force_gray = False): return getimg('4.2.05', force_gray)
def sailboats(force_gray = False): return getimg('4.2.06', force_gray)
def peppers(force_gray = False): return getimg('4.2.07', force_gray)
def boat(force_gray = False): return getimg('boat.512', force_gray)
def man(force_gray = False): return getimg('5.3.01', force_gray)
def cameraman(force_gray = False): return getimg('cameraman', force_gray)
def al(force_gray = False): return getimg('al', force_gray)
def tools(force_gray = False): return getimg('tools', force_gray)

