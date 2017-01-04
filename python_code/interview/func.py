import sys
sys.path.insert(0, '/home/olyaza/Desktop/fyber/python_code/')
import main


file_name = "/home/olyaza/Desktop/fyber/data-science-challenge-master/challenge_training_data.csv"

data = main.read_data(file_name)
#print("test",data)
print("test",len(data[:,0]))

#t, ad_id, country, app_id, net, click = main.read_data2(file_name)

main.distinct_values_and_top5(data)
main.feature_comb_per_impression(data)

