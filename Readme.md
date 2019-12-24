### Log Analysis reporting tool
it's a python program that answer some questions about database from analyzing data. the 3 questions the program answer is:

* What are the most popular three articles of all time?
*  Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?


### Installation
To run this program you have to install:

* Vagrant
* Python
* Python3

## Set up Vagrant
* install **virtual machine** [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
Note: Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

* install **vagrant** [here](Download it from vagrantup.com.)
Note:Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

* download and unzip this file [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

* Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

* When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

* Download the data from this link [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

* To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

* When you run vagrant with `vagrant ssh` and connect the database using `psql news`
you should create those **views** :

```
create view tresponses as select date(time), count(*) as responses from log group by date(time);
create view terrors as select date(time), count(*) as errors from log where status != '200 OK' group by date(time) order by date(time);
create view errors_prcentage as select to_char(tresponses.date, 'FMMon FMDD, YYYY'), ((errors*10000)/responses)*0.01 as percentage
from tresponses join terrors on tresponses.date=terrors.date order by percentage desc
```
* then  run the log-analysis.py file using this command into your vagrant  `python log-analysis.py`
