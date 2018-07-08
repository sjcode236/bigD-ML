
passwd hadoop
hd123


vi /etc/hosts
192.168.56.131  centosNN
192.168.56.132  centosNN2
192.168.56.141  centosDN
192.168.56.142  centosDN2
192.168.56.143  centosDN3

chkconfig ntpd on
service ntpd start
chkconfig --list ntpd

cd /etc/yum.repos.d
wget  http://public-repo-1.hortonworks.com/ambari/centos6/1.x/updates/1.4.3.38/ambari.repo

http://capnjosh.com/blog/installing-hortonworks-hadoop-ambari-server/

===================================================
Ambari Install Guide from  hotron works 
