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
            result = [data_points for data_points in cursor.fetchall()]
            
            yield result
              
#            for data_catch in cursor.fetchall():
#                yield DataRow(data_catch)
#                print(data_catch) # alright, this looks like it is working, data is being returned.
            
    return DataRow  # this is not correct... returns the attribute, I want to 
    
# There is a testing framework now. Please ignore this.
#if __name__ == "__main__":
#    import mysql.connector
#    from database import login_info
#    db = mysql.connector.Connect(**login_info)
#    c = db.cursor()
#
##    id, name, family, weight = ('1', 'Sillyface', 'Sheep', '50')
#    
#    a = build_row('animal', 'id', 'name', 'family', 'weight', 
#                  cursor=c, condition="WHERE name ='Peaches'")
#    
#    a.retrieve(a,cursor=c, condition="WHERE name ='Peaches'")
##    print(a)
