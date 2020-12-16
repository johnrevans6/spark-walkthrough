Vagrant.configure("2") do |config|
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", 2048]
  end

  config.vm.box = "paulovn/spark-base64"
  config.vm.hostname = "spark.local"

  config.vm.network :forwarded_port, guest: 8888, host: 8888
  config.vm.network :forwarded_port, guest: 4040, host: 4040, auto_correct: true
  config.vm.network :forwarded_port, guest: 4041, host: 4041, auto_correct: true

  config.vm.provision :shell, privileged: true, :path => "helpers/configure_jupyter.sh"
  config.vm.provision :shell, privileged: true, :path => "helpers/load_kernel.sh"
end