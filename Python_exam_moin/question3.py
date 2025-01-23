def sales_data_analysis(sales_data):
	Total_sales = 0
	Average_sales = 0
	sales_data_result = {}
	result = {}
	HSP = {} #High selling product dictionary
	for i in range(len(sales_data)):
		Total_sales += sales_data[i]["sale_amount"]
		if sales_data[i]["product_id"] not in HSP.keys():
			HSP[sales_data[i]["product_id"]] = sales_data[i]["sale_amount"] #add key as product id and value as sale amount
		else:
			HSP[sales_data[i]["product_id"]] += sales_data[i]["sale_amount"] #add sale_amount existing product_id
		
	Average_sales = Total_sales/len(sales_data)
	max_key_value = [0,0] #initialize list to storing max sale_amount index 0 and product id index 1
	for key,value in HSP.items():
		if value >= max_key_value[0]:
			max_key_value[0] = value
			max_key_value[1] = key
	#finding product_name using product_id		
	for i in range(len(sales_data)):
		if sales_data[i]['product_id'] == max_key_value[1]:
			HSP.clear()
			HSP['product_id'] = sales_data[i]['product_id']
			HSP['product_name'] = sales_data[i]['product_name']
			break
	
	result['Total_sales'] = Total_sales
	result['Average_sales'] = Average_sales
	result['High-selling-price'] = HSP
	
	return result
	
	
	

sales_data = [
{"product_id": 101, "product_name": "Smartphone", "sale_amount": 500, "sale_date": "2025-01-01"},
{"product_id": 102, "product_name": "Laptop", "sale_amount": 300, "sale_date": "2025-01-02"},
{"product_id": 101, "product_name": "Smartphone", "sale_amount": 400, "sale_date": "2025-01-03"},
{"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700, "sale_date": "2025-01-04"},
]

print(sales_data_analysis(sales_data))

	
