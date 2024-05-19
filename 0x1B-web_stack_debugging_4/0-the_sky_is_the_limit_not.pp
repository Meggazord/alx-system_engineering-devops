# 0-the_sky_is_the_limit_not.pp
# Increase Nginx's capacity to handle more requests by adjusting system and Nginx configurations

exec { 'increase_worker_processes':
  command     => "sed -i '/worker_processes/c\\worker_processes auto;' /etc/nginx/nginx.conf",
  path        => ['/bin', '/usr/bin'],
  unless      => "grep -q 'worker_processes auto;' /etc/nginx/nginx.conf",
}

exec { 'increase_file_descriptors':
  command     => "sed -i 's/worker_connections 1024/worker_connections 4096/' /etc/nginx/nginx.conf",
  path        => ['/bin', '/usr/bin'],
  unless      => "grep -q 'worker_connections 4096;' /etc/nginx/nginx.conf",
}

exec { 'adjust_client_buffers':
  command     => "sed -i 's/client_body_buffer_size 8k/client_body_buffer_size 32k/' /etc/nginx/nginx.conf",
  path        => ['/bin', '/usr/bin'],
  unless      => "grep -q 'client_body_buffer_size 32k;' /etc/nginx/nginx.conf",
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  path        => ['/usr/sbin', '/usr/bin', '/bin'],
  subscribe   => [ Exec['increase_worker_processes'], Exec['increase_file_descriptors'], Exec['adjust_client_buffers'] ],
  refreshonly => true,
}
