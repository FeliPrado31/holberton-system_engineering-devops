# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec { '/usr/bin/env apt-get -y update' : }
-> package { 'nginx':
  ensure => installed,
}

-> file { '/var/www/html/index.html' :
  content => 'Holberton School!',
}

-> file_line { '/etc/nginx/sites-available/default' :
  ensure => present,
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

-> service { 'nginx':
  ensure => running,
}