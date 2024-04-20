# Define a custom fact to retrieve the server's hostname

Facter.add('server_hostname') do
  setcode 'hostname'
end

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                server_name _;

                location / {
                    add_header X-Served-By $hostname;
                }
            }",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
