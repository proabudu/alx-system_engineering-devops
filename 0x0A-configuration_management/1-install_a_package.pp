# Ensure pip3 is installed before trying to install Flask

package
{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
