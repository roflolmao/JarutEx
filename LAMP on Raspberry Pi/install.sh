sudo apt install apache2
sudo a2enmode rewrite
sudo systemctl restart apache2
sudo chown -R pi:www-data /var/www/html
chmod -R 770 /var/www/html
sudo apt install  php
sudo apt install libapache2-mod-php
sudo service apache2 restart
cd /var/www/html
rm index.html
nano index.php
sudo apt install php-mysql
sudo service apache2 restart
