# puppet file to install custom http_response_header

exec { 'apt_update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
  ensure => installed,
}

$nginx_config_content = @(EOF)
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
        add_header X-Served-By $hostname;
    }
}
EOF

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $nginx_config_content,
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}


exec { 'apt_update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
  ensure => installed,
}

$hostname = $facts['hostname']
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
        add_header X-Served-By ${hostname};
    }
}",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}
