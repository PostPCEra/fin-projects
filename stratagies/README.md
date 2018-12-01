

#### 1. alpha_vantage : Python module to get stock data/cryptocurrencies [from the Alpha Vantage APi](https://github.com/RomelTorres/alpha_vantage)

- alpha vantage is installed as part of pip install -r requirements.txt and is saved in lib/python../site_pacakges/alpha*

- extlibs dir has  ta.py , ta2.py and util.py that are copied from [from the project](https://github.com/bukosabino/financial-forecasting-challenge-gresearch)


####  2. Jypypter notebook instructions
-  $ ./start-jupyter    # will start server, in this file first 2 lines are configs, last one starts server. These are taken from the post below.
-
- [Jupyter Notebook Tricks for Data Science that Enhance your efficiency](https://codeburst.io/jupyter-notebook-tricks-for-data-science-that-enhance-your-efficiency-95f98d3adee4)
-
- http://localhost:8888/nbextensions   # open browser /w URL will show all extensions 
- Enable the following Hinterland extension # 
- Hinterland : Enable code autocompletion menu for every keypress in a code cell, instead of only enabling it with tab


 - $ jupyter notbook   #  this is to start without all the above extensions etc..
 
 -  paste in chrome browser http://localhost:8888/tree ( or URL displayed on Treminal when above cmd statred)
 - $ jupyter --paths   # show various paths jupyter is installed 
 - $ jupyter notebook --generate-config   # will generate config file ~/.jupyter/jupyter_notebook_config.py
 - edit the file as follows ( last one not working, open chrome and paste URL as said above)
 ```
 c.NotebookApp.notebook_dir = './'
 c.NotebookApp.open_browser = True
 c.NotebookApp.browser = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
 ```
 - 
 - 'CTRL-C' to stop jyper server 
 - arrow keys on the board to move to nex CELL
 - up/down keys on TOP header of browser in notebook, to physically move CELLS
 - only LAST statement in the CELL print output, so have only ONE output per CELL