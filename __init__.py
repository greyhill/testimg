import pylab as pl
import os
import sys

def getimg(name):
    mypath = os.path.dirname(sys.modules['testimg'].__file__)
    try:
        return pl.imread(os.path.join(mypath, 'misc', '%s.tiff' % name))
    except:
        raise ValueError('unknown image name %s' % name)

def house(): return getimg('4.1.05')
def couple(): return getimg('4.1.02')
def jellybeans(): return getimg('4.1.07')
def splash(): return getimg('4.2.01')
def mandrill(): return getimg('4.2.03')
def lena(): return getimg('4.2.04')
def airplane(): return getimg('4.2.05')
def sailboats(): return getimg('4.2.06')
def peppers(): return getimg('4.2.07')
def boat(): return getimg('boat.512')
def man(): return getimg('5.3.01')
def cameraman(): return getimg('cameraman')
