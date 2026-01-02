wc -l data/raw/records_2022.csv
wc -l data/raw/records_2023.csv

^
total number of lines to check dataset size


grep "NULL" data/raw/normalized_records_2022.csv
grep "NULL" data/raw/normalized_records_2023.csv

^
show every occurence of NULL in dataset, every row where NULL is found


cut -d ',' -f 2 data/raw/records_2022.csv | sort | uniq
cut -d ',' -f 2 data/raw/records_2023.csv | sort | uniq

^
show eveything found on column 2 or just any column(change 2 in whatever) then it's sorted and it's shown every unique value to see what values are found there. 
It was useful for category, for example, to properly see all the ways the categories are written with full caps, with all lower cases, etc.


grep "review" data/raw/records_2023.csv > data/interim/flagged_for_review.csv

^
dataset filter all initial records flagged for review and redirect output to a new file


head -q -n 1 data/raw/*.csv

^
check headers from both raw files to compare schema over the years