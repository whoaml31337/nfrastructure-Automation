# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # Global Vagrant configuration
    config.vm.box = "ubuntu/focal64"
    
    # Disable automatic box update checking
    config.vm.box_check_update = false
  
    # Application Server Configuration
    config.vm.define "app-server" do |app|
      # Network configuration
      app.vm.network "private_network", ip: "192.168.56.10"
      app.vm.network "forwarded_port", guest: 8000, host: 8000   # App port
      app.vm.network "forwarded_port", guest: 9100, host: 9100   # Node exporter
      
      # Provisioning script
      app.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y rsync openssh-server
        sudo systemctl restart ssh
      SHELL
      
      # VirtualBox provider settings
      app.vm.provider "virtualbox" do |vb|
        vb.name = "app-server"
        vb.memory = 1024
        vb.cpus = 1
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      end
    end
  
    # Monitoring Server Configuration
    config.vm.define "monitoring-server" do |mon|
      # Network configuration
      mon.vm.network "private_network", ip: "192.168.56.20"
      mon.vm.network "forwarded_port", guest: 3000,  host: 3000    # Grafana
      mon.vm.network "forwarded_port", guest: 9090,  host: 9090    # Prometheus
      mon.vm.network "forwarded_port", guest: 9093,  host: 9093    # Alertmanager
      
      # Provisioning script
      mon.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y rsync openssh-server
        sudo systemctl restart ssh
      SHELL
      
      # VirtualBox provider settings
      mon.vm.provider "virtualbox" do |vb|
        vb.name = "monitoring-server"
        vb.memory = 1024
        vb.cpus = 1
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      end
    end
  end