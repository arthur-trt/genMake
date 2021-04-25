## SOURCES.MK ##

## TEST ##

SOURCES		+=                                       		\
		test/file.c                                     	\
		test/file_bonus.c                               	\


## TEST/TEST1 ##

SOURCES		+=                                       		\
		test/test1/file3.c                              	\
		test/test1/file2.c                              	\
		test/test1/file_bonus.c                         	\
		test/test1/file1.c                              	\


## TEST/TEST2 ##

SOURCES		+=                                       		\
		test/test2/file5.c                              	\
		test/test2/file4.c                              	\
		test/test2/file2_bonus.c                        	\


## TEST/TEST2/TEST3 ##

SOURCES		+=                                       		\
		test/test2/test3/file7.c                        	\
		test/test2/test3/superlongfilefortesting.c      	\
		test/test2/test3/file6.c                        	\


## BONUS ##

SOURCES_BONUS	+= $(SOURCES)                       			\
		test/file_bonus.c                               	\
		test/test1/file_bonus.c                         	\
		test/test2/file2_bonus.c                        	\


