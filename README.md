# Steam Recommender System
A recommender system based on Collaborative Filtering (Pearson's Similarity Coefficient) from datasets of the Steam userbase.

Pandas was used for most of the data manipulation with some string functions used for non-unicode, non-alphanumeric text cleaning. Additionally, Flask and JS was used for the front-end.

## __Data Wrangling__
Two datasets were used in the making of this recommender system. The first was [Steam Games Dataset](https://www.kaggle.com/nikdavis/steam-store-games) from Kaggle. This was required to identify the game names to their application ids since the other dataset, which contained implicit ratings in the form of hours played by a user per game, did not contain the application ids. The user dataset is also sourced from Kaggle [here](https://www.kaggle.com/tamber/steam-video-games).

#### __Implicit Ratings__
The user dataset had data of each user <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;$x$" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;$x$" title="\large $x$" /></a> playing a game <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;$y$" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;$y$" title="\large $y$" /></a> for <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;$z$" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;$z$" title="\large $z$" /></a> hours. What I did was convert the implicit rating *hours played* to an explicit rating on a scale from 1 to 5.

This was achieved simply by mapping the ratings linearly to  the range <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;[0,\frac{4}{5}\bar{z}]" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;[0,\frac{4}{5}\bar{z}]" title="\large [0,\frac{4}{5}\bar{z}]" /></a> where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;\bar{z}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;\bar{z}" title="\large \bar{z}" /></a> is the average number of hours game <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;$y$" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;$y$" title="\large $y$" /></a> is played across the whole dataset.

#### __Endpoint Dataset__
This dataset is generated using an inner join of the appid of the gamee in our dataset to the media dataset containing header images for the games. This dataset is used to retreive media images for the front-end in browser.

## __Front End__
The front end is made using HTML/CSS and the fetch API and Flask on the Python side. The process is generally straightforward but not without its hiccups as this was my first time implementing cross-communication between the front-end and the back-end.

## To Run
Simply clone the repository, the code from *main.ipynb* has been copied into *website.py* due to Flask requirements. 

* Run *website.py*
* Open src/templates/index.html in Chrome with "--disable-web-security --user-data-dir=~/chromeTemp" launch options set and running as admin.
* Just pick your games and rate them 5 for *__LOVED IT__* and 1 for __*HATED IT*__
* See what games are next on your ever-increasing backlog that you will never play because you are too busy reading READMEs to the very end. Come on now, no shame in admitting it...
