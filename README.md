# fin-projects


### Python 3 setup on a new Mac machine
- 1/ first install iTerm2 , Oh My Zsh by following exact steps on this post : [Jazz Up Your “ZSH” Terminal In Seven Steps  ](https://medium.freecodecamp.org/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38)
- 2/ Install Python 3 on Mac OS X : [follow exact steps](https://wsvincent.com/install-python3-mac/) . You get 'virtualenv' as part of python3 install.
- these 2 steps are enough, NOW go to  'PIP based'
- 
- I did not follow the below , but just for reference:
- Installing Development environment on macOS : well [maintained git repo](https://github.com/sb2nov/mac-setup) ,  web [site is here](https://sourabhbajaj.com/mac-setup/) , python [specific page](https://sourabhbajaj.com/mac-setup/Python/)

### PIP based

How-To: Building a Virtual [Python Environment](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment) : 
- 1/ first build Virual env 

```
$ virtualenv -p python3 finenv
$ source finenv/bin/activate

```

- 2/ do 'git clone <repo>'  from anohter 'TERMINAL' with out virual environment that will takecare

```
$ git clone <repo>

$ cd <repo-dir>
$ pip install -r requirements.txt   # will install in <finenv>/lib/python<ver>/site_packages/<package-name> in the TOP LEVEL ENV Dir

$ pip show <pkg-name>  # will show details ex..  'pandas' 
```

- 3/ do your file edit with PyCharm, open <gitrepo-dir> folder with Pycharm , then commit there. You can also do command line GIT from Termimal which has no 'Virual ENV'
------------------------------------------
### CONDA bases

My Python Environment [Workflow with Conda](https://tdhopper.com/blog/my-python-environment-workflow-with-conda/) : if you want to use CONDA with 'NO PIP business' this seems the way
    
