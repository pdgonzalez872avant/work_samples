"""
Project 11 - adding retrieve to classFactory.
"""

def build_row(table, *cols, cursor, condition):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data) == len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        
        def retrieve(self, cursor, condition=None):
#            print('Inside retrieve')  # I'm in the function! Yeah!
            if condition:
                sql = "SELECT * FROM animal" + " " + condition
#                print(condition)  # works as well
            else:
                sql = "SELECT * FROM animal"
            cursor.execute(sql)

            # Attempt xx
            for d in cursor.fetchall(): # 
#                print(DataRow(d)) # 
                yield DataRow(d) # - [<class 'project11.build_row.<locals>.DataRow'>, <class 'project11.build_row.<locals>.DataRow'>]

            
    DataRow.table = table # AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    DataRow.cols = cols # AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH  
    
    return DataRow  