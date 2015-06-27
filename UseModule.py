from TestModule import a        # get only function a() from module 'TestModule'    other ways:    from TestModule import a,b         or      from TestModule import *

print( a() )


# if we use:   import TestModule,   the we have to use:      print( TestModule.a() )