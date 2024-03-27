# Puppet manifest to kill a process named "killmenow"
exec { 'terminate process':
  command  => 'pkill killmenow',
  provider => 'shell'
}
