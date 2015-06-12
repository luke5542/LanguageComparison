# Most of this should really go in a script...

FROM phusion/baseimage

MAINTAINER George Vanburgh

RUN \
  # Install the DLang repo
  curl http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -o /etc/apt/sources.list.d/d-apt.list && \
  apt-get update && \
  apt-get -y --allow-unauthenticated install -y --reinstall d-apt-keyring && \

  # Install the mono repo
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
  echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list && \
  echo "deb http://download.mono-project.com/repo/debian wheezy-apache24-compat main" | sudo tee -a /etc/apt/sources.list.d/mono-xamarin.list && \

  # Install Rust nightly image
  #add-apt-repository ppa:kevincantu/rust \
  apt-get update && \

  # Now actually install everything
  apt-get install -y --no-install-recommends \
    clang-3.5 \
    lua5.2 \
    openjdk-7-jdk \
    dmd-bin \
    g++ \
    nodejs \
    git \
    scala \
    ruby \
    python2.7-minimal \
    mono-devel \
    && \

  # Rust is special - so install that seperately
  curl -sf -L https://static.rust-lang.org/rustup.sh -o /tmp/rustup.sh && chmod +x /tmp/rustup.sh && \
  /bin/bash /tmp/rustup.sh -y && \
  rm -rf /usr/local/share/doc/rust && \


  # Symlink Clang
  ln /usr/bin/clang++-3.5 /usr/bin/clang++ && \

  # Symlink Node
  ln /usr/bin/nodejs /usr/bin/node && \

  # Now clean out the apt-get cache
  apt-get autoclean && apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN \
  # Download all the code
  cd /root && \
  git clone https://github.com/luke5542/LanguageComparison.git && \
  cd LanguageComparison && \
  ./compile-all

WORKDIR /root/LanguageComparison

CMD ["./run-all"]