Vagrant.configure("2") do |config| # API version vagrant 

    config.vm.box = "ubuntu/jammy64" # Version VM
    config.vm.hostname = "mr-penya" # Name VM

    config.vm.network "forwarded_port", guest:3000, host:3000 # Standart port for Grafana
    config.vm.network "forwarded_port", guest:8080, host:8080 # Standart port for Jenkins
    config.vm.network "forwarded_port", guest:9090, host:9090 # Standart port for Prometheus
    config.vm.network "private_network", ip: "192.168.56.10"
   
    config.vm.provider "virtualbox" do |vb| # Settings Vb
        vb.memory = 2048 
        vb.cpus = 2
        vb.name = "mr-penya"
    end   
end     
