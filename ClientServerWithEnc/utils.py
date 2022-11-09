

def enkrypt(s,k):
    n = len(s)
    ans = ""
    for i in range (0,k,1):
        j = i
        if i==0:
            while j<n:
                if(j<n):
                    ans = ans+s[j]
                j = (j+(k-i-1)*2)

        if i == k-1:
            while j<n:
                if j<n:
                    ans = ans+s[j]
                j = j + (i*2)
        if j<n:
            ans = ans + s[j]
        
        while j<n:
            j = j + ((k-i-1)*2)
            if j<n:
                ans = ans+s[j]
            
            j = j + (i*2)
            if j<n:
                ans = ans + s[j]
    
    return ans

def decrypt(s, k):
 
    # create the matrix to s
    # plain text k = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [['\n' for i in range(len(s))]
                  for j in range(k)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(s)):
        if row == 0:
            dir_down = True
        if row == k - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(k):
        for j in range(len(s)):
            if ((rail[i][j] == '*') and
               (index < len(s))):
                rail[i][j] = s[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(s)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == k-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
 
