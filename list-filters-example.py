payments = [{"amount":"100.00", "course":"0001"}, {"amount":"150.00", "course":"0002"}, {"amount":"110.00", "course":"0001"}, {"amount":"200.00", "course":"0003"},
            {"amount":"300.00", "course":"0002"}, {"amount":"100.00", "course":"0001"}, {"amount":"100.00", "course":"0001"}, {"amount":"100.00", "course":"0001"}]
extended_payments = [{"amount":"150.00", "course":{"name":"Course 1", "id":"0001"}}, {"amount":"250.00", "course":{"name":"Course 2", "id":"0002"}}]
s = set(val for dic in payments for val in dic.values())
unique_values = set(dic['course'] for dic in payments)
courses_list = list(dic['course'] for dic in payments)
count_list = []

for value in unique_values:
    count_dict = {}
    count_dict['amount'] = courses_list.count(value)
    count_dict['course'] = value
    count_list.append(count_dict)
    #count_dict[value] = courses_list.count(value)
    print(courses_list.count(value))
print(count_list)

unique_course_ids = set(dic['course']['id'] for dic in extended_payments)
print(unique_course_ids)

#print(payments[0])
#print(type(payments[0]))
#print(payments[0]['amount'])
#print(payments[0].values())
#print(s)
#print(unique_values)
#print(courses_list)