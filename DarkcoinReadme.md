Reecoin Electrum Keep it Simple Instructions
=============================================

Reecoind
-----------

* Reecoin.conf must have txindex=1 in it. After updating, you'll need to reindex.

electrum-reecoin-server
---------------------

* Create a directory /var/electrum-reecoin-server 
	$sudo mkdir /var/electrum-reecoin-server
* Chown the directory to the user you'll run the electrum-reecoin-server as. 
	$sudo chown user:user /var/electrum-reecoin-server
* Install x13_hash located in src/x13_hash 
	$cd src/x13_hash && sudo python setup.py install
*Install electrum-reecoin-server
	$sudo ./configure
	$sudo python setup.py install 

electrum-reecoin-server configuration
---------------------------------

*By default, the configuration file is located in /etc/electrum-reecoin.conf
*By defualt, the logfile is located in /var/log/electrum-reecoin.log 
*Check for both these files before attempting to run electrum-reecoin-server.
	If they do not exist, create them and chown them to the user you'll be using.




 


 
