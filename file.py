import csv
op=open('output.csv','w')
op.write("credit_card_number,ipv4,state"+'\n')
prefix=['5018', '5020', '5038', '56','51', '52', '54', '55', '222','4','34', '37','6011', '65','300', '301', '304', '305', '36', '38','35','2131','1800']
with open('transaction-001.csv', mode ='r')as file:
	for line in file:
		ent_line=line.strip()
		new=ent_line.split(",")[0]
		for code in prefix:
			if new.startswith(code):
				###print(new)
				op.write(ent_line+"\n")
				break
op.close()
op=open('output.csv','a')
with open('transaction-002.csv', mode ='r')as file:
	for line in file:
		sec_line=line.strip()
		new=sec_line.split(",")[0]
		for code in prefix:
			if new.startswith(code):
				###print(new)
				op.write(sec_line+"\n")
				break
op.close()
out=open('output.csv','r')
Lines = out.readlines()
fraudulent=open('fraudulent.csv','w')
with open('fraud.csv', mode ='r')as file_1:
	for line in file_1:
		fraud=line.strip()
		new_f=fraud.split(",")[0]
		for line in Lines:
			if new_f in line:
				fraudulent.write(line+"\n")
				break
			
out.close()
fraudlent.close()			
		
