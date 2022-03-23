import math
taxfree_products = ['book', 'chocolate', 'headache pills' ]
input_case = 1


def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

for j in range(input_case):
    input_list = []
    output_list = []
    total = 0
    sales_taxes = 0

    print('input {}\n'.format(j+1))
    while True:
        input_item = input()
        if input_item == '': break
        else: input_list.append(input_item)

    for i in range(len(input_list)):
        
        v = input_list[i].split()
        p = int(v[0]) * float(v[-1])
        t = 0
        if not(any(word in input_list[i] for word in taxfree_products)):
            t =  round_nearest((10 * p)/ 100, .05)
            v[-1] = str(format(float(v[-1]) + t, '.2f'))
            sales_taxes = sales_taxes + t
        total  = total + p + t
        v.remove(v[-2])
        v[-2] = v[-2]+':'
        output_list.append(' '.join(v))

    print('output {}\n'.format(j+1))
    for i in output_list:
        print(i)    

    print('Sales Taxes: ',format(sales_taxes, '.2f'))
    print('Total: ', format(total, '.2f'))
