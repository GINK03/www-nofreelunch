aws ec2 run-instances --image-id ami-5a7dc03a --count 1 --instance-type t1.micro --key-name ansible-test --security-groups ansible-group | jq '.'
