#!/usr/bin/env bash
#iwaywa
sudo apt-get -y upgrade
sudo atp-get install -y nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    HOLEBRITONIA School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "server {
				listen 80;

				root /var/www/html;
				
				location /hbnb_statc/ {
								alias /data/web_static/current/;
				}
}" | sudo tee "/etc/nginx/sites-available/default"
service nginx restart
