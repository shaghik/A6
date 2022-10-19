from unitTest import unitTest as ut

ut.test_equal('ABC', 'ABC')

ut.test_num_equal((3*3)+3, 12)

a = 3
b = 3

ut.testAdd(a,b, 6)

try:
    ut.testAddFail(a,b,6)
except:
    print('failed add method test')


print('Success')