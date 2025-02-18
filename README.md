# Visualizing Domestic Migration

This project visualizes domestic migration in Finland based on data from the [Statistics Finland](https://stat.fi/en) using Python. The running of the project in its entirety is currently rather clunky due to time restraints, and a current development focus. Packages are handled by [Poetry](https://python-poetry.org/).

Initialising the project from scratch is easy enough by running `main.py`. This validates the existence of the necessary data files and, finding them lacking, creates the necessary API requests to the stat.fi API. 
Based on this data, the scripts in `data_processing` can now be run. Each script performs one or multiple transformations necessary for the visualization of the data with the scripts available in visualization, with corresponding naming practices signifying the corresponding data_processing and visualization files.

As of the current state of the repository, all data for all visualizations should be available as is when cloning the repo, and pngs of the created visualizations available in `visualization/results`. Running the respective visualization files is, however, recommended - the matplotlib viewer provides the possibility to examine the results of each visualization in much finer detail than the simple .pngs in results.

Please note: this is a very experimental project. The author does not make any claims on the scientific accuracy of any of the results produced by running programs in this repo, nor does he take any stance, political or otherwise, on the actual matter of domestic migration in Finland.
This repo is merely intended for the completion of a class project related to a subject that the author found personally interesting, and related to which there were copious datasets available.

NB: This project stores data in .parquet, mainly due to personal grievances with .csv not maintaining data types. Many IDEs do not support viewing these by default. In case you wish to see the data in a tabular format, please use an appropriate viewer, or e.g. the VSCode parquet-viewer extension.