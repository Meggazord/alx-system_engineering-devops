# Do the ssh configuration file
include stdlib
file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'HostKey ~/.ssh/school',
  match   => '^#?HostKey \/etc\/ssh\/ssh_host_rsa_key$',
  replace => true,
}
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication.+$',
  replace => true,
}
