#see to it that your college wifi/isp hasnt blocked port 21 
import ftplib
session = ftplib.FTP_TLS('domain name','username','password')
file = open('encodings.pickle','rb')                  # file to send
session.storbinary('STOR encodings.pickle', file)     # send the file
file.close()                                    # close file and FTP
session.quit()