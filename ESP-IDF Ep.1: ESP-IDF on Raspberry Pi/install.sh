sudo apt update
sudo apt full-upgrade -y
sudo apt install python3 python3-pip -y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
sudo apt install -y \
git wget flex bison \
gperf python-setuptools \
cmake ninja-build ccache \
libffi-dev libssl-dev dfu-util
cd ~
git clone https://github.com/espressif/esp-idf.git esp-idf
cd esp-idf
git submodule update --init --recursive
cd esp-idf
../install.sh
../export.sh
."$HOME/esp-idf/export.sh"
sudo usermod -a -G dialout,tty $USER
