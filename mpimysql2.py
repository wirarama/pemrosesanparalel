from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="mpi",
  password="mpi",
  database="mpitest"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM tabelnum WHERE (suhu BETWEEN '%s' AND '%s') AND (kelembaban BETWEEN '%s' AND '%s')"
val = (((rank*100)+2800/100),((rank*100)+2900/100),((rank*10)+40),((rank*10)+60))
"""
if rank == 0:
    sql = ""
elif rank == 1:
    sql = ""
"""
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print("rank %d memiliki %s data \n\n" % (rank,len(myresult)))
data = comm.gather(myresult, root=0)
if rank == 0:
    print("rank %d memiliki %s data yaitu :\n %s \n\n"%(rank,len(data),str(data)))