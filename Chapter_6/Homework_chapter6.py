with open('measurements.txt') as measurements_object:
    measurement_list = measurements_object.readlines()
    for x in measurement_list:
        x.split('/n')


measurement_dict = {}
for x in measurement_list:
    if x[0] not in measurement_dict:
        list(measurement_dict[x[0]]).append(x[1])
    else:
        pass



print(measurement_dict)
