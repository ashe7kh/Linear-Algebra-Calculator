from copy import deepcopy           #needed to prevent data from unintentionally being edited where it shouldn't

k = [[1,2,3,4],[1,3,4,5],[1,4,2,6],[1,5,1,7]]      #these are all stock matrices created for testing the algorithm
n = [[2,1,5],[3,4,3],[7,7,7]]                      #they are also stocked into the dictionary containing user data
m = [[1,0,0],[0,1,0],[0,0,1]]


#from here (line 9) to line 162 are all the linear algebra functions used

def crtsqmatrix(dimension):      #function to create square matrices
    g = []      #dummy variable g
    for i in xrange(dimension):
        g.append([])   #create x blank columns
    for j in xrange(dimension):
        for i in xrange(dimension):
            print "current element in a(ij) notation: a(" + str(j+1) + str(i+1) + ")"   #notify user what element is being input
            g[j].append(int(raw_input("input number:    ")))
    return g

def mulmat(matrix_a,matrix_b):
    x = len(matrix_a)  # get number of rows,
    if len(matrix_a) != len(matrix_b[0]): # make sure rows of pre = columns of post
        print "incompatible matrices"
    c = []    #dummy variable declarations
    f = []
    d = 0
    for i in xrange(0, x):    #prints both pre and post multiplier in order
        print matrix_a[i][0:]
    print "times"
    for i in xrange(0, x):
        print matrix_b[i][0:]
    print "equals"        #multiplication algorithm begins
    for k in xrange (0,x):           # after "x" iterations produces the product matrix
        for i in xrange(0,x):        # every "x" iterations produce a row of a matrix
            for j in xrange (0,x):   # every "x" iterations produce a dot product
                d += matrix_a[k][j]*matrix_b[j][i]     #algorithm to produce a part of a dot product within each iteration and aggregate to dummy variable
            c.append(d)             #dot product appended to a vector after each dot product
            d = 0                   #dummy variable value reset, to record values of next dot product
        f.append(c)          #row vector appended to what will be final product
        c = []               #row vector reset to record next row vector
    for i in xrange(0, x):
        print f[i][0:]
    return f

def transpose(matrix):
    x = len(matrix)       #dimensional information recorded to dummy variables
    y = len(matrix[0])    #
    b = []           #dummy matrix variable
    for i in xrange(0, x):    #create x rows in dummy matrix variable
        b.append([])

    for i in xrange(0, x):   #algorithm to  transpose
        for j in xrange(0, y):      #loop that appends elements of a to b in transpose order
            b[i].append(matrix[j][i])   #element "ji"  appended to row "i" making a(ij) = b(ji)
    a = b
    return a

def dis(matrix):     #function to display matrices
    x = len(matrix)
    for i in xrange(0, x):
        print matrix[i][0:]

def addmat(matrix_a,matrix_b):
    x = len(matrix_a)
    y = len(matrix_a[0])
    nu = []      #return variable
    c = 0        #dummy variable
    for i in xrange(0,x):
        nu.append([])
    if len(matrix_a) == len(matrix_b):
        if len(matrix_a[0]) == len(matrix_b[0]):    #"if" statements used to detmerine if matrices are compatible
            for i in range(0,x):
                for j in range(0,y):
                    c = matrix_a[i][j] + matrix_b[i][j]    #dummy variable records element addition
                    nu[i].append(c)          #dummy variable then appended to matrix
                    c = 0                    #dummy variable reset
    else:
        print "incompatible matrices"
        return 0
    return nu

def scalmul(scaler,matrix):
    child = deepcopy(matrix)
    for i in xrange(0, len(child)):
        for j in xrange(0, len(child[0])):
            child[i][j] *= scaler               #multiplies each element of matrix by scalar.

    dis(child)
    return child

def scaldiv(scaler, matrix):     #divides a matrix by a scaler
    child = deepcopy(matrix)
    for i in xrange(0, len(child)):
        for j in xrange(0, len(child[0])):
            child[i][j] = child[i][j]/float(scaler)              #divides each element of matrix by scalar.

    dis(child)
    return child

def powermat(power_raised,matrix):
    if power_raised == 1:
        dis(matrix)
        return matrix
    elif power_raised == 0:
        print "1"
        return 1
    b = matrix            #create matrix clone
    for i in xrange(power_raised):     #loop calculates each power up to c. most recent power of matrix stored in "a"
        matrix = mulmat(b, matrix)      #matrix "b" used to store original value of a, and multiply through each iteration
    print ""
    print "matrix to the " + str(power_raised) + "th power"
    dis(matrix)
    return matrix

def submat(matrix, row, column):   #creates minor that deletes row i and column j
    child = []
                        #algorithm to create a deep copy of
    for i in xrange(0, len(matrix)):
        vChild = []
        for j in xrange(0, len(matrix[i])):
            vChild.append(matrix[i][j])   #creates hard copy of each row and stores into vChild
        del vChild[column]               #deletes elements in column specified in function
        child.append(vChild)             #appends modified row into child
    del child[row]                       #deletes row specified in function

    return child

def determinant(matrix):      #finds determinant of matrix "a"
    if len(matrix) == 1:
        return matrix[0][0]               #determinant of a 1 by 1 matrix
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]    #determinant of a 2 by 2 matrix
    else:
        d = 0
        for j in xrange(len(matrix[0])):
            d += determinant(submat(matrix, 0, j)) * matrix[0][j] * ((-1)**j)      #recursive function that breaks matrix into smaller ones and finds determinants of those smaller matrices and feeds its back into the equation
        return d

def inverse(matrix):    #creates inverse of inputted matrix but does NOT divide out the determinant, to prevent large unseemly decimal places
    matrix_inverse = []
    for i in xrange(len(matrix)):
        matrix_inverse.append([])     #create blank matrix of same dimension as a
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix)):
            matrix_inverse[i].append(((-1)**(i+j))*determinant((submat(matrix, i, j))))      # creates co-factor matrix, appending each cofactor with each iteration
    matrix_inverse = transpose(matrix_inverse)    #creates transpose of co-factor matrix and stores into inverse matrix
    return matrix_inverse  #doesn't actually create inverse: matrix must be divided by determinant, however, that is done postfacto to simplify appearance of resulting matrix

def true_inverse(matrix):
    true_inverse_matrix = inverse(matrix)
    if determinant(matrix) == 0:
        print "singular matrix"           #makes sure that there is no division by zero
    else:
        true_inverse_matrix = scaldiv(determinant(matrix), true_inverse_matrix)
        return true_inverse_matrix

def inversemult(matrix):      #created to simplify appearance of resultant matrix. also created to check if "inverse" function works
    c = mulmat(matrix, inverse(matrix))     #multiplies matrix, creating diagnal matrix with determinant of matrix "a" along diagnal
    c = scaldiv((determinant(matrix)),c)    #divides out determinant leaving identity matrix
    return c

#end of linear algebra function library. beginning of UI section
user_var_dict = {'n': n,    #dictionary that contains all user created matrices and has them tagged with name
                 'k': k,    #this allows them to be called back with the name given to them by the user
                 'm': m}


def store_matrix(matrix, a):      #used to store matrices created by program into the dictionary "user_var_dict"
    store_com = raw_input("do you wish to store this matrix?   Y/N  ")  #variable "a" represents the name of a the matrix
    if store_com in ["y", "Y"]:
        store_com2 = raw_input("do you wish to store over matrix " + a + "?  Y/N  ")
        if store_com2 in ["y", "Y"]:
            user_var_dict[a] = matrix
        elif store_com2 in ["n", "N"]:
            a = raw_input("input new matrix name: ")
            user_var_dict[a] = matrix


co = 0   #variable used to keep while loop going indefinetely, until user ends program




while co < 1:  #while loop that contains code for the UI. loop has condition that will not be met and will run forever
    com = raw_input("Matrix manipulation program. must use created matrices for all operations\n"
                    "for help, enter 'help'\n"
                    "Enter Command:   ")   #all commands call corresponding function in linear algebra section
    if com == "help":     #gives a list of all commands
        print "end -- ends program \nhelp -- brings this menu \ncrt -- create a square matrix\n" \
              "inv -- take inverse of matrix\n" \
              "mu -- multiply matrices\ntran -- create transpose of matrix\n" \
              "disp -- display matrix\nscmu -- multiply matrix by scaler\nscdi - divide by scalar\n" \
              "pwr -- raise matrix to a power\ndet -- find determinant of matrix\n" \
              "co -- gives transpose of cofactor matrix\nview -- view all stored data"
    elif com == "end":    #ends program
        break
    elif com == "crt":    #command to create a matrix and store it
        a = raw_input("input matrix name: ")
        user_var_dict[a] = crtsqmatrix(int(raw_input("input dimension of matrix:   ")))
        print "you have created matrix " + a
        dis(user_var_dict[a])
        print "matrix: '" + a + "' has been stored"
    elif com == "pwr":
        a = raw_input("input matrix name: ")
        b = int(raw_input("input the exponent you wish to raise the matrix to: "))
        power_matrix = powermat(b, user_var_dict[a])
        store_matrix(power_matrix, a)
    elif com == "inv":
        a = raw_input("input matrix name: ")
        print "the inverse is"
        inverse = true_inverse(user_var_dict[a])
        print "you cannot store this matrix, sorry"
    elif com == "mu":
        a = raw_input("input pre-multiplier name: ")
        b = raw_input("input pre-multiplier name: ")
        resultant_matrix = mulmat(user_var_dict[a], user_var_dict[b])
        print "the product is:"
        dis(resultant_matrix)
        store_com = raw_input("do you wish to store this matrix? Y/N   ")
        if store_com in ["y", "Y"]:
            a = raw_input("input new matrix name: ")
            user_var_dict[a] = resultant_matrix
    elif com == "tran":
        a = raw_input("input matrix name: ")
        resultant_matrix = transpose(user_var_dict[a])
        print "the transpose is: "
        dis(resultant_matrix)
        store_matrix(resultant_matrix, a)
    elif com == "co":
        a = raw_input("input matrix name: ")
        resultant_matrix = inverse(user_var_dict[a])
        print "The transpose of the co-factor matrix is: "
        dis(resultant_matrix)
        store_matrix(resultant_matrix, a)
    elif com == "scmu":
        a = raw_input("input matrix name: ")
        b = int(raw_input("input scalar value to be multiplied: "))
        resultant_matrix = scalmul(b, user_var_dict[a])
        store_matrix(resultant_matrix, a)
    elif com == "scdi":
        a = raw_input("input matrix name: ")
        b = int(raw_input("input scalar value to be divided: "))
        resultant_matrix = scaldiv(b, user_var_dict[a])
        store_matrix(resultant_matrix, a)
    elif com == "disp":
        a = raw_input("input matrix name: ")
        dis(user_var_dict[a])
    elif com == "det":
        a = raw_input("input matrix name: ")
        print determinant(user_var_dict[a])
    elif com == "view":
        for key in user_var_dict:
            print key
            if len(user_var_dict[key]) >= 2:
                dis(user_var_dict[key])
                print ""
            else:
                print user_var_dict[key]
                print ""
    else:
        print "ERROR: INVALID COMMAND"
