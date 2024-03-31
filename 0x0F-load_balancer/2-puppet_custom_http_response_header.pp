# 2-puppet_custom_http_response_header.pp

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
