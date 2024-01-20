# install_flask.pp

# Ensure the package 'python3-pip' is installed (if not already installed) { 'python3-pip':
  ensure => installed,
}

# Use pip3 to install Flask version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}
