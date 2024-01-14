package { 'nginx':
  ensure => installed,
}

file {'/data/web_static/shared/':
  ensure => directory,
}

file {'/data/web_static/releases/test/':
  ensure => directory,
}

file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    HOLEBRITONIA School
  </body>
</html>'
}

file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/'
}

file {'/data/':
  ensure  => directory,
  recurse => true,
  group   =>'ubuntu',
  owner   => 'ubuntu'
}

file {'/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => 'server {
	listen 80;

	root /var/www/html;
				
	location /hbnb_static/ {
				alias /data/web_static/current/;
	}
}'
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  restart    => '/etc/init.d/nginx restart',
}
