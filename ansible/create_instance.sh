ansible 127.0.0.1 -m ec2 -a "image=ami-be1c848e instance_type=t1.micro keypair=ansible-test.pem group=ec2-servers region=us-west-2 wait=true" -c local
