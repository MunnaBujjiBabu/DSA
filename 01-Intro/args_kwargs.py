
def my_normal(a):   #function definition
    print(a)


#args
def my_args(*args):
    print(args)



#kwargs
def my_kwargs(**kwargs):
    print(kwargs)
    


my_normal(1)
#my_args()
#my_args(10, 11, 12, 13, 'test', 'my_key':'my_value') 
my_args(10, 11, 12, 13, 'test')

my_kwargs(test= 'myvalue12', test2='myvalue134')

my_dictionary = {'test': 'myvalue12', 'test2': 'myvalue124'}
print(my_dictionary)


def my_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

my_args_kwargs(1, 2, 3, test='value1', test2= 'value2')


