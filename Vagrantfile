Vagrant.configure("2") do |config| # API version vagrant 
    config.vm.box = "ubuntu/focal64" # Version VM

    config.vm.define "app-server" do |app|
        app.vm.network "private_network", ip: "192.168.56.10"
        app.vm.provider "virtualbox" do |vb|
            vb.memory = "1024"
            vb.cpus = 1
        end
    end


    config.vm.define "monitoring-server" do |mon|
        mon.vm.network "private_network", ip: "192.168.56.20"
        mon.vm.network "forwarded_port", guest: 3000 , host: 3000
        mon.vm.network "forwarded_port", guest: 9090 , host: 9090
        mon.vm.provider "virtualbox" do |vb|
            vb.memory = "1024"
            vb.cpus = 1
        end
    end
end
