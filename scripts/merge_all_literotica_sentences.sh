# Create one sentences file from data/literotica-stories/sentences
# Usage: bash merge_all_literotica_sentences.sh ../data/literotica-stories/all-sentences-0.1.

touch $1

for filename in ../data/literotica-stories/sentences-0.1/*.txt; do
  cat $filename >> $1
done

