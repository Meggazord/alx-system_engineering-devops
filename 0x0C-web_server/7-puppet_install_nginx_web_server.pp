# File: 7-puppet_install_nginx_web_server.pp

package { 'nginx':
  ensure => installed,
}
file { '/var/www/html/index.html':
  content => 'Hello World!',
}
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
}

file { '/etc/nginx/sites-available/redirect_me':
  content => template('nginx/redirect_me.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}
nginx::resource::vhost { 'redirect_me':
  ensure => present,
  source => '/etc/nginx/sites-available/redirect_me',
}

