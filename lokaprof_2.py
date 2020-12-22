def open_file(file_name): # Do not change this line
    '''Opens the given filename and returns its file object, or None if not found'''
    try:
        file_object = open(file_name, 'r')
        return file_object
    except FileNotFoundError:
        return None
    
def read_matrix(file_object): # Do not change this line
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    line_list = file_object.readlines()
    return [[int(n) for n in line.split()] for line in line_list]
    

def row_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    row_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != row_sum:
            return 0
    return row_sum

def col_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    col_matrix = rotate_matrix(matrix)
    return row_sum_same(col_matrix)

def matrix_has_same_sums(matrix):
    '''Returns true if matrix has same sums, else returns false '''
    if row_sum_same(matrix) != 0:
        if col_sum_same(matrix) != 0:
            return True
    return False

def rotate_matrix(matrix):
    ''' Takes in an nxn matrix and rotates it 90 degrees'''
    boundary = len(matrix[0])
    rotated_matrix = []
    for i in range(boundary):
        rotated_matrix_line = []
        for n in range(boundary):
            rotated_matrix_line.append(matrix[n][i])
        rotated_matrix.append(rotated_matrix_line)
    return rotated_matrix

def print_matrix(matrix):
    for line in matrix:
        print('\t'.join(str(element) for element in line)+'\t') #had to add '\t' to get passed

def main(): # Do not change this line
    filename = input('File name: ')
    file_object = open_file(filename)
    if file_object == None:
        print('File not found')
    else:
        matrix = read_matrix(file_object)
        print_matrix(matrix)
        if matrix_has_same_sums(matrix):
            print('Same sums')
        else:
            print('Not same sums')
    

# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()