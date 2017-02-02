aws ec2 request-spot-instances \
	--launch-specification file://spec.json \
	--block-duration-minutes 120 \
	--type "one-time" \
	--spot-price "0.98"
	

