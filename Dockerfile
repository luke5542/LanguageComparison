FROM phusion/baseimage

RUN \
  # Install the DLang repo
  curl http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -o /etc/apt/sources.list.d/d-apt.list && \
  apt-get update && \
  apt-get -y --allow-unauthenticated install -y --reinstall d-apt-keyring && \

  # Install Oracle JRE 8 (maybe)
  # apt-get install -y python-software-properties && \
  # add-apt-repository ppa:webupd8team/java && \

  # Install Rust nightly image
  #add-apt-repository ppa:kevincantu/rust \
  apt-get update && \

  # Now actually install everything
  apt-get install -y --no-install-recommends \
    clang-3.5 \
    lua5.2 \
    openjdk-7-jdk \
    dmd-bin \
    # rust \
    g++ \
    nodejs \
    git \
    scala \
    ruby \
    python2.7-minimal \
    && \

  # Symlink Clang
  ln /usr/bin/clang++-3.5 /usr/bin/clang++ && \

  # Symlink Node
  ln /usr/bin/nodejs /usr/bin/node && \

  # Now clean out the apt-get cache
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN \
  # Download all the code
  cd /root && \
  git clone https://github.com/luke5542/LanguageComparison.git && \
  cd LanguageComparison && \
  ./compile-all

WORKDIR /root/LanguageComparison

CMD ["./run-all"]