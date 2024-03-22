# installing flask using pip3
python::pip { 'flask':
  ensure   => '2.1.0',
  pkgname  => 'flask',
  provider => 'pip3',
}
