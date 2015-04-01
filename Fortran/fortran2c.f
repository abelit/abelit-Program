C   fortran2c.f
C
        PROGRAM FORTRAN2C
C
        CHARACTER*32 HELLO
        REAL PI
C
        HELLO = "Hello C from Fortran"
        HELLO(21:21) = CHAR(0)
        PI = 3.14159
        CALL SHOWHIPI(HELLO,PI)
        END PROGRAM FORTRAN2C
