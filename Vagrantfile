# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network :forwarded_port, guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider :virtualbox do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end

  # Use the apt-cache directory on the vagrant host if present
  # Create the following sub-directory in the project directory
  #   mkdir -p data/apt-cache/partial/
  if File.directory? File.expand_path "./data/apt-cache/partial/"
    config.vm.synced_folder "data/apt-cache", "/var/cache/apt/archives", :owner => "root", :group => "root"
  end

  config.vm.provision "shell",
    inline: <<-EOM
      apt-get -qq update
      apt-get -qy install python-software-properties
      add-apt-repository ppa:ubuntugis/ubuntugis-unstable
      apt-get -qq update
      apt-get -qy build-dep python-gdal python-numpy
      apt-get -qy install libgdal1h libgdal1-dev virtualenvwrapper
    EOM

end
