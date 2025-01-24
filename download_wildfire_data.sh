# read the links from  csv
while IFS= read -r line; do
    echo "Downloading data from : $line"
    # download the data from  the read links
    curl -C - -o data/wildfires.zip "$line"
done < wildfire_data_links.txt
