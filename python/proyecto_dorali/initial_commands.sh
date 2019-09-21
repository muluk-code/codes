Python 3.7
apt-get install -y python3
apt-get install -y python3-tk
apt-get install -y build-essential
apt-get install -y checkinstall
apt-get install -y libreadline-gplv2-dev
apt-get install -y libncursesw5-dev
apt-get install -y libssl-dev
apt-get install -y libsqlite3-dev
apt-get install -y tk-dev
apt-get install -y libgdbm-dev
apt-get install -y libc6-dev
apt-get install -y libbz2-dev
apt-get install -y zlib1g-dev
apt-get install -y openssl
apt-get install -y libffi-dev
apt-get install -y python3-dev
apt-get install -y python3-setuptools
apt-get install -y wget
sudo apt-get install git
#temporal
mkdir /tmp/Python37
cd /tmp/Python37
#descarga, descomprime,configura y empaqueta
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xvf Python-3.7.0.tar.xz
cd /tmp/Python37/Python-3.7.0
./configure
make altinstall
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1 linux64.tar.gz
ckoDriver-Install
tar -xvzf geckodriver-v0.19.1-linux64.tar.gz
rm geckodriver-v0.19.1-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/

              
