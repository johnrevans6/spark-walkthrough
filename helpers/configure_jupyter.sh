#!/bin/bash
mkdir /home/vagrant/.jupyter
mkdir /etc/jupyter
cp "/vagrant/helpers/jupyter_notebook_config.py" /home/vagrant/.jupyter
chown vagrant:vagrant /home/vagrant/.jupyter/jupyter_notebook_config.py
systemctl enable notebook
/opt/ipnb/bin/python /vagrant/helpers/install_extensions.py
ln -fs /opt/ipnb/share/jupyter/pre_pymarkdown.py /opt/ipnb/lib/python?.?/site-packages
chmod 775 /opt/ipnb/bin/jupyter-notebook-mgr
rm -f /usr/sbin/jupyter-notebook-mgr
ln -s /opt/ipnb/bin/jupyter-notebook-mgr /usr/sbin

cat <<-EOF >> /etc/jupyter/jupyter-notebook
NOTEBOOK_USER="vagrant"
NOTEBOOK_SCRIPT="/opt/ipnb/bin/jupyter-notebook"
NOTEBOOK_BASEDIR="/vagrant/labs"
EOF
jupyter-notebook-mgr set-mode "local"
systemctl start notebook


