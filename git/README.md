# How to install Git in ec2 instance?
sudo yum update -y
sudo yum install gh -y
sudo yum install github -y
type -p yum-config-manager >/dev/null || sudo yum install yum-utils
sudo yum-config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo yum install gh
sudo yum update gh
gh auth login
