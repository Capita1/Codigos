apps=("waybar" "wpaperd" "swaync") ; len=${#apps[@]} ; n=0
while [ $len -ge $n ]; do
	app=${apps[$n]}	
	killall $app
	$($app)
	let "n++"
done


