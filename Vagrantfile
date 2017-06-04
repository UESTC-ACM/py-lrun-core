Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision "shell" do |s|
    s.inline = "sudo apt-get -y update && sudo apt-get -y install build-essential python2.7"
  end
  config.vm.network "forwarded_port", guest: 8080, host: 8080
end
