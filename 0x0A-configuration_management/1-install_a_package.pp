# Include the python class with ez_setup enabled
class { 'python': ez_setup => true, }

# Use pip provider to install Flask 2.1.0
package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
}
