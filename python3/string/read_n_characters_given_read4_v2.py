""" 
Given a file and assume that you can only read the file using a given method read4, 
implement a method to read n characters.  Your method read may be called multiple times.

Method read4:

    The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

    The return value is the number of actual characters read.

    Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    def read(buf4: list) -> n
    Parameter:  buf4 and array that will return the next characters from the file.
    Returns:    int

Note that buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

Below is a high-level example of how read4 works:

    File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
    char[] buf4 = new char[4]; // Create buffer with enough space to store characters
    read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
    read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
    read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

buf[] is a destination, not a source. You will need to write the results to buf[].

Note:

  * Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
  * The read function will only be called once for each test case.
  * Please remember to RESET your class variables declared in Solution,
    as static/class variables are persisted across multiple test cases.
  * You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
  * It is guaranteed that in a given test case the same buffer buf is called by read.

Example 1:
    Input: file = "abc", queries = [1,2,1]
    Output: [1,2,0]
    Explanation: The test case represents the following scenario:
      File file("abc");
      Solution sol;
      sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
      sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
      sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
      Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.

Example 2:
    Input: file = "abc", queries = [4,1]
    Output: [3,0]
    Explanation: The test case represents the following scenario:
      File file("abc");
      Solution sol;
      sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
      sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 
Constraints:
    1 <= file.length <= 500
    file consist of English letters and digits.
    1 <= queries.length <= 10
    1 <= queries[i] <= 500

Technologies:
  * Class attribute
  * pop(0)
  
"""

  
file_buffer = []
fp = 0

def set_file_buffer(b):
    global file_buffer, fp
    file_buffer = b
    fp = 0

def read4(buf4):
    global file_buffer
    global fp
    nread = 0
    for i in range(4):
        if fp < len(file_buffer):
            buf4[i] = file_buffer[fp]
            fp += 1
            nread += 1
    return nread


from typing import List

class Solution:

    class_buffer = []

    def read(self, buf: List[str], n: int) -> int:
        # Read class buffer
        i = 0
        while self.class_buffer and i < n:
            # pop is not very efficient; yet the operation is limited to 3
            buf[i] = self.class_buffer.pop(0)
            i += 1

        # Read buf4
        buf4 = [''] * 4
        while i < n:
            remain = n - i
            nread = read4(buf4)
            if nread == 0:
                break

            # Calculate how many to take from buf4
            if nread <= remain:
                ntake = nread
                nkeep = 0
            else:
                ntake = remain
                nkeep = nread - remain

            # Copy to the return buffer
            if ntake:
                buf[i:i+ntake] = buf4[0:ntake]
                i += ntake

            # Copy to the class buffer
            if nkeep:
                self.class_buffer = buf4[ntake:ntake+nkeep]
                break

        return i


def main():
    test_data = [
        ["abc", [1,2,1], [1,2,0]],
        ["abc", [4,1], [3,0]],
        ["leetcode", [1,4,4], [1,4,3]],
    ]

    ob1 = Solution()
    for file_buf, queries, ans in test_data:
        print(f"\n# Input = {file_buf}, {queries}, {ans}")

        # Set file buffer
        set_file_buffer(file_buf)
        # print(f"[DEBUG] file_buffer={file_buffer}, fp={fp}")

        # Prepare the read buffer
        n = sum(queries)
        for q in queries:
            buf = [''] * q
            nread = ob1.read(buf, q)
            print(f"  read({q}) => {buf} (nread = {nread})")


if __name__ == "__main__":
    main()

