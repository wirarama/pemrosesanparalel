from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank==0:
    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="mpi",
      password="mpi",
      database="mpitest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tabelnum")
    myresult = mycursor.fetchall()
    from bagikerja import bagikerja
    data = bagikerja(myresult,size)
else:
    data = None
data = comm.scatter(data, root=0)
print("rank %d memiliki %s data yaitu :\n %s \n\n"%(rank,len(data),str(data)))