from   __future__ import  division
from   __future__ import  unicode_literals

def test():
    print '\'xxx\' is unicode?',isinstance('xxx',unicode)
    print 'u\'xxx\' is unicode?',isinstance(u'xxx',unicode)
    print '\'xxx\' is str? ',isinstance('xxx',str)
    print 'b\'xxx\' is str?',isinstance(b'xxx',str)
    print '10/3=',10/3
    print '10//3=',10//3




if __name__=="__main__":
    test()