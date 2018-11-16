# fin-projects



### PIP based

How-To: Building a Virtual [Python Environment](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment) : 
- 1. first build Virual env 

```
$ virtualenv -p python3 finenv
$ source finenv/bin/activate

```

- 2. do 'git clone <repo>'  from anohter 'TERMINAL' with out virual environment that will takecare

```
$ git clone <repo>

$ cd <repo-dir>
$ pip install -r requirements.txt   # will install in lib/python<ver>/site_packages/<package-name> in the TOP LEVEL ENV Dir

$ pip show <pkg-name>  # will show details ex..  'pandas' 
```

- 3. do your file edit with PyCharm, open <gitrepo-dir> folder with Pycharm , then commit there. You can also do command line GIT from Termimal which has no 'Virual ENV'
------------------------------------------
### CONDA bases

My Python Environment [Workflow with Conda](https://tdhopper.com/blog/my-python-environment-workflow-with-conda/) : if you want to use CONDA with 'NO PIP business' this seems the way
