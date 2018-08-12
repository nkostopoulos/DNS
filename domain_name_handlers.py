def separate_domain(fqdn,domain_name):
	fqdn_parts=fqdn.split('.')
	domain_name_parts=domain_name.split('.')
	variable_part_list=[element for element in fqdn_parts if element not in domain_name_parts]
	return variable_part_list

def get_variable_part_string(fqdn,domain_name):
	dom_name_length=len(domain_name)
	fqdn_length=len(fqdn)
	variable_part_string=fqdn[0:(fqdn_length-dom_name_length)]
	return variable_part_string

def count_labels(variable_part_list):
	return len(variable_part_list)

def count_label_characters(variable_part_list):
	per_label_chars=[len(label) for label in variable_part_list]
	return per_label_chars

def count_total_characters(per_label_chars):
	sum=0
	for number in per_label_chars:
		sum=sum+number
	return sum

def find_bigrams(variable_part_string):
	variable_part_string_length=len(variable_part_string)
	bigrams=[variable_part_string[i:(i+2)] for i in range(0,variable_part_string_length)]
	return bigrams

def find_trigrams(variable_part_string):
	variable_part_string_length=len(variable_part_string)
	trigrams=[variable_part_string[i:(i+3)] for i in range(0,variable_part_string_length)]
	return trigrams

def test_function():
	variable_part=separate_domain('www.dolly.netmode.ece.ntua.gr','ntua.gr')
	print(variable_part)
	variable_part_string=get_variable_part_string('www.dolly.netmode.ece.ntua.gr','ntua.gr')
	print(variable_part_string)
	total_labels=count_labels(variable_part)
	print(total_labels)
	per_label_chars=count_label_characters(variable_part)
	print(per_label_chars)
	sum=count_total_characters(per_label_chars)
	print(sum)
	bigrams=find_bigrams(variable_part_string)
	print(bigrams)
	trigrams=find_trigrams(variable_part_string)
	print(trigrams)

test_function()

