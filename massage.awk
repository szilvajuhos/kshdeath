BEGIN{
	# print header
	print "\"date\",\"0–34\",\"35–39\",\"40–44\",\"45–49\",\"50–54\",\"55–59\",\"60–64\",\"65–69\",\"70–74\",\"75–79\",\"80–84\",\"85–89\",\"90+\"";
	FS=";";
}
# print the rest
/^;/ || /^20/{
	# date
	printf("%s,",$4);
	# print only the totals, but only for age groups
	for(i=13;i>=2;i--) {
		death = $(NF-i);
		sub(" ","",death);
		printf("%s,",death);
	}
	# last value without comma
	death = $(NF-1);
	sub(" ","",death);
	printf("%s\n",death);
}
