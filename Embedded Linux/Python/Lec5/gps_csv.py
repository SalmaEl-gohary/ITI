import csv

#function to handle gps data
def parse_gps(data):
	data = data.split(",")
	parsed = []
	
	#convert latitude & append to list
	parsed.append((float(data[1]) //100)+ ((float(data[1]) % 100)/60))
	parsed.append(data[2])
	
	#convert longitude & append to list
	parsed.append((float(data[3]) //100) + ((float(data[3]) % 100)/60))
	parsed.append(data[4])
	
	#convert time & append to list
	hrs = int(float(data[5]) // 10000)
	min = int(float(data[5]) // 100 % 100)
	sec = int((float(data[5]) %100))
	time = str(hrs) + ":" + str(min) + ":" + str(sec)
	
	
	parsed.append(time)
	
	return parsed

#list that has the fields of csv file 
fields = ["Latitude", "N/S", "Longitude", "E/W", "UTC Time"]

#data to parse
gps_data = "$GPGLL,3401.21044,N,11824.67722,W,044840.00,A,D*7F"



parsed = parse_gps(gps_data)


filename = "gps_data.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data row & could use writerows for multiple rows 
    csvwriter.writerow(parsed)








