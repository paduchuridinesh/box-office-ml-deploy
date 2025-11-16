package { 'python3-pip':
  ensure => installed,
}

exec { 'install_requirements':
  command => '/usr/bin/pip3 install -r /home/ubuntu/mlapp/requirements.txt --break-system-packages',
  refreshonly => false,
}

exec { 'start_app':
  command => 'nohup /usr/bin/python3 /home/ubuntu/mlapp/app.py > /home/ubuntu/app.log 2>&1 &',
  unless  => '/usr/bin/pgrep -f app.py',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
