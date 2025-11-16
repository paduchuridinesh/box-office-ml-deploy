package { 'python3-pip':
  ensure => installed,
}

exec { 'install_requirements':
  command => '/usr/bin/pip3 install -r /home/ubuntu/mlapp/requirements.txt',
  refreshonly => false,
}

exec { 'start_app':
  command => 'nohup python3 /home/ubuntu/mlapp/app.py > /home/ubuntu/app.log 2>&1 &',
  unless  => 'pgrep -f app.py',
}
