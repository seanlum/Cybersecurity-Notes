echo '# Index' > README.md
find . -type f -name $"*.md" | awk '{ begin; gsub(/[ ]/, "%20",$0); print "- ["$0"]("$0")\n"; }' >> README.md
