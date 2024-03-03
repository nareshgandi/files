Install aws cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version 
aws configure

sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform

terraform init
terraform plan
terraform apply
   
https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/

Downloading and installing Jenkins

sudo yum update –y
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo yum upgrade
sudo dnf install java-17-amazon-corretto -y
sudo yum install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

Configuring Jenkins
Jenkins is now installed and running on your EC2 instance. To configure Jenkins:

Connect to http://<your_server_public_DNS>:8080 from your browser. 
You will be able to access Jenkins through its management interface:

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

On the left-hand side, select Manage Jenkins, and then select Manage Plugins.

Select the Available tab, and then enter Amazon EC2 plugin at the top right.

Select the checkbox next to Amazon EC2 plugin, and then select Install without restart.

Add amazon EC2 plugin
