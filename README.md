Hello, world!

This is a repository visualizing domestic migration in Finland using Python and its libraries. A complete list of the libraries used in this project can be found at the bottom of this file, and it is recommended all are installed before attempting to run any of the code found in this repository.

As of the most recent edit to this readme, the running of the project in its entirety is unfortunately rather clunky due to time restraints. The next step in development is decomposing the methods in data_processing and visualization to feature less repeated code and a more OO approach, leading to a concise set of packages similar to the current api directory.

Nevertheles, initialising the project from scratch is easy enough by running main.py. This validates the existence of the necessary data files and, finding them lacking, creates the necessary API requests to the stat.fi API.
Based on this data, the files in data_processing can now be run. Each script performs one or multiple transformations necessary for the visualization of the data with the scripts available in visualization, with corresponding naming practices signifying the corresponding data_processing and visualization files.

As of the current state of the repository, all data for all visualizations should be available as is when cloning the repo, and pngs of the created visualizations available in visualization/results. Running the respective visualization files is, however, recommended - the matplotlib viewer provides the possibility to examine the results of each visualization in much finer detail than the simple .pngs in results.

Please note: this is a very experimental project. The author does not make any claims on the scientific accuracy of any of the results produced by running programs in this repo, nor does he take any stance, political or otherwise, on the actual matter of domestic migration in Finland.
This repo is merely intended for the completion of a class project related to a subject that the author found personally interesting, and related to which there were copious datasets available.

Peace and love,
@ihamuma

Libraries used in the project:
- pandas (duh)
- chardet (Finnish tax authority uses some random ass codec)
- csv-detective (Finnish tax authority uses some random ass separator)
- os
- requests
- pyarrow (for fun, to enable parquet file usage)
- matplotlib (thought I was too cool to ever use this - always good to be proven wrong!)
- seaborn (for sweet(er) visuals)
- numpy
- sklearn (for PCA)
- networkx (for, you know. graphs and stuff.)
- sammon (https://github.com/tompollard/sammon/)
- pillow (for graphical overlays of visualizations)

NB: This project stores data in .parquet, mainly due to personal grievances with .csv not maintaining data types. Many IDEs do not support viewing these by default. In case you wish to see the data in a tabular format, please use an appropriate viewer, or e.g. the VSCode parquet-viewer extension.