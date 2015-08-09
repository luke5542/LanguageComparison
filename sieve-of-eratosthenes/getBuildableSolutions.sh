#! /bin/bash

for dir in `find * -maxdepth 0 -type d -print`; do
  if make -s -i -C $dir checkdeps 2> /dev/null ; then
    echo $dir
  else
    :
  fi
done
