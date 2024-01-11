#!/usr/bin/env bash
#iwaywa
sudo apt-get -y upgrade
sudo apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    HOLEBRITONIA School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "
server {
	listen 80;

	root /var/www/html;
				
	location /hbnb_static/ {
				alias /data/web_static/current/;
	}
}" | sudo tee "/etc/nginx/sites-enabled/default"
service nginx restart
