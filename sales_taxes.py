import math
taxfree_products = ['books', 'chocolates', 'headache pills' ] # tax free product list , i assume 3 items for this problem according to input case but we can add more items and can do many things here!!
input_case = 3  ## iteration number for input case according to the assignment here is 3

## round up a float to nearest 0.05
def roundUp_nearest(x, a):
    return math.ceil(x / a) * a

# def findSub_string(a, b):
#     for word in a:      
#         if word not in b: continue
#         else : return True
#     return False    

print('\nPlease press ENTER key 2 times to stop input operation ')
for j in range(input_case):
    input_list = [] 
    output_list = []
    total = 0 ## total price of all items include tax
    sales_taxes = 0 ## total taxes
    print('Input {}:\n'.format(j+1))
    ## infinte loop for taking input items 
    ## break loop while press double 'ENTER' key
    while True:
        input_item = input()
        if input_item == '': break
        else: input_list.append(input_item)

    for i in range(len(input_list)):

        v = input_list[i].split() ## split each entry of input list so that we can access eash word by index.
        p = int(v[0]) * float(v[-1]) # price = number of items * item value 
        t = 0 # tax for each item , intial valu 0

        ## first check whether our product imported or not. if imported and not included in taxfree_products list
        ## calculate both sales tax and duty fees
        ## otherwise calculate only duty fees for imported product
        if 'imported' in v:
            if not next((True for word in v[1:-2]  if word in  "!".join(taxfree_products)), False):
                t =  roundUp_nearest((5 * p)/ 100 + (10 * p)/ 100, 0.05) ##calculate both tax and duty fees
            else :  t =  roundUp_nearest((5 * p)/ 100, .05)   ## calculate only tax 
            v[-1] = str(format(float(v[-1]) + t, '.2f')) ## update last element of v list
            sales_taxes = sales_taxes + t ## update our sales taxes

            ## not imported and not tax free items
        elif not next((True for word in v[1:-2]  if word in  "!".join(taxfree_products)), False): ## use next()  to find first true and return without further searching 
            t =  roundUp_nearest((10 * p)/ 100, .05)
            v[-1] = str(format(float(v[-1]) + t, '.2f')) ## formating v list to show appropriate output according to assignment output pattern
            sales_taxes = sales_taxes + t

        total  = total + p + t ## update totat prices included taxes(all kinds)
        v.remove(v[-2]) ## formating v list to show appropriate output according to assignment 
        v[-2] = v[-2]+':' ## same thing here
        output_list.append(' '.join(v)) ## make a string with white space from v and push it to output list

    print('Output {}:\n'.format(j+1))
    ## print output 
    for i in output_list:
        print(i)    
    print('Sales Taxes: ',format(sales_taxes, '.2f'))
    print('Total: ', format(total, '.2f'))
    print('\n')
