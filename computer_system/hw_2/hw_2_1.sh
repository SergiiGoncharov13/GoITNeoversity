sites=("https://google.com" "https://facebook.com" "https://twitter.com")

logfile="check.log"

# Clear log file
> "$logfile"

for site in "${sites[@]}"
do
    echo "$site"
    if curl  -o /dev/null -s -L --head --request GET -w "%{http_code}\n" "$site" | grep 200 > /dev/null
    then 
        echo "$site is UP" >> "$logfile"
    else
        echo "$site is DOWN" >> "$logfile"
    fi
done

echo "Result written to $logfile"